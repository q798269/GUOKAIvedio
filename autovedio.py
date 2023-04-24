import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time
from time import sleep
import re
import urllib.request
# 启动 Chrome 浏览器
# service = Service('path/to/chromedriver')
# service.start()
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome()

# 加载视频页面
driver.get('https://iam.pt.ouchn.cn/am/UI/Login?realm=%2F&service=initService&goto=https%3A%2F%2Fiam.pt.ouchn.cn%2Fam%2Foauth2%2Fauthorize%3Fservice%3DinitService%26response_type%3Dcode%26client_id%3D345fcbaf076a4f8a%26scope%3Dall%26redirect_uri%3Dhttps%253A%252F%252Fmenhu.pt.ouchn.cn%252Fouchnapp%252Fwap%252Flogin%252Findex%26decision%3DAllow')



sleep(60)
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[0])
# with open('page.html', 'w', encoding='utf-8') as f:
#     f.write(driver.page_source)

# password_input = driver.find_element(By.ID, "password")
# 找到 video 元素
# video_element = driver.find_element(By.XPATH, '//video[@class="vjs-tech"]'
# video_element = driver.find_element(By.XPATH, '//video[contains(@id, "resource-0-") and contains(@id, "_html5_api") and contains(@src, "/api/uploads/video/")]')
#
#
# # 获取 id 属性值
# video_id = video_element.get_attribute('id')
#
# # 使用正则表达式匹配 id 属性值
# match = re.search(r'resource-\d+-[\w-]+', video_id)
# if match:
#     # 获取匹配结果
#     video_id = match.group()
# else:
#     print('No match found')
#
# # 打印匹配结果
# print('Video ID:', video_id)
#
#
# video = WebDriverWait(driver, 260).until(
#     EC.presence_of_element_located((By.ID, video_id))
# )
#
# button_element = driver.find_element(By.CSS_SELECTOR, 'button.mvp-toggle-play')
# button_element.click()
# #   <div class="show-advanced ng-scope" ng-if="!uiShowDetail">
# #             <span>显示基本信息</span>
# #             <i class="font font-down-arrow"></i>
# #         </div>
# element_basicInfo = driver.find_element(By.XPATH, '//a[@ng-click="toggleActivityInfo()"]')
# element_basicInfo.click()
#
# # <a class="next ng-binding ng-scope" ng-click="changeActivity(next)" ng-if="next">下一个: 1.4 组织层数据模型</a>
# next_button = driver.find_element_by_xpath('//a[@class="next ng-binding ng-scope"]')
#
# time_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//span[@class="attribute-value ng-binding" and contains(@ng-bind, "ui.duration")]'))
# )
#
# # 提取时间
# time_text = time_element.text
# duration = re.findall(r'\d+:\d+:\d+', time_text)[0]
#
# print(int(duration.split(':')[0])*3600 + int(duration.split(':')[1])*60 + int(duration.split(':')[2]) + 5)
# # 程序sleep时间
# time.sleep(int(duration.split(':')[0])*3600 + int(duration.split(':')[1])*60 + int(duration.split(':')[2]) + 5)
# next_button.click()
# sleep(10)


while True:
    try:
        video_element = driver.find_element(By.XPATH, '//video[contains(@id, "resource-0-") and contains(@id, "_html5_api") and contains(@src, "/api/uploads/video/")]')

        # 获取 id 属性值
        video_id = video_element.get_attribute('id')

        # 使用正则表达式匹配 id 属性值
        match = re.search(r'resource-\d+-[\w-]+', video_id)
        if match:
            # 获取匹配结果
            video_id = match.group()
        else:
            print('No match found')

        # 打印匹配结果
        print('Video ID:', video_id)

        video = WebDriverWait(driver, 260).until(
            EC.presence_of_element_located((By.ID, video_id))
        )

        button_element = driver.find_element(By.CSS_SELECTOR, 'button.mvp-toggle-play')
        button_element.click()
        #   <div class="show-advanced ng-scope" ng-if="!uiShowDetail">
        #             <span>显示基本信息</span>
        #             <i class="font font-down-arrow"></i>
        #         </div>
        element_basicInfo = driver.find_element(By.XPATH, '//a[@ng-click="toggleActivityInfo()"]')
        element_basicInfo.click()

        #<div data-v-65ba481a="" class="mvp-play-rate">
    #   2.0X
    # </div>
    #     element_x2 = driver.find_element(By.CSS_SELECTOR, 'div.mvp-play-rate')
    #     element_x2.click()
        # <a class="next ng-binding ng-scope" ng-click="changeActivity(next)" ng-if="next">下一个: 1.4 组织层数据模型</a>
        next_button = driver.find_element(By.XPATH, '//a[@class="next ng-binding ng-scope"]')

        time_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[@class="attribute-value ng-binding" and contains(@ng-bind, "ui.duration")]'))
        )

        # 提取时间
        time_text = time_element.text
        duration = re.findall(r'\d+:\d+:\d+', time_text)[0]

        print(int(duration.split(':')[0]) * 3600 + int(duration.split(':')[1]) * 60 + int(duration.split(':')[2]) + 5)
        # 程序sleep时间
        time.sleep(
            int(duration.split(':')[0]) * 3600 + int(duration.split(':')[1]) * 60 + int(duration.split(':')[2]) + 5)
        next_button.click()
        sleep(10)
    except:
        next_button = driver.find_element(By.XPATH, '//a[@class="next ng-binding ng-scope"]')
        next_button.click()
        sleep(10)

# 等待视频播放完成





# 关闭浏览器
# driver.quit()