'''
monitor
controller
app
'''
import pyaudio

import pyaudio
import wave
import numpy as np
path=r"C:\Users\HK145\Desktop\新建文件夹\try2"
waitime=5
BoolListing = False


def audioToWord(path):
    import speech_recognition as sr

    # 创建语音识别器对象
    r = sr.Recognizer()


    # 打开音频文件
    with sr.AudioFile(path) as source:
        # 从音频文件中读取数据
        audio_data = r.record(source)

    # 将音频转换为文字
    text = r.recognize_google(audio_data, language='zh-CN')
    print(text)
    if text=="小爱同学":
        print("小爱在听，需要协助吗？")
        print("调用录音","小爱同学")
        Monitor_MIC(300, path)
        BoolListing = True
    if BoolListing==True:
        if text=="微信":
            print("打开微信")

    # 打印转换结果
    #

def Monitor_MIC(th,filename):
    CHUNK=512
    FOMART=pyaudio.paInt16
    CHANNLS=1
    RATE=16000
    WAVE_OUTPUT_FILENAME=filename+".wav"
    p=pyaudio.PyAudio()
    stream=p.open(format=FOMART,
                  channels=CHANNLS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)
    frames=[]
    while True:
        for i in range(0,5):
            data=stream.read(CHUNK)
            frames.append(data)
        audio_data=np.frombuffer(data,dtype=np.short)
        temp=np.max(audio_data)
        if temp>th:
            print("delected a signal")
            print("current threshold:",temp)
            less=[]
            frames2=[]
            while True:
                print("recording")
                for i in range(0,30):
                    data2=stream.read(CHUNK)
                    frames2.append(data2)
                audio_data2= np.frombuffer(data2, dtype=np.short)
                temp2=np.max(audio_data2)
                if temp2<th:
                    less.append(-1)
                    print("below threshold,counting:",less)
                    if len(less)==waitime:
                        break
                else:
                    less=[]
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf=wave.open(WAVE_OUTPUT_FILENAME,'wb')
    wf.setnchannels(CHANNLS)
    wf.setframerate(RATE)
    wf.setsampwidth(p.get_sample_size(FOMART))
    wf.writeframes(b''.join(frames2))
    wf.close()


def BGM(th):
    CHUNK=512
    FOMART=pyaudio.paInt16
    CHANNLS=1
    RATE=16000
    p=pyaudio.PyAudio()
    stream=p.open(format=FOMART,
                  channels=CHANNLS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)
    frames=[]
    while True:
        for i in range(0,5):
            data=stream.read(CHUNK)
            frames.append(data)
        audio_data=np.frombuffer(data,dtype=np.short)
        temp=np.max(audio_data)
        if temp<th+300:
            print("delected a signal")
            print("current threshold:",temp)
            less=[]
            frames2=[]
            while True:
                print("recording")
                for i in range(0,30):
                    data2=stream.read(CHUNK)
                    frames2.append(data2)
                audio_data2= np.frombuffer(data2, dtype=np.short)
                temp2=np.max(audio_data2)
                if temp2>th+400:
                    less.append(1)
                    print("调用录音",less)
                    Monitor_MIC(300, path)
                    audioToWord(path+".wav")
                else:
                    less=[]
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
BGM(10)




