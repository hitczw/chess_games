from copy import deepcopy
from Parameter import th
#围棋规则实现,对落子,悔棋,pass,重新开始操作进行处理
class game_rule():#游戏规则类
    def __init__(self):#设置初始参数
        self.matrix=[[0 for i in range(th+1)]for j in range(th+1)]
        self.long=th+1
        self.oder=1#行棋次序标志位,黑棋先走
        self.regret=[]#记录行棋结果,用于悔棋
        self.direction=[[1,1],[0,1],[1,0],[1,-1]]
        self.gameover=0
    def ispointinmatrix(self,x_y):#判断点是否在矩阵里
        return 0<=x_y[0]<=self.long-1 and 0<=x_y[1]<=self.long-1

    def get_dirction(self,start,direction):#得到在方向上的棋子数量
        st=start
        result=0
        while(1):
            next_point=[st[0]+direction[0],st[1]+direction[1]]
            if(not self.ispointinmatrix(next_point)):#如果点在棋盘外
                return result
            elif(self.matrix[next_point[0]][next_point[1]]==-self.oder):#如果点是其他棋子
                return result
            elif(self.matrix[next_point[0]][next_point[1]]==0):#如果点没有棋子
                return result
            #排除以上情况,剩下点是本身棋子的情况
            result=result+1#记录这个棋子
            st=deepcopy(next_point)

    def judge_win(self,x_y):#判断是否五子连珠
        for j in self.direction:#遍历4个方向,加入反方向为8个方向
            number=self.get_dirction(x_y,j)+self.get_dirction(x_y,[-j[0],-j[1]])
            if(number+1>=5):
                return 1
        return 0

    def chess_move(self,x_y):#当棋子落下时候执行
        if(self.gameover):#游戏结束不做处理
            return
        self.matrix[x_y[0]][x_y[1]] =self.oder  # 更改游戏矩阵
        if(self.judge_win(x_y)):
            print("Game Over")
            self.gameover=1
            if(self.oder==1):
                print("Black Wins!")
            else:
                print("White Wins!")
            print("\n")
        self.oder=-self.oder
        self.regret=self.regret+[deepcopy(self.matrix)]#记录结果
        return
    def regret_deal(self):#进行悔棋处理
        self.gameover=0
        if(len(self.regret)==1):#若果只有一个棋子
            self.__init__()#重置游戏规则
            return
        self.matrix = deepcopy(self.regret[len(self.regret) - 2])  # 取上一次的游戏信息
        self.oder = -self.oder  # 交换行棋次序
        del self.regret[-1]  # 删除这一次的信息
