from copy import deepcopy
from Parameter import th
#围棋规则实现,对落子,悔棋,pass,重新开始操作进行处理
class game_rule():#游戏规则类
    def __init__(self):#设置初始参数
        self.matrix=[[0 for i in range(th)]for j in range(th)]
        self.max=int(th/2)
        self.min=int(th/2-1)
        self.matrix[self.max][self.max]=-1
        self.matrix[self.min][self.min]=-1
        self.matrix[self.max][self.min]=1
        self.matrix[self.min][self.max]=1
        self.oder=1#行棋次序标志位,黑棋先走
        self.regret=[]#记录行棋结果,用于悔棋
        self.long=th
        self.legal=self.wherecanGo2()#合法的可以走的地方
    def inside(self,x_y):#判断点是否在边界内
        return 0<=x_y[0]<=self.long-1 and 0<=x_y[1]<=self.long-1
    def get_direction(self,x_y):#得到一个点八个方向的点中的反色点
        lyst=[1,-1,0]
        result=[]
        newresult=[]
        for j in lyst:
            for i in lyst:
                result=result+[[x_y[0]+j,x_y[1]+i]]
        result.remove(x_y)
        for j in result:
            if(self.inside(j) and  self.matrix[j[0]][j[1]]==-self.oder):#判断是否在边界内且颜色相反
                newresult=newresult+[j]
        return newresult

    def extent(self,direction,start):#从反色点出发看是否存在翻转情况,存在返回中间被翻得棋子列表
        # direction为向量差,start为初始反色点
        node=deepcopy(start)
        color=self.oder#颜色
        result=[deepcopy(start)]
        while(1):
            next=[node[0]+direction[0],node[1]+direction[1]]#计算下一个点
            if(self.inside(next)):#如果点在边界内
                if(self.matrix[next[0]][next[1]]==-color):#如果是反色点
                    node=deepcopy(next)#从下一个点继续出发
                    result=result+[deepcopy(next)]
                    continue#继续循环
                elif(self.matrix[next[0]][next[1]]==color):#如果是本色点,说明可以翻转,返回终点翻转点
                    return result
                elif(self.matrix[next[0]][next[1]]==0):#如果是空白
                    return 0
            else:#如果在边界外
                return 0
    def whichTorotate(self,x_y):#输入坐标点,返回被翻转的点
        around_point=self.get_direction(x_y)#得到四周的反色点
        result=[]#中间变量
        for j in around_point:#遍历反色点
            direction=[j[0]-x_y[0],j[1]-x_y[1]]#得到差向量
            final=self.extent(direction,j)#判断这个方向是否可以翻子
            if(final!=0):#这个方向可以翻子可以翻子
                result=result+final
        return result
    def wherecanGo2(self):#计算当前局面可以走的地方
        result=[]
        for x in range(self.long):
            for y in range(self.long):
                if (self.matrix[x][y] == 0 and self.whichTorotate([x,y])!=[]):  # 如果这个地方是空白且可以翻转的不为空
                    result=result+[[x,y]]
        return result
    def rotate(self,lyst):#执行翻转操作,输入为被翻转列表
        for j in lyst:
            self.matrix[j[0]][j[1]]=self.oder
        return
    def get_score(self):#得到局面比分
        black=0
        white=0
        for x in range(self.long):
            for y in range(self.long):
                if(self.matrix[x][y]==1):
                    black=black+1
                elif(self.matrix[x][y]==-1):
                    white=white+1
        return black,white
    def chess_move(self,x_y):#当棋子落下时候执行,输入为落子坐标
        if(x_y not in self.legal):#没有下在合法区域,不做改变返回
            return
        #下在了合法区域
        WhatToChange=self.whichTorotate(x_y)#计算被翻转的点
        self.rotate(WhatToChange)#进行翻转操作
        self.matrix[x_y[0]][x_y[1]]=self.oder#成功落子
        self.oder = -self.oder#改变行棋次序
        self.legal=self.wherecanGo2()#计算下一次可以翻转的点
        if(self.legal==[]):#如果下一次可以翻转的点是空,要停止一手
            self.oder=-self.oder#改回行棋次序
            self.legal=self.wherecanGo2()#再次计算本方可以走的地方
            if(self.legal==[]):#如果还是等于空,双方均无法下子,游戏结束
                print("Game Over")
                self.regret = self.regret + [deepcopy(self.matrix)]
                score=self.get_score()
                print("Black:",score[0])
                print("White:",score[1])
                return
            else:#如果本方可以下子
                self.regret = self.regret + [deepcopy(self.matrix)]
                if(self.oder==1):
                    print("White has no place to go,Black continue")
                elif(self.oder==-1):
                    print("Black has no place to go,White continue")
                return #返回等待下一次处理
        #对方翻转的点不是空
        self.regret = self.regret + [deepcopy(self.matrix)]  # 记录结果
        return

    def regret_deal(self):#进行悔棋处理
        if(len(self.regret)==1):#若果只有一个棋子
            self.__init__()#重置游戏规则
            return
        self.matrix = deepcopy(self.regret[len(self.regret) - 2])  # 取上一次的游戏信息
        self.oder = -self.oder  # 交换行棋次序
        if(self.wherecanGo2()==[]):
            self.oder=-self.oder
        self.legal=self.wherecanGo2()#


        del self.regret[-1]  # 删除这一次的信息

