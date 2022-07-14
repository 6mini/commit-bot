# -*- coding: utf-8 -*-
# 라이브러리
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from pytz import timezone

# 슬랙 기능 라이브러리
from slack_sdk import WebClient
import json



def main():
    today = datetime.now(timezone('Asia/Seoul')) # 오늘 날짜
    today = today.strftime('%Y-%m-%d') # 형식 변경
    
    # 슬랙 클라이언트 설정
    client = WebClient(token='')
    
    url = f'https://github.com/6mini' # 깃허브 프로필 url
    
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    
    for i in soup.select("rect"):
        if i["data-date"] == today:
            if i["data-level"] == '1': # 커밋 수가 없다면 슬랙 알림
                message = [{
                                "type": "section",
                                "text": {
                                            "type": "mrkdwn",
                                            "text": "깃허브 커밋해라 !"
                                        }
                            }]
                client.chat_postMessage(channel='', blocks=json.dumps(message))
            break            

if __name__ == '__main__':
    main()