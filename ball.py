# -*- coding: utf-8 -*-
# @Date    : 2021-01-25 16:38:17
# @Author  : autohe (${email})
# @知乎    : https://www.zhihu.com/people/kuanye
# @微信    : xdxh-1
# @funtion : 球的碰撞
# @Version : $Id$

import os
import pygame
import sys
from pygame.locals import *
import random 

SCREENWIDTH  = 480
SCREENHEIGHT = 640
#1 配置图片地址
IMAGE_PATH = './img/'
# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
# 刷新的帧率
FRAME_PER_SEC = 60

class Background(pygame.sprite.Sprite):
    """背景精灵"""
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + img_path)
        self.rect = self.image.get_rect()

    def update(self):
        pass

class Ball(pygame.sprite.Sprite):
    """球"""
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + img_path)
        self.rect = self.image.get_rect()
        self.speed = [5, 5]
        self.rect.left = 100
        self.rect.top = 100
    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > SCREEN_RECT.width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_RECT.height:
            self.speed[1] = -self.speed[1]




class Game:
    """主游戏"""
    def __init__(self):
        print("游戏初始化")
        # 1，创建游戏的窗口
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2，创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3，调用私有方法， 精灵和精灵组的创建
        pygame.display.set_caption("游戏")
        self.__create_sprites()

    def __create_sprites(self):
        '''创建游戏需要的精灵，比如敌人，玩家，背景等图片加载'''
        color = (255, 255, 255)
        self.screen.fill(color)

        self.bg_group = pygame.sprite.Group()
        self.bg = Background('bg_img.jpg')
        self.bg_group.add(self.bg)

        self.ball_group = pygame.sprite.Group()
        self.ball = Ball('yball.png')
        self.ball_group.add(self.ball)
        # self.sun = pygame.image.load(IMAGE_PATH+'sun.png')yball.png
        # self.sun = pygame.transform.scale(self.sun, (80, 80))  #缩放
        # self.sun_rect = self.sun.get_rect()
        # self.sun_rect.top = 100
        # self.sun_rect.left = 200


    def start_game(self):
        print("游戏开始...")
        while True:
            # 1，设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2，事件监听
            self.__event_handler()
            # 3，碰撞检测
            self.__check_collide()
            # 4，更新/绘制精灵组
            self.__update_sprites()
            # 5，更新显示
            pygame.display.update()

    def __event_handler(self):
        '''检测鼠标，键盘案件，或者其他游戏状态'''
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                Game.__game_over()
    def __check_collide(self):
        '''检测游戏碰撞的实现'''
    def __update_sprites(self):
        '''更新游戏精灵的状态'''
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.ball_group.update()
        self.ball_group.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    # 创建游戏对象
    game = Game()
    # 启动游戏
    game.start_game()