import requests
import json


# 定义函数，通过视频id号爬取视频文件
def getByID(videoID):
    myUrl = 'https://weibo.com/tv/api/component?page=%2Ftv%2Fshow%2F1034%3A'+ videoID

    # myHeader = {
    #     'Cookie':'XSRF-TOKEN=U0hjBuec-v72bL0mGLm0BB6x; SUB=_2A25LGwVODeRhGedH6lUR9SnIzTuIHXVoWRiGrDV8PUNbmtANLUetkW9NUMGw1xAIg0Z-LUHWTBvB8lKvD5fPuXsI; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhnYOB_ZuGcU5oHDda__dLW5NHD95Qp1K2Neh-NShqNWs4DqcjUi--4i-iWi-2cwJ.LxK-L1KeLBK-LxK-L1KeLBK-t; _s_tentry=weibo.com; Apache=1014227726020.1549.1712732193534; SINAGLOBAL=1014227726020.1549.1712732193534; ULV=1712732193578:1:1:1:1014227726020.1549.1712732193534:; WBPSESS=l9cDTIb35bXgJ_czrLQbvRjm5Fq-vki6Q3pdU3bqc5Yr0kuCD03m8x3qdCId1Iiy2PLRs4UZBVygSjFjmCs1vnSNOU0mUg-i1VSf9pq2AEx-wwOvg89F3B3TE_tyy8Nfgt4-9koY8fikdYEUAvVfOg==; ALF=02_1715929630; PC_TOKEN=67c6b2c00d',
    #     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0'
    # }
    myParams = {
        'data':'{"Component_Play_Playinfo":{"oid":"1034:'+videoID+'"}}'
    }

    webHtml = requests.get(url=myUrl,headers=myHeader,params=myParams).text
    # 直接访问，则提示{"code":"100001","msg":"miss param","data":{}}  param = parameter

    # print(webHtml)
    myDict = json.loads(webHtml)
    videoTitle = myDict['data']['Component_Play_Playinfo']['title']
    print(videoTitle)

    videoAddr = myDict['data']['Component_Play_Playinfo']['urls'].values()
    videoAddr = 'https:'+list(videoAddr)[0]

    print(videoAddr)

    # 获取到视频媒体地址后，通过get方法访问视频地址
    videoFile = requests.get(url=videoAddr).content

    f = open(videoTitle+'.mp4','wb')

    f.write(videoFile)

myUrl = 'https://weibo.com/tv/api/component'
myHeader = {
    'Cookie':'SINAGLOBAL=1014227726020.1549.1712732193534; ULV=1715154933907:3:1:1:4197345834521.5376.1715154933831:1713489268419; ALF=1717746933; SUB=_2A25LP1-lDeRhGedH6lUR9SnIzTuIHXVoNd1trDV8PUJbkNANLWzDkW1NUMGw1xjoW1nn6J7eWJTGWxHUJIhit4_p; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhnYOB_ZuGcU5oHDda__dLW5JpX5KMhUgL.Fo24eKM7SKMXSoM2dJLoIpXLxK.LB.2LBK9AICH8SC-4eEHWSCH8SC-4eEHWSBtt; _s_tentry=-; Apache=4197345834521.5376.1715154933831; XSRF-TOKEN=deCaCxPYmSX6G1ezUoI-tcxv; WBPSESS=l9cDTIb35bXgJ_czrLQbvRjm5Fq-vki6Q3pdU3bqc5bxtN0ebn6sAsNFKU60B-tRas9MZtz8x689-Iqedq7TUsvg2lCbKIAPEKUZbIY4IeccBMeEflmNveaNi9bOUrEV7BoClGnSKgAZqks-HWgkPw==',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0'
}
myParams = {
    'data':'{"Component_Home_Recommend":{}}'
}
myResonse = requests.get(url=myUrl,headers=myHeader,params=myParams).text

videoList = json.loads(myResonse)['data']['Component_Home_Recommend']['list']

for vl in videoList:
    id = vl['media_id']
    print(id)
    getByID(str(id))
