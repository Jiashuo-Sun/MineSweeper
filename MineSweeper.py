import pygame
from pygame.locals import *
import sys
import copy
from random import *

# define constants
MINE_NUMB = 5
SCREEN_SIZE = (330,450)
SCREEN_COLOR = (150,150,150)
SQUARE_LENGTH = 30
SQUARE_SIZE = (SQUARE_LENGTH, SQUARE_LENGTH)
SQUARE_COLOR = (0,0,0)
LOCATION_NUMB1 = (30,30)
LOCATION_NUMB2 = (45,30)
LOCATION_RESTART = (120,30)

# input images for mine sweeper
image_mine = pygame.image.load('mine.bmp')
image_numb = pygame.image.load('MineNumb.bmp')
image_restart = pygame.image.load('Restart.png')
image_lose = pygame.image.load('Lose.png')
image_win = pygame.image.load('Win.png')
name_mine = ["blank","flag",9,"wrongflag",'mine',8,7,6,5,4,3,2,1,0]
name_numb = [9,8,7,6,5,4,3,2,1,0]
mineimgs = {}
for i in range(14): mineimgs[name_mine[i]] = image_mine.subsurface((0,i*30,30,30))
numbimgs = {}
for i in range(10): numbimgs[name_numb[i]] = image_numb.subsurface((0,i*25,15,25))

# the class for mines
class mine():
    def __init__(self):
        self.o_m, self.o_v, self.nb_m, self.nb_v = self.creat_mine(MINE_NUMB)
        self.flag_v = []
        self.stat_v = []
        for i in range(81): self.stat_v.append(1)
        for i in range(81): self.flag_v.append(0)
        
        self.mine_now = sum(self.flag_v + self.o_v)

# creat all 81 mines
    def creat_mine(self,numb):
        o_v=[]
        o_m = []
        nb_m = []
        nb_v = []
        
        temp = sample(range(81),numb)
        for i in range(81):
            if i in temp:
                o_v.append(1)
            else:
                o_v.append(0)
    
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(o_v[9*i+j])
            o_m.append(temp)
            
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(0)
            nb_m.append(temp)
  
        for i in range(9):
            for j in range(9):
                if o_m[i][j] == 1:
                    nb_m[i][j] = 9 
    
        for i in range(1,8):
            for j in range(1,8):
                if o_m[i][j] == 0:
                    nb_m[i][j] = o_m[i-1][j-1]+o_m[i-1][j]+o_m[i-1][j+1]+o_m[i][j-1]+o_m[i][j+1]+o_m[i+1][j-1]+o_m[i+1][j]+o_m[i+1][j+1]

        for j in range(1,8):
            if o_m[0][j] == 0 :
                nb_m[0][j] = o_m[0][j-1]+o_m[0][j+1]+o_m[1][j-1]+o_m[1][j]+o_m[1][j+1]
            if o_m[8][j] == 0:
                nb_m[8][j] = o_m[7][j-1]+o_m[7][j]+o_m[7][j+1]+o_m[8][j-1]+o_m[8][j+1]
            if o_m[j][0] == 0:
                nb_m[j][0] = o_m[j-1][0]+o_m[j+1][0]+o_m[j-1][1]+o_m[j][1]+o_m[j+1][1]
            if o_m[j][8] == 0:
                nb_m[j][8] = o_m[j-1][7]+o_m[j][7]+o_m[j+1][7]+o_m[j-1][8]+o_m[j+1][8]

        nb_m[0][0] = o_m[0][1]+o_m[1][0]+o_m[1][1]
        nb_m[0][8] = o_m[0][7]+o_m[1][7]+o_m[1][8]
        nb_m[8][0] = o_m[7][0]+o_m[7][1]+o_m[8][1]
        nb_m[8][8] = o_m[7][7]+o_m[7][8]+o_m[8][7]
    
        for i in range(9):
            for j in range(9):
                nb_v.append(nb_m[i][j])
            
        return o_m, o_v, nb_m, nb_v      

# The Following 4 functions (covermatrix, record, transfer11, play) are made by Guanchao Tong.
# In the main part, only need use 'covermatrix' as the request function.

