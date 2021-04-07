from ClassBasicDraw import*
from ClassRule import*
from sys import exit

print('''欢迎来到五子棋界面
基本操作:
    按空格键悔棋
    按r重新开始
programmed by hitczw
         ''')

rule=game_rule()#建立规则对象
real_exam=game_draw()#建立绘制对象

while(1):
    for e in pygame.event.get():
        if e.type==QUIT:#检测到退出则退出游戏
            exit()
        elif e.type==MOUSEBUTTONDOWN:#每当按键按下时候检测
            x_y=real_exam.change_absolute(e.pos)#得到相对坐标
            if(x_y!=None and rule.matrix[x_y[0]][x_y[1]]==0):#当落子在棋盘内判且落下地方没有棋子
                rule.chess_move(x_y)#对落子进行处理

        elif e.type==KEYDOWN :
            if(len(rule.regret)>=1and e.key==32):#每当按下空白键的时候执行悔棋
                rule.regret_deal()
            elif(e.key==114):#每当按下r键的时候重新开始
                rule.__init__()

    real_exam.basic_draw()#对基本对象进行绘制
    real_exam.chess_draw(rule.matrix)#对棋子进行绘制
    pygame.display.update()#刷新界面

