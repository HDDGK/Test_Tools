import pyaudio
import wave
'''
https://blog.csdn.net/zhjadsf/article/details/120799689
'''
record_seconds=10
pfomart=pyaudio.paInt16
channels=1
rate=16000

path=r"C:\Users\HK145\Desktop\新建文件夹\try.wav"
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