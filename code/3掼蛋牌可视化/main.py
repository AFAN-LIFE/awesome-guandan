import os
import sys
import time
import pygame
from util import deal, deck, poker_card_sort

# 设定画面和牌的大小、可覆盖的比例
BASE_CARD_WIDTH, BASE_CARD_HEIGHT = 500, 726
CARD_RATIO, COVER_RATIO = 1/3, 2/3
CARD_WIDTH, CARD_HEIGHT = BASE_CARD_WIDTH * CARD_RATIO, BASE_CARD_HEIGHT*CARD_RATIO
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
COVER_WIDTH = 500 * CARD_RATIO * COVER_RATIO

# 获取扑克牌的图片
cards_path = os.path.join('cards')
png_list = os.listdir(cards_path)
png_list = [i for i in png_list if i.endswith('png')]
cards_dict = {i.split('.')[0]: os.path.join(cards_path, i) for i in png_list}
assert len(cards_dict) == 54

# 开始初始化窗口设置颜色
pygame.init()
bg_color = (0, 128, 128)
pygame.display.set_caption('AFAN掼蛋对战平台')
screen_image = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen_image.fill(bg_color)
screen_rect = screen_image.get_rect()

# 生成自己的手牌
hold_card_list = deal(deck, 42)[0]
hold_card_list = poker_card_sort(hold_card_list)

# 加载手牌需要的图片
show_image_list, show_rect_list = [], []
start_x = (screen_image.get_width() - (CARD_WIDTH - COVER_WIDTH) * len(hold_card_list)) // 2
for i, card_name in enumerate(hold_card_list):
    card_image = pygame.image.load(cards_dict[card_name])
    card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
    card_rect = card_image.get_rect()
    # 开始计算每张牌的中心位置
    card_rect.centerx = start_x + (i % len(hold_card_list)) * (CARD_WIDTH - COVER_WIDTH)  # 计算每张牌的x坐标
    card_rect.centery = screen_image.get_height() // 2  # 所有牌都在屏幕中间垂直排列
    show_image_list.append(card_image)
    show_rect_list.append(card_rect)

# 将图片展示到屏幕中
for i, j in zip(show_image_list, show_rect_list):
    screen_image.blit(i, j)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()