import pygame
from pygame.locals import *



SCREENWIDTH  = 640
SCREENHEIGHT = 480
#1 配置图片地址
#IMAGE_PATH = 'assets/'
# 屏幕大小的常量
SCREEN_RECT = (SCREENWIDTH, SCREENHEIGHT )
#初始化
pygame.init()

# pygame.display.set_caption("游戏")
#屏幕对象
SCREEN = pygame.display.set_mode(SCREEN_RECT)
# SCREEN.fill((255, 255, 255))
# #颜色对象
# BLACK = pygame.Color(0, 0, 0)         # Black
# pygame.draw.circle(SCREEN, BLACK, (200,50), 30)

color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
# color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red
#SCREEN.fill(color2)
# pygame.draw.circle(SCREEN, color1, (200,50), 3)
# pygame.draw.line(SCREEN, color1, (30, 100), (170,170), 3)#（表面，颜色，起点，终点，宽度）

#pygame.draw.line(SCREEN, color1, (30, 100), (170,170), 3)#表面，颜色，起点，终点，宽度）

# bg = pygame.image.load('./img/bg_img.jpg')
# SCREEN.blit(bg)
FPS = pygame.time.Clock()

ball = pygame.image.load('./img/ball.jpg')
ball_rect = ball.get_rect()

while  True:
    FPS.tick(60)
    #pygame.draw.rect(SCREEN, color4, (100, 200, 100, 50), 30)
    ball_rect.x +=1
    SCREEN.blit(ball, ball_rect)
    for event in pygame.event.get():
        # 判断是否退出游戏
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()