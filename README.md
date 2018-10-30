# speech_commmunication
### 项目说明：
在windows平台下，使用speech_recognition记录音频，并转换为16k的wav， 之后利用ffmpeg将wav转化为pcm文件，上传到百度语音端，返回语音信息，并利用pyttsx3添加了简单的交互功能。
#### 需求模块：
 speech_recognition， pyttsx3， pyaudio， wave， aip， ffmpeg
#### 模块安装：
* speech_recognition: [https://pypi.org/project/SpeechRecognition/](https://pypi.org/project/SpeechRecognition/)
* pyttsx3: [https://blog.csdn.net/dss_dssssd/article/details/82693742](https://blog.csdn.net/dss_dssssd/article/details/82693742)
* pyaudio: [https://pypi.org/project/PyAudio/](https://pypi.org/project/PyAudio/)
* aip:[https://ai.baidu.com/docs#/ASR-Online-Python-SDK/top](https://ai.baidu.com/docs#/ASR-Online-Python-SDK/top)
* ffmpeg (Windows下） **注意是系统的环境变量，不是个人的path**
[https://blog.csdn.net/zhuiqiuk/article/details/72834385](https://blog.csdn.net/zhuiqiuk/article/details/72834385)

### 关于pyttsx3模块的使用：
[https://blog.csdn.net/dss_dssssd/article/details/82693742](https://blog.csdn.net/dss_dssssd/article/details/82693742)
## 注意：
**pyttsx3的pyttsx3.engine()初始化不能放在线程中进行，会错。**

##### 说明：
* 如果返回timeout错误，在网络畅通的情况下，建议换一个id和key试一下。