# These four functions will complete the user request: 
# When user click a blank mine, it will show all the blank mines connected to this one and the non-blank ones directly connected in the neighborhood of all these blank mines.

    def covermatrix(self):
        covermatrix = []
        length1 = 9
        for i in range(0,length1+2):
            ten=[]
            for j in range(0,length1+2):
                ten.append(10);
            covermatrix.append(ten)
        return covermatrix

    def record(self):
        record = []
        length1 = 9
        for i in range(0,length1+2):
            ten=[]
            for j in range(0,length1+2):
                ten.append(0);
            record.append(ten)
        return record

    def transfer11(self,NumberMatrix_o):
        NumberMatrix=[]
        for x in range(0,11):
            temp = []
            for y in range(0,11):
                temp.append(11)
            NumberMatrix.append(temp)
    
        for i in range(1,10):
            for j in range(1,10):
                NumberMatrix[i][j] = copy.deepcopy(NumberMatrix_o[i-1][j-1])
        return NumberMatrix
        
    def play(self,i,j,NumberMatrix,covermatrix,record):  
        c = []
        step=[]
        
        for x in range(1,10):
            for y in range(1,10):
                if covermatrix[x][y] != 10:
                    step.append([x,y])
        if record[i][j] == 0 :
            covermatrix[i][j] = NumberMatrix[i][j]
            record[i][j] = 1
            if i<1 or i>9 or j<1 or j>9:
                for x in range(1,10):
                    for y in range(1,10):
                        if covermatrix[x][y] != 10:
                            c.append([x-1,y-1])
                return c
     
            if NumberMatrix[i][j] == 0:
                covermatrix[i-1][j-1] = NumberMatrix[i-1][j-1]
                covermatrix[i-1][j] = NumberMatrix[i-1][j]
                covermatrix[i-1][j+1] = NumberMatrix[i-1][j+1]
                covermatrix[i][j-1] = NumberMatrix[i][j-1]
                covermatrix[i][j+1] = NumberMatrix[i][j+1]
                covermatrix[i+1][j-1] = NumberMatrix[i+1][j-1]
                covermatrix[i+1][j] = NumberMatrix[i+1][j]
                covermatrix[i+1][j+1] = NumberMatrix[i+1][j+1]
                for a in [(i-1),i,(i+1)]:
                    for b in [(j-1),j,(j+1)]:
                        self.play(a,b,NumberMatrix,covermatrix,record)
        
            for x in range(1,10):
                for y in range(1,10):
                    if covermatrix[x][y] != 10:
                        c.append([x-1,y-1])
            return c

# find the number of the mines in a particular mine's neighborhood  
    def find_nb(self,matrix,i,j,n):
        if i in range(0,9) and j in range(1,9) and matrix[i][j-1] == 0 :
            n.append(9*i+j-1)
            matrix[i][j-1] = -1
            self.find_nb(matrix,i,j-1,n)
        elif i in range(0,9) and j in range(1,9) and matrix[i][j-1] != 0 and  matrix[i][j-1] != -1:
            n.append(9*i+j-1)
        
        if i in range(1,9) and j in range(0,9) and matrix[i-1][j] == 0 :
            n.append(9*(i-1)+j)
            matrix[i-1][j] = -1
            self.find_nb(matrix,i-1,j,n)
        elif i in range(1,9) and j in range(0,9) and matrix[i-1][j] != 0 and  matrix[i-1][j] != -1:
            n.append(9*(i-1)+j)
        
        if i in range(0,9) and j in range(0,8) and matrix[i][j+1] == 0 :
            n.append(9*i+j+1)
            matrix[i][j+1] = -1
            self.find_nb(matrix,i,j+1,n)    
        elif i in range(0,9) and j in range(0,8) and matrix[i][j+1] != 0 and matrix[i][j+1] != -1:
            n.append(9*i+j+1)
        
        if i in range(0,8) and j in range(0,9) and matrix[i+1][j] == 0 :
            n.append(9*(i+1)+j)
            matrix[i+1][j] = -1
            self.find_nb(matrix,i+1,j,n)
        elif i in range(0,8) and j in range(0,9) and matrix[i+1][j] != 0 and matrix[i+1][j] != -1:
            n.append(9*(i+1)+j)      
        return n

