import pyaudio
import wave
import numpy as np
'''
https://blog.csdn.net/qq_21288703/article/details/108010701?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-108010701-blog-120799689.235%5Ev38%5Epc_relevant_sort_base1&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-108010701-blog-120799689.235%5Ev38%5Epc_relevant_sort_base1&utm_relevant_index=1
'''
path=r"C:\Users\HK145\Desktop\新建文件夹\try2"

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
                    if len(less)==5:
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
Monitor_MIC(300,path)

'''
    record_seconds=10
    pfomart=pyaudio.paInt16
    channels=1
    rate=16000

    path=r"C:\\Users\HK145\Desktop\新建文件夹\\try.wav"
    audio=pyaudio.PyAudio()
    stream=audio.open(format=pfomart,
                      channels=channels,
                      rate=rate,
                      input=True)
    wav_data =stream.read(int(rate * record_seconds))
    with wave.open(path,"wb")as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(pyaudio.get_sample_size(pfomart))
        wf.setframerate(rate)
        wf.writeframes(wav_data)
    stream.stop_stream()
    stream.close()
    audio.terminate()
'''
