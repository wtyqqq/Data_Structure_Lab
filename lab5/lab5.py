#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lab5.py
@Time    :   2022/06/12 08:49:22
@Author  :   Tianyi Wang
@Version :   1.0
@Contact :   tianyiwang58@gmail.com
@Desc    :   None
'''
class graph():
    def __init__(self,node,edge):
        self.node = node
        self.edge = edge
        self.linktable = []
        for _ in range (node):
            line = input("Please enter the link table: ").split(",")
            self.linktable.append(line)
        print(self.linktable)
        if self.checkLinktable():
            print("The link table is correct!")
        else:
            print("The link table is not correct! Please check!")
    
    def checkLinktable(self):# 检查链接表是否正确
        if len(self.linktable)!=self.node:
            print("The number of nodes is not correct!")
            return False
        count = 0
        for i in self.linktable:
            count+=int(i[1])
        if count!=self.edge:
            print("The number of edges is not correct!")
            return False
        return True

    def dfs(self,visited = None,i=None):# 深度遍历
        if visited == None:# 初始化
            visited=[False]*len(self.linktable)    
            print(i,end=" ")
        visited[i-1]=True # 访问点i
        
        for j in range(2,len(self.linktable[i-1])):# 对i的每一个邻接点进行深度遍历
            if visited[int(self.linktable[i-1][j])-1]==False:# 如果邻接点没有被访问过
                visited[int(self.linktable[i-1][j])-1]=True# 设置邻接点为已访问
                print(int(self.linktable[i-1][j]),end=" ")
                self.dfs(visited,int(self.linktable[i-1][j]))# 递归调用dfs函数

    def bfs(self,i): # 广度遍历
        myqueue=[]# 初始化队列
        myqueue.append(i)
        visited=[False]*len(self.linktable)
        visited[i-1]=True
        while len(myqueue)>0:# 当队列不为空时
            i=myqueue.pop(0)
            print(i,end=" ")
            for j in range(2,len(self.linktable[i-1])):# 对i的每一个邻接点进行广度遍历
                if visited[int(self.linktable[i-1][j])-1]==False:# 如果邻接点没有被访问过
                    myqueue.append(int(self.linktable[i-1][j]))# 将邻接点加入队列
                    #print(int(linktable[i-1][j]))
                    visited[int(self.linktable[i-1][j])-1]=True

def main():
    nodeAndEdge = input('Please enter the number of nodes and edges: ').split(" ")
    node = int(nodeAndEdge[0])
    edge = int(nodeAndEdge[1])
    a = graph(node,edge)
    a.dfs(i=1)
    print("\n")
    a.bfs(i=1)

if __name__ == "__main__":
    main()