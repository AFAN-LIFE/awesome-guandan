import random
import numpy as np
import pandas as pd

suits = ['♠', '♥', '♣', '♦']  # 黑桃, 红心, 梅花, 方片
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# 创建一副牌
deck = [f'{rank}{suit}' for suit in suits for rank in ranks]
deck += ['BJ', 'RJ']  # 加入两张王
# 洗牌发牌，每人27张（掼蛋通常4人）
# 上一个视频中的代码这块有点问题，这里修复了
def deal(deck, seed):
    random.seed(seed)
    two_decks = deck + deck
    random.shuffle(two_decks)
    return [two_decks[i::4] for i in range(4)]

def trans_hand_into_df(hand):
    df = pd.DataFrame(columns=['♠', '♥', '♣', '♦', 'sum'], data=0,
             index=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'BJ', 'RJ'])
    for i in hand:
        if i == 'BJ':
            df.loc['BJ', 'sum'] += 1
        elif i == 'RJ':
            df.loc['RJ', 'sum'] += 1
        else:
            df.loc[i[:-1], i[-1]] += 1
    df['sum'] += df.loc[:, ['♠', '♥', '♣', '♦']].sum(axis=1)
    return df

def poker_card_sort(cards):
    # 定义花色和牌面顺序
    suits = {'♠': 3, '♦': 2, '♥': 1, '♣': 0}
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'BJ': 15, 'RJ': 16}

    # 排序函数
    def sort_key(card):
        if card not in ['BJ', 'RJ']:
            rank, suit = card[:-1], card[-1]
            return (ranks[rank], suits[suit])
        else:
            return (ranks[card], 0)

    # 排序并返回结果
    sorted_cards = sorted(cards, key=sort_key)
    return sorted_cards


if __name__ == '__main__':
    hand_list = deal(deck, 42)[0]
    print(hand_list)
    print(poker_card_sort(hand_list))
    hand_df = trans_hand_into_df(hand_list)
    print(hand_df)