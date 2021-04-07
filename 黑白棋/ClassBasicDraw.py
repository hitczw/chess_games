from Parameter import*
#基本界面绘制,包括棋盘,线条,棋子
class game_draw():#建立游戏绘制对象
    def __init__(self):
        self.start = start
        self.line_color = line_color
        self.line_wide = line_wide
        self.grid_wide = grid_wide
        self.th = th
        self.basic_color = basic_color
        self.screen=screen
        self.font_size = font_size # 字体大小
        self.ABC_list = ABC_list
        self.compensate=compensate
        self.radius=radius
        self.radiuscolor=radiuscolor
        self.blue=(0,125,255)

        self.board=board
        self.black=black
        self.white=white
        self.font=font

    def draw_line(self,start_pos,end_pos):
        pygame.draw.aaline(self.screen, self.line_color, start_pos,end_pos,self.line_wide)
    def draw_circle(self,circle_centre):
        pygame.draw.circle(self.screen, self.radiuscolor, circle_centre, self.radius)
    def generate_font(self,string):
        return self.font.render(string, True, self.basic_color)
    def change_absolute(self,xy):#将点击绝对坐标换算成精确相对坐标
        result=["a","b"]
        for i in range(th):
            min=self.change_relativenumber(i)#计算出格子边界
            max=self.change_relativenumber(i)+self.grid_wide
            if(min<=xy[0]<=max):
                result[0]=i
            if(min<=xy[1]<=max):
                result[1]=i
        if(result[0]=="a" or result[1]=="b"):
            return None
        return result

    def change_relative(self,point):#将相对坐标换算成绝对坐标
        x=self.change_relativenumber(point[0])
        y=self.change_relativenumber(point[1])
        return [x,y]
    def change_relativenumber(self,number):
        return number*self.grid_wide+self.start
    def change_relativenumber2(self,number):
        return self.start+number*self.grid_wide+int(self.grid_wide/2)
    def basic_draw(self):
        self.screen.blit(self.board, [0, 0])  # 绘制底部木纹条理
        for i in range(0, self.th+1):
            add = i * self.grid_wide
            self.draw_line((self.start + add, self.start), (self.start + add, self.start + self.grid_wide * self.th))  # 绘制竖线
            self.draw_line((self.start, self.start + add), (self.start + self.grid_wide * self.th, self.start + add))  # 绘制横线
        for i in range(0,self.th):
            add = i * self.grid_wide+self.grid_wide/2
            text_number = self.generate_font(str(i + 1))
            self.screen.blit(text_number, (self.start + add, self.start - self.font_size))  # 绘制数字
            letter = self.ABC_list[i]
            text_letter = self.generate_font(letter)
            self.screen.blit(text_letter, (self.start - self.font_size, self.start + add - self.compensate))  # 绘制字母
    def chess_draw(self,matrix):
        for i in range(self.th):  # 遍历游戏信息矩阵绘制棋子
            for j in range(self.th):
                if (matrix[i][j] == 1):
                    self.screen.blit(self.black, self.change_relative([i, j]))
                elif (matrix[i][j] == -1):
                    self.screen.blit(self.white, self.change_relative([i, j]))
    def drawcirclelyst(self,lyst):
        for j in lyst:
            abs_point=[self.change_relativenumber2(j[0]),self.change_relativenumber2(j[1])]#得到绝对坐标
            self.draw_circle(abs_point)

