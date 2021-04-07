import pygame
from pygame.locals import *
#基本参数设置
start=30#起点绝对坐标
line_color=(200,200,200)#线条颜色
line_wide=1#线宽,像素单位,整型变量
grid_wide=35#格子长度
th=14#棋盘一排的格子数,标准五子棋棋盘为15*15,格子数为14
basic_color=(0,0,0)#基本颜色
long=start+th*grid_wide+36#游戏界面大小
radius=5#棋盘圆点直径大小
touch_sensitive=13#点击敏感度,越小敏感度越高,最大值设为17合适,否则容易引起误触
chessraius=33
font_size=15#字体大小
compensate=10#字体位置补偿
ABC_list=[]#字母表
for i in range(65,65+th+1,1):#计算abc列表
    ABC_list=ABC_list+[chr(i)]

pygame.init()

screen = pygame.display.set_mode((long,long))
board_picture="picture\\board.jpg"
board=pygame.image.load(board_picture).convert()#底部木头纹理图片
black_picture="picture\\black.png"
black=pygame.image.load(black_picture).convert_alpha()#黑棋图片
white_picture="picture\\white.png"
white=pygame.image.load(white_picture).convert_alpha()#白棋图片
font= pygame.font.SysFont("arial", font_size)



