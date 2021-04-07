import pygame

#基本参数设置
start=30#起点绝对坐标
line_color=(200,200,200)#线条颜色
line_wide=1#线宽,像素单位,整型变量
grid_wide=35#格子长度
th=8#棋盘一排的格子数,标准黑白棋为8*8,格子数为8,应为偶数,由于图片大小原因,最大设置为18
basic_color=(0,0,0)#基本颜色
long=start+th*grid_wide+36#游戏界面大小
font_size=15#字体大小
compensate=10#字体位置补偿
ABC_list=[]#字母表
radius=5
radiuscolor=(255,0,0)
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



