import pygame
from pygame.locals import *
import sys 
import copy
from random import *

SCREEN_SIZE = (330 , 450)
SQUARE_LENGTH = 30
SQUARE_SIZE = (SQUARE_LENGTH, SQUARE_LENGTH)
SQUARE_COLOR = (100,100,100)
MINE_NUMBER = 10


def creat_mine(numb):
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

n = []
def find_nb(matrix,i,j,n):
    if i in range(0,9) and j in range(1,9) and matrix[i][j-1] == 0 :
        n.append(9*i+j-1)
        matrix[i][j-1] = -1
        find_nb(matrix,i,j-1,n)
    elif i in range(0,9) and j in range(1,9) and matrix[i][j-1] != 0 and  matrix[i][j-1] != -1:
        n.append(9*i+j-1)
        
    if i in range(1,9) and j in range(0,9) and matrix[i-1][j] == 0 :
        n.append(9*(i-1)+j)
        matrix[i-1][j] = -1
        find_nb(matrix,i-1,j,n)
    elif i in range(1,9) and j in range(0,9) and matrix[i-1][j] != 0 and  matrix[i-1][j] != -1:
        n.append(9*(i-1)+j)
        
    if i in range(0,9) and j in range(0,8) and matrix[i][j+1] == 0 :
        n.append(9*i+j+1)
        matrix[i][j+1] = -1
        find_nb(matrix,i,j+1,n)    
    elif i in range(0,9) and j in range(0,8) and matrix[i][j+1] != 0 and matrix[i][j+1] != -1:
        n.append(9*i+j+1)
        
    if i in range(0,8) and j in range(0,9) and matrix[i+1][j] == 0 :
        n.append(9*(i+1)+j)
        matrix[i+1][j] = -1
        find_nb(matrix,i+1,j,n)
    elif i in range(0,8) and j in range(0,9) and matrix[i+1][j] != 0 and matrix[i+1][j] != -1:
        n.append(9*(i+1)+j)
    return n        
 
def set_zero(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == -1:
                matrix[i][j] = 0;
    return matrix
     
o_m, o_v, nb_m, nb_v= creat_mine(10) 



n = find_nb(nb_m,0,0,n)   
m_i = []
m_j = []
for m in n:
    m_i.append(m//9)
    m_j.append(m%9)
    

nb_m = set_zero(nb_m)    
  
a = o_m[:][:]

b = copy.deepcopy(a)


def play(self,i,j,NumberMatrix_o,covermatrix,record):
    step = []
    for x in range(1,12):
        temp = []
        for y in range(1,12):
               temp.append()
        NumberMatrix.append(temp)
    
    for i in range(1,10):
        for j in range(1,10):
            NumberMatrix[i][j] = copy.deepcopy(NumberMatrix_o[i-1][j-1])
        
    for x in range(1,10):
        for y in range(1,10):
            if covermatrix[x][y] != 10:
                step.append([x,y])
    if record[i][j] == 0 :
        covermatrix[i][j] = NumberMatrix[i][j]
        record[i][j] = 1
        if i<1 or i>9 or j<1 or j>9:
            return [step,covermatrix]
     
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
                    self.play(self,a,b,NumberMatrix,covermatrix,record)

    return step,covermatrix
     
        



print(o_m)
print(b)
o_m[0][0] = 5

print(o_m)
print(a)
print(b)
              
