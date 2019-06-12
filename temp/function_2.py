# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:46:58 2017

@author: Guanchao
"""

def Mt(mine,length):
    from random import randint
    OriginMatrix=[]#保存原始地雷矩阵
    NumberMatrix=[]#保存计算后的数字矩阵
    StateMatrix=[]#保存矩阵的显示状态

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
        
    for i in range(0,length+2):
        temp=[]
        for j in range(0,length+2):
            temp.append(0);
        StateMatrix.append(temp)
    
     


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
    
    for i in OriginMatrix:
        print(i) #打印 OriginMatrix，矩阵外圈加了一圈零
    
    print('\n')
    
    
    for i in range(1,length+1):
        for j in range(1,length+1):
            if OriginMatrix[i][j]==0:
                NumberMatrix[i][j]=OriginMatrix[i-1][j-1]+OriginMatrix[i][j-1]+OriginMatrix[i-1][j]+OriginMatrix[i+1][j]+OriginMatrix[i-1][j+1]+OriginMatrix[i][j+1]+OriginMatrix[i+1][j+1]
            else:
                NumberMatrix[i][j]=9#雷标记为9
            
    
    for i in NumberMatrix:
        print(i) #打印 NumberMatrix，矩阵外圈加了一圈零

#接下来 输入一个点，然后输出一个结果的函数
        
    def Pt(i,j):# i应该在1-length之间，j也应该在1-length之间（i,j)就是坐标
        if NumberMatrix[i][j]==9:#踩到雷
            print("game over")
        elif NumberMatrix[i][j]!=0:#踩到有数字的点
            StateMatrix[i][j]=NumberMatrix[i][j]
        else:#踩到的是0
            StateMatrix[i][j]='*'#*表示此处的周围八个点没有雷
            if StateMatrix[i-1][j-1]==0 and i-1>=1 and j-1>=1 and i-1<=length and j-1<=length:
                Pt(i-1,j-1)#这里是说，如果这个邻点之前没有做过运算，且在我们的这个定义域范围里，那么，就要递归做一遍运算。
            if StateMatrix[i-1][j]==0 and i-1>=1 and j>=1 and i-1<=length and j<=length:
                Pt(i-1,j)
            if StateMatrix[i-1][j+1]==0 and i-1>=1 and j+1>=1 and i-1<=length and j+1<=length:
                Pt(i-1,j+1)
            if StateMatrix[i][j-1]==0 and i>=1 and j-1>=1 and i<=length and j-1<=length:
                Pt(i,j-1)
            if StateMatrix[i][j+1]==0 and i>=1 and j+1>=1 and i<=length and j+1<=length:
                Pt(i,j+1)
            if StateMatrix[i+1][j-1]==0 and i+1>=1 and j-1>=1 and i+1<=length and j-1<=length:
                Pt(i+1,j-1)
            if StateMatrix[i+1][j]==0 and i+1>=1 and j>=1 and i+1<=length and j<=length:
                Pt(i+1,j)
            if StateMatrix[i+1][j+1]==0 and i+1>=1 and j+1>=1 and i+1<=length and j+1<=length:
                Pt(i+1,j+1)
        
        for i in StateMatrix:
            print(i) #打印 StateMatrix，矩阵外圈加了一圈零 
        
    
    
    
    
    
    
    
    