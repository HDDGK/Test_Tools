import time
import wave
import pyaudio
'''
https://blog.csdn.net/zhjadsf/article/details/120799689
'''
path = r"WWW.wav"
wf=wave.open(path, "rb")
wav_data=wf.readframes(wf.getnframes())
meta={"seek":0}

def callback(in_data,frame_count,time_info,status):
    start=meta["seek"]
    meta["seek"]+=frame_count*pyaudio.get_sample_size(pyaudio.paInt16)*wf.getnchannels()
    data=wav_data[start:meta["seek"]]
    return (data,pyaudio.paContinue)

audioGet=pyaudio.PyAudio()
stream = audioGet.open(format=audioGet.get_format_from_width(wf.getsampwidth()),  # paInt16指定数据类型
                       channels=wf.getnchannels(),
                       rate=wf.getframerate(),
                       output=True,
                       stream_callback=callback
                       )
stream.start_stream()
while stream.is_active():
    time.sleep(0.1)
stream.stop_stream()
stream.close()
wf.close()
audioGet.terminate()

def readAudio():
    audioGet = pyaudio.PyAudio()
    # wave.open 从wf文件读取信息

    with wave.open(path, "rb") as wf:
        stream = audioGet.open(format=pyaudio.paInt16,  # paInt16指定数据类型
                               channels=wf.getnchannels(),
                               rate=wf.getframerate(),
                               frames_per_buffer=1024,
                               output=True
                               )
        stream.write(wf.readframes(wf.getnframes()))
        stream.stop_stream()
        stream.close()
    audioGet.terminate()
