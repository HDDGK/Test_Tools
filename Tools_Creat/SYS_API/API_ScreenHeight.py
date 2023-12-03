import ctypes
from ctypes import wintypes
def get_taskbar_height():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    MONITOR_DEFAULTTOPRIMARY = 1
    x, y = 0, 0
    hMonitor = user32.MonitorFromPoint(wintypes.POINT(x, y), MONITOR_DEFAULTTOPRIMARY)

    class MONITORINFO(ctypes.Structure):
        _fields_ = [
            ("cbSize", wintypes.DWORD),
            ("rcMonitor", wintypes.RECT),
            ("rcWork", wintypes.RECT),
            ("dwFlags", wintypes.DWORD)
        ]

    monitor_info = MONITORINFO()
    monitor_info.cbSize = ctypes.sizeof(monitor_info)
    user32.GetMonitorInfoA(hMonitor, ctypes.pointer(monitor_info))

    screen_height = monitor_info.rcMonitor.bottom - monitor_info.rcMonitor.top
    available_height = monitor_info.rcWork.bottom - monitor_info.rcWork.top
    taskbar_height = screen_height - available_height

    return taskbar_height


if __name__ == "__main__":
    taskbar_height = get_taskbar_height()
    print("Taskbar height:", taskbar_height)