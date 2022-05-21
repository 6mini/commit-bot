# -*- coding: utf-8 -*-
# 라이브러리
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime, timedelta
from pytz import timezone
import time
import re
import sys

# 슬랙 기능 라이브러리
from slack_sdk import WebClient
import json

# 리눅스 환경 라이브러리
from pyvirtualdisplay import Display

def main():
    # 슬랙 클라이언트 설정
    client = WebClient(token='')
    
    url = f'https://github.com/6mini' # 깃허브 프로필 url
     
    driver.get(url)
    
    for i in driver.find_elements(By.CSS_SELECTOR, 'rect'): # 커밋 기록
        if i.get_attribute('data-date') == today: # 오늘 날짜일 때:
            if i.get_attribute('data-level') == '0': # 커밋 수가 없다면 슬랙 알림
                message = [{
                                "type": "section",
                                "text": {
                                            "type": "mrkdwn",
                                            "text": "깃허브 커밋해라 !"
                                        }
                            }]
                client.chat_postMessage(channel='#에러', blocks=json.dumps(message))
                

if __name__ == '__main__':
    # 리눅스 디스플레이 설정
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    
    
    path = '/home/ubuntu/chromedriver' # 리눅스 드라이버 경로
    # path = '/Users/6mini/commit-bot/driver/mac/chromedriver' # 맥 드라이버 경로
    driver = webdriver.Chrome(path)
    
    today = datetime.now(timezone('Asia/Seoul')) # 오늘 날짜
    today = today.strftime('%Y-%m-%d') # 형식 변경
    
    main()
    
    driver.quit() # 드라이버 종료
    display.stop() # 디스플레이 종료