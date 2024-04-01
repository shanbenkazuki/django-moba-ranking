from django.shortcuts import render
from .models import Hero
from django.db.models import Max
from .models import HeroMetaData
import pandas as pd

# 定数の定義
RANK_THRESHOLDS = [1.0, 0.5, 0, -0.5, -1.0]  # ランクの閾値
RANK_LABELS = ['S+', 'S', 'A+', 'A', 'B', 'C']  # ランクのラベル

def get_rank_from_z_score(score):
    """
    z-scoreからランクを取得する関数
    """
    for threshold, label in zip(RANK_THRESHOLDS, RANK_LABELS):
        if score >= threshold:
            return label
    return 'C'

def hero_ranking(request):
    # Heroモデルから必要なデータを取得
    heroes = Hero.objects.all().values_list('name_jp', 'name_en', 'image_url')
    
    # HeroMetaDataモデルから最新の日付のデータを取得
    latest_hero_metadata = HeroMetaData.objects.filter(
        reference_date=HeroMetaData.objects.latest('reference_date').reference_date
    ).values('name', 'win_rate', 'pick_rate', 'ban_rate', 'reference_date')
    
    # クエリセットをDataFrameに変換
    hero_metadata_df = pd.DataFrame(list(latest_hero_metadata))
    
    # 列のデータ型を変更
    hero_metadata_df = hero_metadata_df.astype({'win_rate': 'float', 'pick_rate': 'float', 'ban_rate': 'float'})
    
    # 各指標のz-scoreを計算
    hero_metadata_df['win_rate_z'] = (hero_metadata_df['win_rate'] - hero_metadata_df['win_rate'].mean()) / hero_metadata_df['win_rate'].std()
    hero_metadata_df['pick_rate_z'] = (hero_metadata_df['pick_rate'] - hero_metadata_df['pick_rate'].mean()) / hero_metadata_df['pick_rate'].std()
    hero_metadata_df['ban_rate_z'] = (hero_metadata_df['ban_rate'] - hero_metadata_df['ban_rate'].mean()) / hero_metadata_df['ban_rate'].std()
    
    # interactionの計算
    hero_metadata_df['interaction'] = hero_metadata_df['win_rate_z'] * hero_metadata_df['pick_rate_z']
    
    # tier_score_zの計算
    hero_metadata_df['tier_score_z'] = 0.6 * hero_metadata_df['win_rate_z'] + 0.25 * hero_metadata_df['pick_rate_z'] + 0.15 * hero_metadata_df['ban_rate_z'] - 0.2 * hero_metadata_df['interaction']
    
    # DataFrameのインデックスをname_enに変更
    hero_metadata_df = hero_metadata_df.reset_index().set_index('name')
    
    hero_dict = {}
    for name_ja, name_en, image_url in heroes:
        if name_en in hero_metadata_df.index:
            hero_dict[name_en] = {
                'name_ja': name_ja,
                'image_url': image_url,
                'rank': get_rank_from_z_score(hero_metadata_df.loc[name_en, 'tier_score_z']),
            }
    
    # ランクごとのヒーローを格納する辞書を初期化
    rank_heroes = {rank: [] for rank in RANK_LABELS}
    
    # ランクごとにヒーローを分類
    for hero, data in hero_dict.items():
        rank_heroes[data['rank']].append((data['name_ja'], hero, data['image_url']))
    
    # contextにランクごとのヒーローを追加
    context = {f"{rank.lower().replace('+', '_plus')}_heroes": heroes for rank, heroes in rank_heroes.items()}
    
    # contextに最新の日付を追加
    context['latest_date'] = latest_hero_metadata[0]['reference_date'].strftime('%Y-%m-%d')
    
    # hero_ranking.htmlテンプレートにcontextを渡してレンダリング
    return render(request, 'main/hero_ranking.html', context)