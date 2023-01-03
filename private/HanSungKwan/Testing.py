import unittest
from attr import Attribute
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

path = './images/' # 이미지 저장 폴더
if not os.path.isdir(path): # 없으면 새로 생성
    os.mkdir(path)

keyword = input("검색어를 입력하세요\n>>")
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
last_height = 0
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
        except:
            break
    last_height = new_height
for image in images:
    driver.execute_script("arguments[0].click();", image)
    time.sleep(1)
    try :
        imgUrl = driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "images/" + str(count) + ".jpg")
        count += 1
    except :
        pass
print('End')