# find the position(index) for a particular mine
# save mines in a array first, need to turn them into a matrix
    def find_index(self,n):
        n_i = []
        n_j = []
        for i in n:
            n_i.append(i//9)
            n_j.append(i%9)
        return n_i,n_j

        
class main():
    def __init__(self):
# initualize the UI    
        pygame.init()
        self.running = True
        self.isrestart = False  
        self.ismine = False

# set UI parameters        
        self.screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
        self.screen.fill(SCREEN_COLOR)
        pygame.display.set_caption("Mine Sweeper")
        self.screen.blit(image_restart,LOCATION_RESTART)

# print the new screen for a new start        
    def new_screen(self):
        self.print_numb(MINE_NUMB) 
        for i in range(9):
            for j in range(9):
                self.print_mine("blank",i,j)

# print the number of mines remained (not found)
    def print_numb(self,n):     
        if n == 10:
            self.screen.blit(numbimgs[1],LOCATION_NUMB1)
            self.screen.blit(numbimgs[0],LOCATION_NUMB2)
            pygame.display.flip()
        if n in range(10):
            self.screen.blit(numbimgs[0],LOCATION_NUMB1)
            self.screen.blit(numbimgs[n],LOCATION_NUMB2)
            pygame.display.flip()

# print mine pictures
    def print_mine(self,name,i,j):
        self.screen.blit(mineimgs[name],(30+SQUARE_LENGTH*i,150+SQUARE_LENGTH*j))
        pygame.display.flip()    

# this is the main interaction with user's left mouse click        
    def click_left(self,x,y):
        if self.ismine :
            i,j = self.find_location(x,y) 
            if self.Mine.stat_v[9*i+j] == 1:
                num = int(self.Mine.nb_m[i][j])
                if num in range(9):
                    self.Mine.stat_v[9*i+j] = 0
                    self.print_mine(num,i,j)

                if num == 9:
                    self.print_mine(num,i,j)
                    self.gamelose()
                if num == 0:
                    n = []
                    covermatrix = self.Mine.covermatrix()
                    record = self.Mine.record()
                    matrix = self.Mine.transfer11(self.Mine.nb_m)
                    n = self.Mine.play(i+1,j+1,matrix,covermatrix,record)
                    print(covermatrix)

                    for k in range(len(n)):
                        self.print_mine(self.Mine.nb_m[n[k][0]][n[k][1]] ,n[k][0],n[k][1])
                        self.Mine.stat_v[9*n[k][0]+n[k][1]] =0
             
             
            self.ismine = False
        if self.isrestart :
            self.restart()      

# this is the main interaction with user's right mouse click  
    def click_right(self,x,y):
        if self.ismine:
            i,j = self.find_location(x,y)
            if self.Mine.stat_v[9*i+j] == 1:
            
                if self.Mine.flag_v[9*i+j] == 0:
                    self.print_mine('flag',i,j)
                    self.Mine.flag_v[9*i+j] = -1
                    self.Mine.stat_v[9*i+j] = 0
                    self.Mine.mine_now = sum(self.Mine.flag_v + self.Mine.o_v)
                    self.print_numb(self.Mine.mine_now)
                elif self.Mine.flag_v[9*i+j] == -1:
                    self.Mine.flag_v[9*i+j] = 0
                    self.print_mine('blank',i,j)
                    self.Mine.mine_now = sum(self.Mine.flag_v + self.Mine.o_v)
                    self.print_numb(self.Mine.mine_now)

                    self.Mine.stat_v[9*i+j] = 1
                    
            self.print_numb(self.Mine.mine_now)

            self.ismine = False

# test if the click is in the proper area              
    def find_area(self,x,y):
        if x in range(30,300) and y in range(150,420):
            self.ismine = True
            self.isrestart = False
        elif x in range(120,210) and y in range(30,120):
            self.ismine = False
            self.isrestart = True
        else:
            self.ismine = False
            self.isrestart = False

# find the location of the mine for each click
    def find_location(self,x,y):
        xx = (x-30) // SQUARE_LENGTH
        yy = (y-150) // SQUARE_LENGTH
        return xx,yy

# restart the game     
    def restart(self):
        self.new_game()
        self.isrestart = False
        self.screen.blit(image_restart,LOCATION_RESTART)        

# start a new game        
    def new_game(self):
        self.new_screen()
        self.Mine = mine()

# when game is over
    def gameover(self):
        k = 0
        for i in range(81):
            k = self.Mine.stat_v[i]+self.Mine.o_v[i]
        if sum(self.Mine.stat_v) == 0 and k ==0: 
            self.gamewin() 
        else: 
            self.gamelose()
            for i in range(81):
                self.Mine.stat_v[i] =0;

# when user loses the game, show lost result   
    def gamelose(self):
        self.screen.blit(image_lose,LOCATION_RESTART)
        
# when user wins the game, show win result
    def gamewin(self):
        self.screen.blit(image_win,LOCATION_RESTART)

# stop the whole process 
    def quit(self):
        self.running = False

# start the whole process        
    def run(self):
        
        self.new_game()
        
        while self.running :
    
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            if event.type == MOUSEBUTTONDOWN:
                click_mouse = pygame.mouse.get_pressed()
                x,y = pygame.mouse.get_pos()
                self.find_area(x,y)
                if click_mouse[0]:
                    self.click_left(x,y)
                if click_mouse[2]:
                    self.click_right(x,y)
            if sum(self.Mine.stat_v)==0:
                self.gameover()
    
            pygame.display.flip()
    
if __name__ == '__main__':
    application = main()
    application.run()             
