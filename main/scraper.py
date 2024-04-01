import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from .models import HeroMetaData


def scrape_mlbb_meta_data():
    DISPLAY_URL = "https://m.mobilelegends.com/en/rank"
    WAIT_TIME = 10

    # chrome_options = Options()
    # chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(WAIT_TIME)
    driver.get(DISPLAY_URL)

    time.sleep(3)

    # プライバシーポリシーを閉じる
    WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mt-cb-policy']/div/div[2]"))).click()

    # Mythic+のタブに切り替える
    WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='rank']/div[1]/div[2]/ul/li[2]"))).click()
    rank_level = 'Mythic+'

    WebDriverWait(driver, WAIT_TIME).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".slotwrapper > ul > li > a"))
    )

    time.sleep(2)

    # 勝率、使用率、バン率をhero_meta_dataに格納
    rateList = BeautifulSoup(driver.page_source, 'html.parser').select(".slotwrapper > ul > li > a")
    hero_meta_data = {}
    for heroRate in rateList:
        heroEn = heroRate.span.string

        winRatePoint = heroRate.contents[2].string.split("%")[0]
        popRatePoint = heroRate.contents[4].string.split("%")[0]
        banRatePoint = heroRate.contents[6].string.split("%")[0]
        hero_meta_data[heroEn] = {
            'win_rate': winRatePoint,
            'pick_rate': popRatePoint,
            'ban_rate': banRatePoint
        }
    
    # 参照日を取得
    reference_date = BeautifulSoup(driver.page_source, 'html.parser').select_one("#rank > div.header > div:nth-child(1) > ul > li").text

    # 参照日をdatetimeオブジェクトに変換
    reference_date = datetime.strptime(reference_date, '%Y-%m-%d').date()

    # データをデータベースに保存
    for hero_name, hero_data in hero_meta_data.items():
        mlbb_meta_data = HeroMetaData(
            name=hero_name,
            win_rate=hero_data['win_rate'],
            pick_rate=hero_data['pick_rate'],
            ban_rate=hero_data['ban_rate'],
            reference_date=reference_date,
            rank_level=rank_level
        )
        mlbb_meta_data.save()
    
    driver.quit()