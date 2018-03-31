import pyaudio
import wave
'''
录音模块
'''
CHUNK = 1024
FORMAT = pyaudio.paInt16  #录音格式
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3    #录音时长
WAVE_OUTPUT_FILENAME = "output.wav" #保存的文件名
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
##打开一个音频输入流

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)  #从输入流中循环读取CHUNK大小的数据，然后存到列表当中
    frames.append(data)

print("* done recording")

stream.stop_stream()   #停止音频输入流
stream.close()      ##关闭
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb') #使用wave保存音频文件
print(p.get_sample_size(FORMAT))
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()