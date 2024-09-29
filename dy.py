import pprint

import requests
import re
import urllib
import json

myUrl = 'https://www.douyin.com/user/MS4wLjABAAAAjihywFMpCRLGaecNIcgnTt2N9o9-PthBT5GdQH9fVqA?modal_id=7369169950881090831&vid=7371773730701233460'
myHeaders = {
    'Cookie':'douyin.com; __ac_nonce=06656c46200155655968; __ac_signature=_02B4Z6wo00f019W-bQAAAIDAh0FNGxpdfPfVnmmAAJNCfF7zqH2QA-G05mvyvKiVVNgWSqTsFo-q1NZv30K4CAP.aYdDlbzsWokjsRYF6bt7j4IVynPJluEyWmAWmFPq.TZkRrApR-nxFGbNb5; ttwid=1%7CWJyhZbwISLUaGY0VE-Syuzvja_l9mZxim-i5n6yerdg%7C1716962402%7C93ae48de53cc566d5d2e6faae1c82bc2e2ff043fe8494b0f06d7dfa77a31cad5; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; dy_swidth=1440; dy_sheight=900; csrf_session_id=e85cb4a5e69989e657d718c305cbd630; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221716962404.492%22; xgplayer_user_id=188577184065; s_v_web_id=verify_lwrf32n8_XBkEORO8_CeBJ_4yBQ_BCIe_OwGnIFPZhlnW; passport_csrf_token=b3c9d3c856df43b3f6b4691ca9722678; passport_csrf_token_default=b3c9d3c856df43b3f6b4691ca9722678; bd_ticket_guard_client_web_domain=2; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; odin_tt=37b140a184cde01e83ae7d27587cf0e558294ec0a633d0d4c2bd1d40322ce4ec15e5aca3053990153c381c45057c9ed4b388cdb70b2a0703156436ba4cdcd42a7d91e306f3a4f52224e10723e08cebc8; download_guide=%221%2F20240529%2F0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; xg_device_score=7.575861645412042; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A900%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A200%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSWhFNWJ2UWxML0FENHJaUDgvVVBaNzBpTW9ncVRsWEUrWWlSd1ExajI0cTFXQ2YvNFZNU2V5SWkxdHVuaVRObnZWdzNFZXdtMzFuL0JnVWRTbHpvZDA9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; IsDouyinActive=false; msToken=oLFdDA1e9If8nHHaha4zGLv-FflJapTIZY23p0FGhGWHMSOnLUY9cT5XFCaqDWDtPClgd0cx9PNIUH3QF6Tmuf61A0D7hFEG2TLkJnGzbXuLxsK4KA==',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'

}

webHtml = requests.get(url=myUrl,headers=myHeaders).text


info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>',webHtml)[0]

info = urllib.parse.unquote(info)

info = json.loads(info)

videoTitle = info['app']['videoDetail']['desc']

videoAddr = 'https:'+info['app']['videoDetail']['video']['bitRateList'][0]['playAddr'][0]['src']

videoData = requests.get(url=videoAddr,headers=myHeaders).content

f = open(videoTitle+'.mp4','wb')

f.write(videoData)