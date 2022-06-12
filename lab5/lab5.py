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
    
    def checkLinktable(self):
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

    def dfs(self,visited = None,i=None):
        if visited == None:
            visited=[False]*len(self.linktable)    
        visited[i-1]=True
        for j in range(2,len(self.linktable[i-1])):
            if visited[int(self.linktable[i-1][j])-1]==False:
                visited[int(self.linktable[i-1][j])-1]=True
                self.dfs(visited,int(self.linktable[i-1][j]))

    def bfs(self,i):
        myqueue=[]
        myqueue.append(i)
        visited=[False]*len(self.linktable)
        visited[i-1]=True
        while len(myqueue)>0:
            i=myqueue.pop(0)
            print(i,end=" ")
            for j in range(2,len(self.linktable[i-1])):
                if visited[int(self.linktable[i-1][j])-1]==False:
                    myqueue.append(int(self.linktable[i-1][j]))
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