import time
import json
import os

from django.conf import settings
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from .models import HeroMetaData
from django.core.exceptions import ObjectDoesNotExist
from selenium.common.exceptions import NoSuchElementException

def wait_for_page_load(driver):
    while True:
        ready_state = driver.execute_script("return document.readyState")
        if ready_state == "complete":
            return
        time.sleep(1)

# プライバシーポリシーが閉じれないため、一旦保留
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

    time.sleep(10)

    # ページの読み込みが完了するまで待機
    wait_for_page_load(driver)

    print(driver.page_source)

    print('------------------------------------------------------------')

    # プライバシーポリシーを閉じる
    privacy_policy_close_button = WebDriverWait(driver, WAIT_TIME).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class='mt-cb-policy-close']"))
    )
    driver.execute_script("arguments[0].click();", privacy_policy_close_button)

    print(driver.page_source)
    print('------------------------------------------------------------')

    # ページの読み込みが完了するまで待機
    wait_for_page_load(driver)

    time.sleep(10)

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


def create_mlbb_meta_data():

    DISPLAY_URL = "https://m.mobilelegends.com/en/rank"
    WAIT_TIME = 10

    # Heroku環境で実行する場合
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    # service = Service()  # Heroku環境で実行する場合
    service = Service(ChromeDriverManager().install())  # ローカル環境で実行する場合
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(WAIT_TIME)
    driver.get(DISPLAY_URL)

    # ページの読み込みが完了するまで待機
    wait_for_page_load(driver)

    # プライバシーポリシーを閉じる
    privacy_policy_close_button = WebDriverWait(driver, WAIT_TIME).until(
        # EC.element_to_be_clickable((By.XPATH, "//*[@id='mt-cb-policy']/div/div[2]"))
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".mt-cb-policy-close"))
    )
    privacy_policy_close_button.click()

    # time.sleep(5)

    # ページの読み込みが完了するまで待機
    wait_for_page_load(driver)

    print(driver.page_source)

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

    # ページの読み込みが完了するまで待機
    wait_for_page_load(driver)

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

    # JSONデータを作成
    json_data = {
        'reference_date': reference_date.strftime('%Y-%m-%d'),
        'rank_level': rank_level,
        'hero_meta_data': hero_meta_data
    }
    
    # 参照日をファイル名に使用
    dynamic_file_name = f"mlbb_meta_data_{reference_date.strftime('%Y%m%d')}.json"
    latest_file_name = "latest_hero_meta_data.json"

    # staticフォルダのパスを取得
    static_dir = settings.STATICFILES_DIRS[0]

    # 動的なファイル名での保存先パスを作成
    dynamic_file_path = os.path.join(static_dir, dynamic_file_name)

    # 最新のメタデータファイル名での保存先パスを作成
    latest_file_path = os.path.join(static_dir, latest_file_name)

    # 動的なファイル名でJSONファイルに保存
    with open(dynamic_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    # 最新のメタデータファイル名でJSONファイルに保存
    with open(latest_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    driver.quit()

def save_latest_meta_data_to_db():
    # 最新のメタデータファイル名でのパスを作成
    latest_file_path = os.path.join(settings.STATICFILES_DIRS[0], 'latest_hero_meta_data.json')

    # JSONファイルからデータを読み込む
    with open(latest_file_path, 'r') as json_file:
        data = json.load(json_file)

    # データをHeroMetaDataモデルに保存
    reference_date = data['reference_date']
    rank_level = data['rank_level']
    hero_meta_data = data['hero_meta_data']

    updated_count = 0
    created_count = 0

    for hero_name, hero_data in hero_meta_data.items():
        defaults = {
            'win_rate': hero_data['win_rate'],
            'pick_rate': hero_data['pick_rate'],
            'ban_rate': hero_data['ban_rate'],
        }

        try:
            hero_meta_data_obj = HeroMetaData.objects.get(
                name=hero_name,
                rank_level=rank_level,
                reference_date=reference_date
            )
            for key, value in defaults.items():
                setattr(hero_meta_data_obj, key, value)
            hero_meta_data_obj.save()
            updated_count += 1
        except ObjectDoesNotExist:
            HeroMetaData.objects.create(
                name=hero_name,
                rank_level=rank_level,
                reference_date=reference_date,
                **defaults
            )
            created_count += 1

    print(f"Updated: {updated_count} records")
    print(f"Created: {created_count} records")