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
import pytesseract
from PIL import Image
from io import BytesIO
import pickle
import cv2
import time
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


# cookies = driver.get_cookies()

username_input = driver.find_element(By.ID, "loginName")
password_input = driver.find_element(By.ID, "password")
captcha_input = driver.find_element(By.ID, "validateCode")
login_button = driver.find_element(By.ID, "button")
captcha_element = driver.find_element(By.ID, 'kaptchaImage')


captcha_url = captcha_element.get_attribute('src')
# print(captcha_url)
urllib.request.urlretrieve(captcha_url, "captcha.png")
# with open('captcha.png', 'wb') as f:
#     f.write(response.content)


# captcha_image = Image.open("captcha.png")
# img_cv = cv2.imread("captcha.png")
# print(img_cv)
# img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
# print("123{}",pytesseract.image_to_string(img_rgb))
# # print(captcha_image)
# captcha_code = pytesseract.image_to_string("captcha.png")
# print(captcha_code)
# #
# captcha_image = Image.open("captcha.png")
# # 识别验证码
# captcha_code = pytesseract.image_to_string(captcha_image)
# print(captcha_code)
# captcha_input.send_keys(captcha_code)


# 使用OpenCV读取图片
# img = cv2.imread("captcha.png")
#
# # 将图片转换为灰度图像
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # 对图片进行二值化处理
# ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#
# # 使用高斯滤波去除噪点
# kernel = np.ones((3, 3), np.uint8)
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
#
# # 对图片进行识别
# captcha_code = pytesseract.image_to_string(Image.fromarray(opening))
# print(captcha_code)





video = WebDriverWait(driver, 260).until(
    EC.presence_of_element_located((By.ID, "resource-0-fb511ebe-170a-4257-bf61-41bf4330e80c_html5_api"))
)
# 播放视频
video.play()

# 等待视频播放完成
while True:
    if video.ended:
        break
    time.sleep(1)

# 关闭浏览器
# driver.quit()