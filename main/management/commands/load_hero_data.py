from django.core.management.base import BaseCommand
from main.models import Hero

class Command(BaseCommand):
    help = 'Loads hero data into the database'

    def handle(self, *args, **options):
        # heroデータをJSONまたはYAMLファイルから読み込む
        hero_data = [
                        {
                            "name_jp": "ロイン",
                            "name_en": "Lolita",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Lolita.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/lolita"
                        },
                        {
                            "name_jp": "フォヴィウス",
                            "name_en": "Phoveus",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Phoveus.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/phoveus"
                        },
                        {
                            "name_jp": "ウラノス",
                            "name_en": "Uranus",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Uranus.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/uranus"
                        },
                        {
                            "name_jp": "アウルス",
                            "name_en": "Aulus",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Aulus.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/aulus"
                        },
                        {
                            "name_jp": "セシリオン",
                            "name_en": "Cecilion",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Cecilion.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/cecilion"
                        },
                        {
                            "name_jp": "イヴ",
                            "name_en": "Yve",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Yve.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/yve"
                        },
                        {
                            "name_jp": "バレンティナ",
                            "name_en": "Valentina",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Valentina.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/valentina"
                        },
                        {
                            "name_jp": "クリント",
                            "name_en": "Clint",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Clint.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/clint"
                        },
                        {
                            "name_jp": "ディガー",
                            "name_en": "Diggie",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Diggie.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/diggie"
                        },
                        {
                            "name_jp": "アルドス",
                            "name_en": "Aldous",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Aldous.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/aldous"
                        },
                        {
                            "name_jp": "エスメラルダ",
                            "name_en": "Esmeralda",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Esmeralda.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/esmeralda"
                        },
                        {
                            "name_jp": "ジミー",
                            "name_en": "Kimmy",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Kimmy.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/kimmy"
                        },
                        {
                            "name_jp": "グルー",
                            "name_en": "Gloo",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Gloo.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/gloo"
                        },
                        {
                            "name_jp": "ボボル&クバ",
                            "name_en": "Popol and Kupa",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Popol-and-Kupa.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/popol"
                        },
                        {
                            "name_jp": "リリア",
                            "name_en": "Lylia",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Lylia.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/lylia"
                        },
                        {
                            "name_jp": "マチルダ",
                            "name_en": "Mathilda",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Mathilda.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/mathilda"
                        },
                        {
                            "name_jp": "フレイヤ",
                            "name_en": "Freya",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Freya.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/freya"
                        },
                        {
                            "name_jp": "マーシャ",
                            "name_en": "Masha",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Masha.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/masha"
                        },
                        {
                            "name_jp": "エレシル",
                            "name_en": "Irithel",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Irithel.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/irithel"
                        },
                        {
                            "name_jp": "ジェイソン",
                            "name_en": "Johnson",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Johnson.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/jhonson"
                        },
                        {
                            "name_jp": "カチャ",
                            "name_en": "Kaja",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Kaja.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/kaja"
                        },
                        {
                            "name_jp": "ランスロット",
                            "name_en": "Lancelot",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Lancelot.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/lancelot"
                        },
                        {
                            "name_jp": "悟空",
                            "name_en": "Sun",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Sun.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/sun"
                        },
                        {
                            "name_jp": "クッフラー",
                            "name_en": "Khufra",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Khufra.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/khufra"
                        },
                        {
                            "name_jp": "カーミラ",
                            "name_en": "Carmilla",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Carmilla.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/carmilla"
                        },
                        {
                            "name_jp": "イスンシン",
                            "name_en": "Yi Sun-shin",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Yi-Sun-shin.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/yi-sun-shin"
                        },
                        {
                            "name_jp": "ベイン",
                            "name_en": "Bane",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Bane.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/bane"
                        },
                        {
                            "name_jp": "アルゴス",
                            "name_en": "Argus",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Argus.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/argus"
                        },
                        {
                            "name_jp": "マイヤ",
                            "name_en": "Miya",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Miya.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/miya"
                        },
                        {
                            "name_jp": "クラウド",
                            "name_en": "Claude",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Claude.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/claude"
                        },
                        {
                            "name_jp": "ファニー",
                            "name_en": "Fanny",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Fanny.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/fanny"
                        },
                        {
                            "name_jp": "モスコブ",
                            "name_en": "Moskov",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Moskov.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/moskov"
                        },
                        {
                            "name_jp": "ラファエル",
                            "name_en": "Rafaela",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Rafaela.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/rafaela"
                        },
                        {
                            "name_jp": "カティタ",
                            "name_en": "Kadita",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Kadita.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/kadita"
                        },
                        {
                            "name_jp": "カレード",
                            "name_en": "Khaleed",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Khaleed.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/khaleed"
                        },
                        {
                            "name_jp": "ハカート",
                            "name_en": "Helcurt",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Helcurt.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/helcurt"
                        },
                        {
                            "name_jp": "ヘラクレス",
                            "name_en": "Hylos",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Hylos.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/hylos"
                        },
                        {
                            "name_jp": "ゾン",
                            "name_en": "Yu Zhong",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Yu-Zhong.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/yu-zhong"
                        },
                        {
                            "name_jp": "アリス",
                            "name_en": "Alice",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Alice.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/alice"
                        },
                        {
                            "name_jp": "オデット",
                            "name_en": "Odette",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Odetto.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/odette"
                        },
                        {
                            "name_jp": "ビアトリクス",
                            "name_en": "Beatrix",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Beatrix.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/beatrix"
                        },
                        {
                            "name_jp": "ルビー",
                            "name_en": "Ruby",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Ruby.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/ruby"
                        },
                        {
                            "name_jp": "サイクロプス",
                            "name_en": "Cyclops",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Cyclops.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/cyclops"
                        },
                        {
                            "name_jp": "カグラ",
                            "name_en": "Kagura",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Kagura.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/kagura"
                        },
                        {
                            "name_jp": "ヴェル",
                            "name_en": "Vale",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Vale.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/vale"
                        },
                        {
                            "name_jp": "ブルーノ",
                            "name_en": "Bruno",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Bruno.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/bruno"
                        },
                        {
                            "name_jp": "琥珀",
                            "name_en": "Wanwan",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Wanwan.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/wanwan"
                        },
                        {
                            "name_jp": "ゴセン",
                            "name_en": "Gusion",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Gusion.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/gusion"
                        },
                        {
                            "name_jp": "バラッツ",
                            "name_en": "Barats",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Barats.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/barats"
                        },
                        {
                            "name_jp": "星夢",
                            "name_en": "Lunox",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Lunox.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/lunox"
                        },
                        {
                            "name_jp": "ロジャー",
                            "name_en": "Roger",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Roger.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/roger"
                        },
                        {
                            "name_jp": "エウドラ",
                            "name_en": "Eudora",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Eudora.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/eudora"
                        },
                        {
                            "name_jp": "ローイ",
                            "name_en": "Luo Yi",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Luo-Yi.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/luo-yi"
                        },
                        {
                            "name_jp": "フローラ",
                            "name_en": "Floryn",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Floryn.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/floryn"
                        },
                        {
                            "name_jp": "グレンジャー",
                            "name_en": "Granger",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Granger.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/granger"
                        },
                        {
                            "name_jp": "玄覇",
                            "name_en": "Baxia",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Baxia.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/baxia"
                        },
                        {
                            "name_jp": "半蔵",
                            "name_en": "Hanzo",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Hanzo.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/hanzo"
                        },
                        {
                            "name_jp": "寅",
                            "name_en": "Yin",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Yin.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/yin"
                        },
                        {
                            "name_jp": "セリナ",
                            "name_en": "Selena",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Selena.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/selena"
                        },
                        {
                            "name_jp": "子龍",
                            "name_en": "Zilong",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Zilong.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/zilong"
                        },
                        {
                            "name_jp": "オーロラ",
                            "name_en": "Aurora",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Aurora.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/aurora"
                        },
                        {
                            "name_jp": "嫦娥",
                            "name_en": "Chang'e",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Change.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/change"
                        },
                        {
                            "name_jp": "フランコ",
                            "name_en": "Franco",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Franco.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/franco"
                        },
                        {
                            "name_jp": "ブロディ",
                            "name_en": "Brody",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Brody.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/brody"
                        },
                        {
                            "name_jp": "ナタリア",
                            "name_en": "Natalia",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Natalia.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/natalia"
                        },
                        {
                            "name_jp": "隼",
                            "name_en": "Hayabusa",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Hayabusa.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/hayabusa"
                        },
                        {
                            "name_jp": "アテラス",
                            "name_en": "Atlas",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Atlas.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/atlas"
                        },
                        {
                            "name_jp": "リン",
                            "name_en": "Ling",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Ling.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/ling"
                        },
                        {
                            "name_jp": "ファーサ",
                            "name_en": "Pharsa",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Pharsa.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/pharsa"
                        },
                        {
                            "name_jp": "ディアス",
                            "name_en": "Dyrroth",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Dyrroth.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/dyrus"
                        },
                        {
                            "name_jp": "ベレリック",
                            "name_en": "Belerick",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Belerick.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/belerick"
                        },
                        {
                            "name_jp": "ミノタウル",
                            "name_en": "Minotaur",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Minotaur.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/minotaur"
                        },
                        {
                            "name_jp": "シルバンナ",
                            "name_en": "Silvanna",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Silvanna.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/silvanna"
                        },
                        {
                            "name_jp": "メリッサ",
                            "name_en": "Melissa",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Melissa.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/melissa"
                        },
                        {
                            "name_jp": "メタルヘッド",
                            "name_en": "Jawhead",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Jawhead.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/jawhead"
                        },
                        {
                            "name_jp": "ガイ",
                            "name_en": "Akai",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Akai.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/akai"
                        },
                        {
                            "name_jp": "イーディス",
                            "name_en": "Edith",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Edith.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/edith"
                        },
                        {
                            "name_jp": "アンジェラ",
                            "name_en": "Angela",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Angela.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/angela"
                        },
                        {
                            "name_jp": "カリナ",
                            "name_en": "Karina",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Karina.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/karina"
                        },
                        {
                            "name_jp": "ベラ",
                            "name_en": "Benedetta",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Benedetta.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/benedetta"
                        },
                        {
                            "name_jp": "ファラミス",
                            "name_en": "Faramis",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Faramis.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/faramis"
                        },
                        {
                            "name_jp": "パキート",
                            "name_en": "Paquito",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Paquito.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/paquito"
                        },
                        {
                            "name_jp": "ラプラプ",
                            "name_en": "Lapu-Lapu",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Lapu-Lapu.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/lapu-lapu"
                        },
                        {
                            "name_jp": "アルカード",
                            "name_en": "Alucard",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Alucard.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/alucard"
                        },
                        {
                            "name_jp": "エスタス",
                            "name_en": "Estes",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Estes.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/estes"
                        },
                        {
                            "name_jp": "ハナビ",
                            "name_en": "Hanabi",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Hanabi.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/hanabi"
                        },
                        {
                            "name_jp": "セイバー",
                            "name_en": "Saber",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Saber.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/saber"
                        },
                        {
                            "name_jp": "バターン",
                            "name_en": "Badang",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Badang.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/badang"
                        },
                        {
                            "name_jp": "ガトートカチャ",
                            "name_en": "Gatotkaca",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Gatotkaca.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/gatotkaca"
                        },
                        {
                            "name_jp": "エックス",
                            "name_en": "X.Borg",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/11/X-Borg.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/x-borg"
                        },
                        {
                            "name_jp": "ニュート",
                            "name_en": "Natan",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Natan.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/natan"
                        },
                        {
                            "name_jp": "シュウ",
                            "name_en": "Chou",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Chou.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/chou"
                        },
                        {
                            "name_jp": "レオモルド",
                            "name_en": "Leomord",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Leomord.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/leomord"
                        },
                        {
                            "name_jp": "ガレック",
                            "name_en": "Grock",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Grock.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/grock"
                        },
                        {
                            "name_jp": "ラズリー",
                            "name_en": "Lesley",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Lesley.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/lesly"
                        },
                        {
                            "name_jp": "ハーリー",
                            "name_en": "Harley",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Harley.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/harley"
                        },
                        {
                            "name_jp": "バルモンド",
                            "name_en": "Balmond",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Balmond.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/balmond"
                        },
                        {
                            "name_jp": "ヴァリル",
                            "name_en": "Valir",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Valir.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/valir"
                        },
                        {
                            "name_jp": "ヒルダ",
                            "name_en": "Hilda",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Hilda.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/hilda"
                        },
                        {
                            "name_jp": "アルファ",
                            "name_en": "Alpha",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Alpha.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/alpha"
                        },
                        {
                            "name_jp": "グネヴィア",
                            "name_en": "Guinevere",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Guinevere.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/guinevere"
                        },
                        {
                            "name_jp": "ザスク",
                            "name_en": "Zhask",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Zhask.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/zhask"
                        },
                        {
                            "name_jp": "アモン",
                            "name_en": "Aamon",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Aamon.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/aamon"
                        },
                        {
                            "name_jp": "マイシータール",
                            "name_en": "Minsitthar",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Minsitthar.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/minsitthar"
                        },
                        {
                            "name_jp": "グールド",
                            "name_en": "Gord",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Gord.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/gord"
                        },
                        {
                            "name_jp": "ナナ",
                            "name_en": "Nana",
                            "role": "Support",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Nana.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/nana"
                        },
                        {
                            "name_jp": "キャリー",
                            "name_en": "Karrie",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Karrie.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/karrie"
                        },
                        {
                            "name_jp": "デームス",
                            "name_en": "Thamuz",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Thamuz.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/thamuz"
                        },
                        {
                            "name_jp": "ティグラル",
                            "name_en": "Tigreal",
                            "role": "Tank",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Tigreal.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/tank/tigreal"
                        },
                        {
                            "name_jp": "マーティス",
                            "name_en": "Martis",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Martis.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/martis"
                        },
                        {
                            "name_jp": "ハリス",
                            "name_en": "Harith",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Harith.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/harith"
                        },
                        {
                            "name_jp": "ライラ",
                            "name_en": "Layla",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Layla.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/layla"
                        },
                        {
                            "name_jp": "ディスラー",
                            "name_en": "Terizla",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Terizla.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/terizla"
                        },
                        {
                            "name_jp": "サナ",
                            "name_en": "Vexana",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Vexana.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/vexana"
                        },
                        {
                            "name_jp": "ザビエル",
                            "name_en": "Xavier",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Xavier.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/xavier"
                        },
                        {
                            "name_jp": "ジュリアン",
                            "name_en": "Julian",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Julian.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/julian"
                        },
                        {
                            "name_jp": "フレッドリン",
                            "name_en": "Fredrinn",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Fredrinn.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/fredrinn"
                        },
                        {
                            "name_jp": "ジョイ",
                            "name_en": "Joy",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Joy.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/joy"
                        },
                        {
                            "name_jp": "アーロット",
                            "name_en": "Arlott",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Arlott.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/arlott"
                        },
                        {
                            "name_jp": "ノヴァリア",
                            "name_en": "Novaria",
                            "role": "Mage",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Novaria.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/mage/novaria"
                        },
                        {
                            "name_jp": "イクシア",
                            "name_en": "Ixia",
                            "role": "Marksman",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Ixia.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/hunter/ixia"
                        },
                        {
                            "name_jp": "ノーラン",
                            "name_en": "Nolan",
                            "role": "Assassin",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/12/Nolan.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/assassin/nolan"
                        },
                        {
                            "name_jp": "シーシー",
                            "name_en": "Cici",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2024/01/Cici.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/fighter/cici"
                        },
                        {
                            "name_jp": "チップ",
                            "name_en": "Chip",
                            "role": "Fighter",
                            "image_url": "https://shanbenzzz.com/wp-content/uploads/2024/04/Chip.webp",
                            "article_url": "https://shanbenzzz.com/mobile-legends/hero/support/chip"
                        }
                        ]

        for hero in hero_data:
            Hero.objects.create(
                name_jp=hero['name_jp'],
                name_en=hero['name_en'],
                role=hero['role'],
                image_url=hero['image_url'],
                article_url=hero['article_url']
            )

        self.stdout.write(self.style.SUCCESS('Hero data loaded successfully'))