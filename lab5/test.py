# coding=utf-8
from queue import Queue

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    """
    根据邻接表创建有向图
    """
    def __init__(self,adj_list):
        self.adj_list = adj_list
        self.peaks = []
        self.visited = [False]*len(self.adj_list)
    def bfs(self):
        """
        广度优先遍历，时间复杂度O(n)
        :return:
        """
        
        queue = Queue()
        self.visited = [False]*len(self.adj_list) # 存储顶点的访问状态
        queue.put(0) # 默认从邻接表第0个邻接点开始
        self.visited[0] = True
        self.peaks = self.adj_list[0][0]
        while not queue.empty():
            index = queue.get() # 出队
            for i in self.adj_list[index][1]:
                if not self.visited[i]: # 判断是否被访问
                    self.visited[i] = True
                    queue.put(i) # 入队
                    self.peaks.append(adj_list[i][0])
            print(self.visited)
        return self.peaks
    
    def dfs(self,node):
        """
        递归调用深度优先遍历，时间复杂度O(n)
        :return:
        """
        self.visited[node] = True
        self.peaks.append(self.adj_list[node][0])
        for index in self.adj_list[node][1]:
            # 判断该节点是否被访问过
            if not self.visited[index]:
                self.dfs(index)
            # print(index)
        return self.peaks
if __name__ == '__main__':
    # 邻接表表示有向图
    adj_list = [
        ("a",[2,5,4]),
        ("b",[1,3,5]),
        ("c",[2,4]),
        ("d",[1,5,3]),
        ("e",[4,1,2]),
        ]
    solution = Solution(adj_list)
    # print(solution.bfs())
    print(solution.dfs(0))

