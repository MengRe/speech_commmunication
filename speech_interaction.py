import speech_recognition as sr
import pyttsx3
import pyaudio
import wave
from aip import AipSpeech
import os

def read_wav():
    CHUNK = 1024
# 测试语音
    wf = wave.open('./2.wav', 'rb')
        # read data
    data = wf.readframes(CHUNK)
    p = pyaudio.PyAudio()
    FORMAT = p.get_format_from_width(wf.getsampwidth())
    CHANNELS = wf.getnchannels()
    RATE = wf.getframerate()

    print('FORMAT: {} \nCHANNELS: {} \nRATE: {}'.format(FORMAT, CHANNELS, RATE))
    stream = p.open(format=FORMAT,

                    channels=CHANNELS,
                    rate=RATE,
                    frames_per_buffer=CHUNK,
                    output=True)
    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)




def wav_to_pcm(wav_file):
    # 假设 wav_file = "音频文件.wav"
    # wav_file.split(".") 得到["音频文件","wav"] 拿出第一个结果"音频文件"  与 ".pcm" 拼接 等到结果 "音频文件.pcm"
    pcm_file = "%s.pcm" %(wav_file.split(".")[0])
    # 就是此前我们在cmd窗口中输入命令,这里面就是在让Python帮我们在cmd中执行命令
    os.system("ffmpeg -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s"%(wav_file,pcm_file))

    return pcm_file

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


""" 你的 APPID AK SK """
APP_ID = '14434207'
API_KEY = 'B1bP3bX8Y0pRG9RVQ0FTxIgN'
SECRET_KEY = '9L779T18OMqRQSAUklccdAzaTb5GtcoF'

def speech_interaction():
    # 初始化pyttsx3 engine
    engine = pyttsx3.init()

    # obtain audio from the microphone
    # 从麦克风记录数据
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Say something!")
        engine.say("门外有客人来访，需要开门吗, 请一秒后回答？")
        engine.runAndWait()
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    engine.say("录音结束, 识别中")
    engine.runAndWait()
    read_wav()
    # 将数据保存到wav文件中
    with open("2.wav", "wb") as f: 
        f.write(audio.get_wav_data(convert_rate=16000))


        
    # 创建百度语音识别客户端
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 转成pcm格式
    pcmFile = wav_to_pcm("./2.wav")
    result = client.asr(get_file_content(pcmFile), 'pcm', 16000, {
        'dev_pid': 1537,
    })
    print(result)
    # print(result['err_msg'], result['result'][0])

    # 上传到百度云识别
    try:
        success = True if result['err_msg'] == 'success.' else False
        print(success)
        if success:
            text = result['result'][0]
            if "不" in text :
                engine.say("好的，那请您自己去开门")
                engine.runAndWait()
            elif "开" in text or '好' in text:
                engine.say("请您稍等，我去帮您开门，")
                engine.runAndWait()
            else:
                engine.say("语音识别错误")
                engine.runAndWait()
            # engine.say(text)
            # engine.runAndWait()
    except Exception as e:
        engine.say("抱歉， 识别错误")
        engine.runAndWait()

speech_interaction()
