from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"chart_Y_concert10_{current_date}.json"

# 웹드라이버 설정
options = ChromeOptions()
# options.add_argument("window-size=1920x1080")
# options.add_argument("disable-gpu")
# options.add_argument("lang=ko_KR")
# options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
options.add_argument("--no-header")
# service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(options=options)

browser.get("http://ticket.yes24.com/Rank/All")


time.sleep(5)

# rank-division 클래스를 가진 div 요소를 찾기
# search_box = browser.find_element(By.CLASS_NAME, "rank-division")

# # div 내에서 모든 a 태그 요소를 찾기
# a_tags = search_box.find_elements(By.TAG_NAME, "a")

# # 두 번째 a 태그의 소스를 가져오기
# second_a_tag = a_tags[1]
# second_a_tag.click()

# # 월간 카테고리 선택
# monthly_category = browser.find_element(By.XPATH, '//a[@categoryid="3"]')
# monthly_category.click()

# # 대기
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'rank-division')))

# time.sleep(10)

# bestTicket = browser.find_elements(By.CLASS_NAME , "rank-best")

# spanList = bestTicket[0].find_elements(By.TAG_NAME , "span")

# rank = spanList[0].text

# print(rank)






# 새로운 페이지 소스 가져오기
# page_source = browser.page_source



# BeautifulSoup을 사용하여 페이지 소스 파싱
# soup = BeautifulSoup(page_source, 'html.parser')

# # 원하는 데이터 추출 및 처리
# concert_list = []
# rank_best_div = soup.find('div', class_='rank-best')
# if rank_best_div:
#     concerts = rank_best_div.find_all('div')[:10]  # 상위 10개의 div 요소만 선택
#     for concert in concerts:
#         title = concert.find('p', class_='rlb-tit').get_text(strip=True)
#         place = concert.find('p', class_='rlb-sub-tit').get_text(strip=True)
#         rank = concert.find('p', class_='rank-best-number').find('span', class_='rank-best-number-new').get_text(strip=True)
#         concert_data = {
#         "rank": rank,
#         "title": title,
#         "place": place
#         }
#         concert_list.append(concert_data)

# # 브라우저 닫기
# browser.quit()

# JSON 파일로 저장
# with open(filename, 'w', encoding='utf-8') as file:
#     json.dump(concert_list, file, ensure_ascii=False, indent=4)