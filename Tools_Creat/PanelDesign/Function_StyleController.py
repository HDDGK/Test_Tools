from PyQt5.QtCore import QObject, QTime, QTimer

class StyleController(QObject):
    def __init__(self, main_window, style_controller, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.style_controller = style_controller
        self.custom_menubar = custom_menubar
        self.auto_update = True

        timer = QTimer(self)
        timer.timeout.connect(self.update_style_based_on_time)
        timer.start(6 * 1000)  # 每10分钟检查一次

        self.update_style_based_on_time()

    def update_style_based_on_time(self):
        if not self.auto_update:
            return
        current_time = QTime.currentTime()

        if QTime(20, 0) <= current_time < QTime(22, 0):
            self.custom_menubar.set_medium_eye_protection_mode(self.main_window)
        elif QTime(22, 0) <= current_time < QTime(24, 0) or QTime(0, 0) <= current_time < QTime(6, 0):
            self.custom_menubar.set_strong_eye_protection_mode(self.main_window)
        elif QTime(6, 0) <= current_time < QTime(7, 0):
            self.custom_menubar.set_medium_eye_protection_mode(self.main_window)
        elif QTime(7, 0) <= current_time < QTime(8, 0):
            self.custom_menubar.set_light_eye_protection_mode(self.main_window)
        elif QTime(8, 0) <= current_time < QTime(9, 0):
            self.custom_menubar.set_day_mode(self.main_window)
        elif QTime(18, 0) <= current_time < QTime(20, 0):
            self.custom_menubar.set_light_eye_protection_mode(self.main_window)
        else:
            self.custom_menubar.set_day_mode(self.main_window)