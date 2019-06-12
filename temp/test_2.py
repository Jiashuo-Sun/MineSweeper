#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:50:28 2017

@author: pc
"""

def Mt(mine):
    length=9
    from random import randint
    OriginMatrix=[]#保存原始地雷矩阵
    NumberMatrix=[]#保存计算后的数字矩阵


    for i in range(0,length+2):
        temp=[]
        for j in range(0,length+2):
            temp.append(0);
        OriginMatrix.append(temp)
         
    for i in range(0,length+2):
        temp=[]
        for j in range(0,length+2):
            temp.append(0);
        NumberMatrix.append(temp)
        
     


    for i in range(0,mine):
        x=randint(1,length)
        y=randint(1,length)
        if OriginMatrix[x][y]==0:
            OriginMatrix[x][y]=1
        else:
            while OriginMatrix[x][y]==1:
                x=randint(1,length)
                y=randint(1,length)
                if OriginMatrix[x][y]!=1:
                    OriginMatrix[x][y]=1
                    
                    break
    
  
    
    for i in range(1,length+1):
        for j in range(1,length+1):
            if OriginMatrix[i][j]==0:
                NumberMatrix[i][j]=OriginMatrix[i-1][j-1]+OriginMatrix[i][j-1]+OriginMatrix[i-1][j]+OriginMatrix[i+1][j]+OriginMatrix[i-1][j+1]+OriginMatrix[i][j+1]+OriginMatrix[i+1][j+1]+OriginMatrix[i+1][j-1]
            else:
                NumberMatrix[i][j]=9#雷标记为9
    
    for i in range(length+2):
        NumberMatrix[0][i] = 11
        NumberMatrix[length+1][i] = 11
        NumberMatrix[i][0] =11
        NumberMatrix[i][length+1] =11
    
    return NumberMatrix

def mt():
    covermatrix = []
    record = []
    for i in range(0,11):
        tem1 = []
        tem2 = []
        for j in range(0,11):
            tem1.append(0);
            tem2.append(10)
        covermatrix.append(tem2)
        record.append(tem1)
    return covermatrix, record
    
def play(i,j,NumberMatrix,covermatrix,record):
    step = []
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
                    play(a,b,NumberMatrix,covermatrix,record)
        
    return [step,covermatrix]
    
        
def coord(Matrix):
    step = []
    for x in range(1,10):
        for y in range(1,10):
            if Matrix[x][y] != 10:
                step.append([x-1,y-1])
    return step
