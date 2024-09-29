import requests
import re
import json
import os

# myurl = 'https://haokan.baidu.com/v?vid=4784321160072774868&tab=recommend&sfrom=recommend'
myurl = 'https://haokan.baidu.com/v?vid=10136784148794229273&'

myheader = {
    'cookie':'BIDUPSID=3EE98F08025B6B74AE5B81F1D5001AC8; PSTM=1649936852; BAIDUID=3EE98F08025B6B74157E75857BA9F96A:FG=1; BAIDUID_BFESS=3EE98F08025B6B74157E75857BA9F96A:FG=1; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1650440248,1651712812; av1_switch_v3=0; PC_TAB_LOG=video_details_page; COMMON_LID=1edbd9a35d8015a0cbadec99d8f1248e; hkpcvideolandquery=13%u5C81%u4E00%u5E45%u753B%u62CD%u535690%u4E07%uFF0C2%u5C0F%u65F6%u82B1%u514910%u4E07%uFF0C%u674E%u5AE3%uFF1A%u6211%u4E0D%u9700%u8981%u4EC0%u4E48%u80FD%u529B; ab_sr=1.0.1_MmFmMmFkZGRkYjE1OTU4MTFhOGVkN2QxNGNmNjZjYjMyNDY4YmE2MTQ0Mjg0NjljNzc5M2Q5NTI1MTdlNTVmMTE1NmUzYTg4MWE5MjU5MDUzNjQwYzBjMDM4MzhlMjY5NGVjNDkwMjBjYWI4N2E2MGMyM2NmNzEzNDkyYmJjYTY2OTE2OTNjZGUyZmVkYjc4ODU2YmM2MGUxMTY4NWFkOQ==; reptileData=%7B%22data%22%3A%22b35d2919038cae80ba410cc02fe0ac012c5faabd95f406cf7788179d54c456570544cbc25d1c87ab821e9700643a01c9095cc1340496eafa3229231e2260b4f9fa303619223f8bc1f4af91cfd7c82c65067dc008499454a3daecb7bd5ba9ca11%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%221084e505%22%7D; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1651713827; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=qof81fijnj&ss=l2sb5ssi&sl=l&tt=4fw7&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=m4a9&ul=ra27"',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}

response = requests.get(url=myurl,headers=myheader)

# 获取当前网页返回的响应源代码
web_html = response.text

print(web_html)

mydata = re.findall('window.__PRELOADED_STATE__(.*?)document.querySelector',web_html)[0]

print(mydata)

# 找出包含视频地址的字典数据
# 以'window.__PRELOADED_STATE__'开头
# 以'document.querySelector('body').removeChild(document.querySelector('#_page_data'));'结尾

# 从网页源代码中找出以'curVideoMet'开头，并且以'callCurVideoRelate'结尾的内容
# 获取其中的第1条数据
# mydata = re.findall('playurl":"(.*?)","clarity',web_html)[0]

# 替换掉所有的转义字符'\'

# mydata = mydata.replace('\\','')
#
# # print(mydata)
#
# videodata = requests.get(url=mydata,headers=myheader).content
#
# f = open('movie.mp4','wb')
# f.write(videodata)

'''

# 把获取的数据加载成字典
mydict = json.loads(mydata)

# 获取标题
myTitle = mydict['title']

# 获取视频播放地址
videoAddr = mydict['playurl']

# print(videoAddr)

response = requests.get(url=videoAddr,headers = myheader)

videodata = response.content

f = open(myTitle+'.mp4','wb')

f.write(videodata)
'''