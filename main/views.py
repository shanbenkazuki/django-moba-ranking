from django.shortcuts import render
from .models import Hero
from django.db.models import Max
from .models import HeroMetaData

import pandas as pd

def get_rank_from_z_score(score):
  if score >= 1.0:
    return 'S+'
  elif score >= 0.5:
    return 'S'
  elif score >= 0:
    return 'A+'
  elif score >= -0.5:
    return 'A'
  elif score >= -1.0:
    return 'B'
  else:
    return 'C'

# Create your views here.
def hero_ranking(request):
    heroes = Hero.objects.all().values_list('name_jp', 'name_en', 'image_url')
    context = {
        'heroes': heroes
    }

    # reference_dateの最大値（最新の日付）を取得
    latest_date = HeroMetaData.objects.aggregate(Max('reference_date'))['reference_date__max']

    # 最新の日付に対応するHeroMetaDataを取得
    latest_hero_metadata = HeroMetaData.objects.filter(reference_date=latest_date).values('name', 'win_rate', 'pick_rate', 'ban_rate', 'reference_date')

    # クエリセットをデータフレームに変換
    df = pd.DataFrame(list(latest_hero_metadata))

    # 列のデータ型を変更
    df = df.astype({'win_rate': 'float', 'pick_rate': 'float', 'ban_rate': 'float'})

    # win_rate_zの計算
    df['win_rate_z'] = (df['win_rate'] - df['win_rate'].mean()) / df['win_rate'].std()

    # pick_rate_zの計算
    df['pick_rate_z'] = (df['pick_rate'] - df['pick_rate'].mean()) / df['pick_rate'].std()

    # ban_rate_zの計算
    df['ban_rate_z'] = (df['ban_rate'] - df['ban_rate'].mean()) / df['ban_rate'].std()

    # interactionの計算
    df['interaction'] = df['win_rate_z'] * df['pick_rate_z']

    # tier_score_zの計算
    df['tier_score_z'] = 0.6 * df['win_rate_z'] + 0.25 * df['pick_rate_z'] + 0.15 * df['ban_rate_z'] - 0.2 * df['interaction']
    
    hero_dict = {}

    # DataFrameのインデックスをname_enに変更
    df = df.reset_index().set_index('name')

    for name_ja, name_en, image_url in heroes:
        hero_dict[name_en] = {
            'name_ja': name_ja,
            'image_url': image_url,
            'rank': get_rank_from_z_score(df.loc[name_en, 'tier_score_z']) if name_en in df.index else None,
        }

    # ランクごとのヒーローを格納する辞書を初期化
    rank_heroes = {
        'S+': [],
        'S': [],
        'A+': [],
        'A': [],
        'B': [],
        'C': [],
    }

    # ランクごとにヒーローを分類
    for hero, data in hero_dict.items():
        rank = data['rank']
        rank_heroes[rank].append((data['name_ja'], hero, data['image_url']))

    # contextにランクごとのヒーローを追加
    context = {
        's_plus_heroes': rank_heroes['S+'],
        's_heroes': rank_heroes['S'],
        'a_plus_heroes': rank_heroes['A+'],
        'a_heroes': rank_heroes['A'],
        'b_heroes': rank_heroes['B'],
        'c_heroes': rank_heroes['C'],
        'latest_date': latest_date.strftime('%Y-%m-%d'),
    }

    return render(request, 'main/hero_ranking.html', context)