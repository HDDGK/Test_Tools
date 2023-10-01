import speech_recognition as sr

# 创建语音识别器对象
r = sr.Recognizer()
path=r"C:\Users\HK145\Desktop\新建文件夹\try.wav"

# 打开音频文件
with sr.AudioFile(path) as source:
    # 从音频文件中读取数据
    audio_data = r.record(source)

# 将音频转换为文字
text = r.recognize_google(audio_data, language='zh-CN')
if text=="siri":
    print("找我啥事")


# 打印转换结果
print(text)