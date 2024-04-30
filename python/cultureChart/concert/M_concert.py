from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
# 웹 드라이버 설정
options = ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
url = "https://ticket.melon.com/ranking/index.htm"
# 웹 페이지에 접속
driver.get(url)
time.sleep(2)  # 페이지 로딩 대기

btn = driver.find_element(By.CLASS_NAME , "tit_rank_date")

btn.click()

time.sleep(2)

monthly_text = driver.find_element(By.CSS_SELECTOR , "li.nth3 h2.tit")

monthly_text.click()

time.sleep(3)

dateList = driver.find_element(By.CSS_SELECTOR , ".list_date li")

dateList.send_keys(Keys.ENTER)

print("click 2")

time.sleep(5)