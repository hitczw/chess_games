from copy import deepcopy
from Parameter import th
#围棋规则实现,对落子,悔棋,pass,重新开始操作进行处理
class game_rule():#游戏规则类
    def __init__(self):#设置初始参数
        self.matrix=[[0 for i in range(th+1)]for j in range(th+1)]
        self.long=th+1
        self.oder=1#行棋次序标志位,黑棋先走
        self.regret=[]#记录行棋结果,用于悔棋
        self.lastchess=[]#提一子标志位,如果只提了一个子就记录所提子
    def getblocks(self,x,y):#从某一点开始得到其所属于的块的所有点
        color=self.matrix[x][y]#得到这个点的颜色
        result=[[x,y]]#存放结果
        newarrived=[[x,y]]#初始值
        new=[]
        while(1):
            for j in newarrived:  # 遍历结果里的点
                around=self.get_aroundpoint(j[0],j[1])#计算这个点周围的点
                for i in around:#遍历这个点周围的点
                    if (self.isPointLegle(color,i[0],i[1]) and [i[0], i[1]] not in result):  # 如果点是合法的且不重复
                        result = result + [[i[0], i[1]]]  # 新的记录结果
                        new = new + [[i[0], i[1]]]

            if(new!=[]):#一次遍历结束,新的点结果不为空
                newarrived=new
                new=[]
            elif(new==[]):#结果为空,结束遍历
                return result
    def isPointLegle(self,color,x,y):#判断点是否可以延续
        if(self.ispointinmatrix(x,y) ):#判断点是否在矩阵
            if(self.matrix[x][y]==color):#判断颜色是否相同
                return 1
        return 0
    def ispointinmatrix(self,x,y):#判断点是否在矩阵里
        return 0<=x<=self.long-1 and 0<=y <=self.long-1

    @staticmethod
    def get_aroundpoint(x,y):#得到一个点四周的点
        return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]

    def get_blockaroundpoint(self,blocks):#得到方块周围的点,如果出边界则忽略
        result=[]
        for j in blocks:#遍历方块中的点
            around=self.get_aroundpoint(j[0],j[1])#得到这个点四周的点
            for point in around:
                if(self.ispointinmatrix(point[0],point[1]) and point not in (result+blocks)):#如果点在矩阵内且没在已有结果或者方块内
                    result=result+[point]
        return result
    def isblockslocked(self,block):#判断方块是否被包围,返回判断结果
        color =self.matrix[block[0][0]][block[0][1]]  # 取第一个方块的第一个棋子,得到颜色
        outside = self.get_blockaroundpoint(block)  # 得到方块周围的点
        for j in outside:  # 遍历方块周围的点
            if (self.matrix[j[0]][j[1]] != -color):  # 如果周围的点不是相反的颜色,说明没有被包围,退出搜索
                return 0
        return 1#方块被包围
    def set_zero(self,block):#进行提子操作
        for j in block:#遍历方块中的点
            self.matrix[j[0]][j[1]]=0

    def chess_move(self,x_y):#当棋子落下时候执行
        self.matrix[x_y[0]][x_y[1]] =self.oder  # 更改游戏矩阵
        around_point=self.get_aroundpoint(x_y[0],x_y[1])#得到这个点四周的点
        color=self.matrix[x_y[0]][x_y[1]]
        flag=0
        carryed_chess=[]
        for j in around_point:#遍历四周的点
            if(self.ispointinmatrix(j[0],j[1]) and self.matrix[j[0]][j[1]]==-color):#得到四周的反色棋子
               anti_block=self.getblocks(j[0],j[1])#得到反色块
               if(self.isblockslocked(anti_block)):#如果反色块被包围
                   carryed_chess=carryed_chess+[anti_block]#记录被提的棋子块
                   flag=1#提子标志位至1

        if(flag):#若果可以进行提子操作
            if(len(carryed_chess)==1 and len(carryed_chess[0])==1):#如果只提了一块棋且只提了一个子
                #print(1)
                if(carryed_chess[0][0]==self.lastchess):#若果所提的子是上一次的子
                    self.matrix[x_y[0]][x_y[1]] = 0  # 撤销此次操作,oder保持不变
                    return
                else:#提了一个子但是所提的子不是上一个子或者上一次没有提子
                    self.set_zero(carryed_chess[0])#提掉这个子
                    self.oder = -self.oder  # 交换行棋次序
                    self.regret = self.regret + [deepcopy(self.matrix)]  # 记录结果
                    self.lastchess=[x_y[0],x_y[1]]#记录这颗棋子的坐标
                    return
            self.lastchess=[]#提了不止一个棋子,将提子坐标记空
            for j in carryed_chess:#遍历棋子块
                self.set_zero(j)  # 提掉这些子
            self.oder = -self.oder  # 交换行棋次序
            self.regret = self.regret + [deepcopy(self.matrix)]  # 记录结果
            return#进行了提子操作,返回
        myblock=self.getblocks(x_y[0],x_y[1])#得到自己所属的块
        self.lastchess = []#没有进行提子操作,将提子坐标记空
        if(self.isblockslocked(myblock)):#如果是包围状态
            self.matrix[x_y[0]][x_y[1]]=0#撤销此次操作,oder保持不变
            return
        else:#不是提子状态,更改行棋次序并记录结果
            self.oder=-self.oder
            self.regret=self.regret+[deepcopy(self.matrix)]#记录结果
            return
    def regret_deal(self):#进行悔棋处理
        if(len(self.regret)==1):#若果只有一个棋子
            self.__init__()#重置游戏规则
            return
        self.matrix = deepcopy(self.regret[len(self.regret) - 2])  # 取上一次的游戏信息
        self.oder = -self.oder  # 交换行棋次序
        del self.regret[-1]  # 删除这一次的信息
