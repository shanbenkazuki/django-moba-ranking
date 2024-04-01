import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from .models import HeroMetaData

def wait_for_page_load(driver):
    while True:
        ready_state = driver.execute_script("return document.readyState")
        if ready_state == "complete":
            return
        time.sleep(1)


def scrape_mlbb_meta_data():
    DISPLAY_URL = "https://m.mobilelegends.com/en/rank"
    WAIT_TIME = 50

    # ローカル環境で実行する場合
    # chrome_options = Options()
    # chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    # service = Service(ChromeDriverManager().install())

    # Heroku環境で実行する場合
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    service = Service()  # Heroku環境で実行する場合
    # service = Service(ChromeDriverManager().install())  # ローカル環境で実行する場合
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(WAIT_TIME)
    driver.get(DISPLAY_URL)

    time.sleep(3)

    # ページの読み込みが完了するまで待機
    wait_for_page_load(driver)

    print(driver.page_source)

    print('------------------------------------------------------------')

    # プライバシーポリシーを閉じる
    privacy_policy_close_button = WebDriverWait(driver, WAIT_TIME).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='mt-cb-policy-close']"))
    )
    driver.execute_script("arguments[0].click();", privacy_policy_close_button)
    # ページの読み込みが完了するまで待機
    wait_for_page_load(driver)

    print(driver.page_source)
    print('------------------------------------------------------------')

    # Mythic+のタブに切り替える
    mythic_plus_tab = WebDriverWait(driver, WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='rank']/div[1]/div[2]/ul/li[2]"))
    )
    mythic_plus_tab.click()

    rank_level = 'Mythic+'

    # 要素が表示されるまで待機
    hero_elements = WebDriverWait(driver, WAIT_TIME).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".slotwrapper > ul > li > a"))
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