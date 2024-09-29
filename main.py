import requests
import re
import json
import subprocess
import os

# 该程序需要第三方库，ffmpeg，官网地址：https://www.ffmpeg.org

bvid = input("输入BV号：")

myurl = f'https://www.bilibili.com/video/{bvid}/'

myHeader = {
        'cookie':'buvid3=416196A5-8FBA-4178-F6A9-99FCEA7B047293112infoc; b_nut=1683282593; i-wanna-go-back=-1; b_ut=7; _uuid=34AB8462-104EC-CAF3-9FF7-7FD7DB23352591502infoc; FEED_LIVE_VERSION=V8; home_feed_column=4; CURRENT_FNVAL=4048; CURRENT_PID=ce9bca20-eb2f-11ed-92a8-b5fbdf930b3a; rpdid=|(ku|u~YklkR0J\'uY)Jk)kYul; fingerprint=85274705acc4f4610fc9c0ffe5934861; buvid_fp_plain=undefined; b_lsid=253CE3BA_188234D6D50; header_theme_version=CLOSE; browser_resolution=1280-721; innersign=1; buvid_fp=c6b16956b2a8e67be1b4411447e6d010; sid=pc0fjx05; buvid4=351EA4E1-25BC-874C-A9F3-2421714F9CF795944-023050518-DibbRiH2DBLPgEik4fUbkw%3D%3D',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}

# 获取视频详情页面html代码
webHtml = requests.get(url=myurl,headers=myHeader).text

# 获取视频标题
videoTittle = re.findall('<title data-vue-meta="true">(.*?)_哔哩哔哩_bilibili</title>',webHtml)[0]

# 获取中间一段json
jsonData = re.findall('window.__playinfo__=(.*?)</script>',webHtml)[0]

# 解析成字典
jsonData = json.loads(jsonData)

# 分别获取音频和视频文件地址
audioAddr = jsonData['data']['dash']['audio'][0]['baseUrl']
videoAddr = jsonData['data']['dash']['video'][0]['baseUrl']

print(videoAddr,audioAddr)

# 发现直接get返回403forbidden，需要在header中加两个数据
myHeader.update({'origin': 'https://www.bilibili.com'})
myHeader.update({'referer': myurl})

# 获取音视频二进制数据
videoFile = requests.get(url=videoAddr,headers=myHeader)
audioFile = requests.get(url=audioAddr,headers=myHeader)

# 写入音视频二进制文件
with open(videoTittle+'.mp4','wb') as f:
        f.write(videoFile.content)
with open(videoTittle+'.mp3','wb') as f:
        f.write(audioFile.content)



# 调用第三方库，完成音视频合成
# subprocess.call(("/Users/veckydeng/Documents/ffmpeg -i " + videoTittle+'.mp4' + " -i " + videoTittle+'.mp3' +
#                  " -c copy " + videoTittle+'final.mp4').encode(
#                 "utf-8").decode("utf-8"), shell=True)

# os.remove(videoTittle+'.mp4')
# os.remove(videoTittle+'.mp3')
