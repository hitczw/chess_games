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
        self.radius=radius
        self.touch_sensitive=touch_sensitive#点击敏感度,越小敏感度越高,最大值设为17合适,否则容易引起误触
        self.chessraius=chessraius#棋子直径
        self.font_size = font_size # 字体大小
        self.ABC_list = ABC_list
        self.compensate=compensate

        self.board=board
        self.black=black
        self.white=white
        self.font=font

    def draw_line(self,start_pos,end_pos):
        pygame.draw.aaline(self.screen, self.line_color, start_pos,end_pos,self.line_wide)
    def draw_circle(self,circle_centre):
        pygame.draw.circle(self.screen, self.basic_color, circle_centre, self.radius)
    def generate_font(self,string):
        return self.font.render(string, True, self.basic_color)
    def change_absolute(self,xy):#将点击绝对坐标换算成精确相对坐标
        result=["a","b"]
        for i in range(19):
            abosolute_point=self.start+i*self.grid_wide#计算出棋盘点的绝对坐标
            if(abs(xy[0]-abosolute_point)<=self.touch_sensitive):
                result[0]=i
            if(abs(xy[1]-abosolute_point)<=self.touch_sensitive):
                result[1]=i
        if(result[0]=="a" or result[1]=="b"):
            return None
        return result
    def change_relative(self,absolutepoint):#将相对坐标换算成绝对坐标
        x=absolutepoint[0]*self.grid_wide+start-self.chessraius/2
        y=absolutepoint[1]*self.grid_wide+start-self.chessraius/2
        return [x,y]
    def basic_draw(self):
        screen.blit(self.board, [0, 0])  # 绘制底部木纹条理
        for i in range(0, self.th+1):
            add = i * self.grid_wide
            self.draw_line((self.start + add, self.start), (self.start + add, self.start + self.grid_wide * self.th))  # 绘制竖线
            self.draw_line((self.start, self.start + add), (self.start + self.grid_wide * self.th, self.start + add))  # 绘制横线
            text_number = self.generate_font(str(i + 1))
            self.screen.blit(text_number, (self.start + add, self.start-self.font_size))  # 绘制数字
            letter = self.ABC_list[i]
            text_letter=self.generate_font(letter)
            screen.blit(text_letter, (self.start - self.font_size, self.start + add - self.compensate))  # 绘制字母
        if (self.th == 14):
            self.draw_circle((self.start + 3 * self.grid_wide, self.start + 3 * self.grid_wide))  # 仅当是标准棋盘时候绘制棋盘圆点
            self.draw_circle((self.start + 11 * self.grid_wide, self.start + 3 * self.grid_wide))
            self.draw_circle((self.start + 7 * self.grid_wide, self.start + 7 * self.grid_wide))
            self.draw_circle((self.start + 3 * self.grid_wide, self.start + 11 * self.grid_wide))
            self.draw_circle((self.start + 11 * self.grid_wide, self.start + 11 * self.grid_wide))
    def chess_draw(self,matrix):
        for i in range(th + 1):  # 遍历游戏信息矩阵绘制棋子
            for j in range(th + 1):
                if (matrix[i][j] == 1):
                    screen.blit(black, self.change_relative([i, j]))
                elif (matrix[i][j] == -1):
                    screen.blit(white, self.change_relative([i, j]))