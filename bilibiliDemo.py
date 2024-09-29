import requests
import re
import json
import subprocess
import os

# 爬取bilibili视频
myUrl = 'https://www.bilibili.com/video/BV14j411e7jT/?vd_source=16ab63714a9bd7bed91b48e73aa05e7d'

myHeaders = {
    'Cookie':'buvid3=422BE924-C43E-AEAD-3B48-66B347C6E49503249infoc; b_nut=1715759603; CURRENT_FNVAL=4048; b_lsid=101A76D14_18F7B3DE35A; _uuid=C4289472-D9A9-5356-F728-9D69F39337F804577infoc; sid=fvzczqeg; buvid_fp=d3f4ce7f0b8a767b6c5583726bbe702e; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTYwMTg4MDUsImlhdCI6MTcxNTc1OTU0NSwicGx0IjotMX0.AgL0XU--FbmIYF0t12NiI_wUJTEsj3rY2eBEoox3P_8; bili_ticket_expires=1716018745; buvid4=0F9F6856-50ED-1A43-0D80-1CFDACDD19D105394-024051507-uHQN9xk3PZKykxqPSrBOuA%3D%3D; rpdid=|(k|JJumY|lR0J\'u~ul~lmY|Y; PVID=1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

webHtml = requests.get(url=myUrl,headers=myHeaders).text

# 指定匹配规则
myRule = '<title data-vue-meta="true">(.*?)_哔哩哔哩_bilibili</title>'

videoTitle = re.findall(myRule,webHtml)[0]

print(videoTitle)

myRule = 'window.__playinfo__=(.*?)</script>'
fileAddr = re.findall(myRule,webHtml)[0]
fileAddr = json.loads(fileAddr)
videoAddr = fileAddr['data']['dash']['video'][0]['baseUrl']
print(videoAddr)
audioAddr = fileAddr['data']['dash']['audio'][0]['baseUrl']


# 在header字典中需要添加一些数据
myHeaders['Origin'] = 'https://www.bilibili.com'
myHeaders['Referer'] = 'https://www.bilibili.com/video/BV1gH4y1P7KH/'

videoData = requests.get(url=videoAddr,headers=myHeaders).content
audioData = requests.get(url=audioAddr,headers=myHeaders).content

videoFile = open(videoTitle+'.mp4','wb')
videoFile.write(videoData)

audioFile = open(videoTitle+'.mp3','wb')
audioFile.write(audioData)

subprocess.call(('/Users/veckydeng/ffmpeg -i ' + videoTitle +'.mp4 -i '
                 +videoTitle+'.mp3 -c copy '+ videoTitle + '_final.mp4')
                .encode('utf-8').decode('utf-8'),shell=True)

os.remove(videoTitle+'.mp4')
os.remove(videoTitle+'.mp3')