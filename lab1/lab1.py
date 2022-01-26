#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Lab1-Josephu.py
@Time    :   2022/01/04 16:31:48
@Author  :   Tianyi Wang
@Version :   1.0
@Contact :   tianyiwang58@gmail.com
@Desc    :   Josephu's Problem for Lab1 solving by python
@Problem :   
设编号为1，2，… m的m个人围坐一圈，从1开始报数，数到n 的那个人出列，它的下一位又从1开始报数，数到n的那个人又出列，依次类推，直到所有人出列为止，由此产生一个出队编号的序列。
---------------------------------------------------------------------------
Suppose that m persons numbered 1, 2, ... m sit in a circle, start counting from 1, and the person who counts to n goes out, and the next one starts counting from 1, and the person who counts to n Dequeue again, and so on, until everyone is dequeued, resulting in a sequence of dequeue numbers.
'''
# here put the import lib


def normalSolution1(m, n):
    '''
    @description: 这个函数实现了实验报告上的顺序存储方法来解决该问题。
    This function implements the sequential storage method on the lab report to solve this problem.
    '''
    if m <= 0 or n <= 0:
        print("The input is invalid!")
        return
    List = [x for x in range(1, m+1)]
    index = 0
    while len(List) > 1:
        counter = 0
        while counter < n-1:
            index = (index + 1) % len(List)
            counter += 1
        print(List[index], end=" ")
        List.pop(index)
        counter = 0
    print(List[0])


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class ringLinkedList:
    '''
    循环链表的实现
    '''

    def __init__(self, value):
        self.head = Node(value)
        self.head.next = self.head

    def insert(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.head = node

    def delete(self):
        if self.head.next == self.head:
            print("The list is empty!")
            return
        else:
            self.head.next = self.head.next.next


def normalSolution2(m, n):
    '''
    @description: 这个函数实现了实验报告上的循环链表方法来解决该问题。
    This function implements the loop linked list method on the lab report to solve this problem.
    '''
    if m <= 0 or n <= 0:
        print("The input is invalid!")
        return
    remainNumber = m
    List = ringLinkedList(1)
    for i in range(2, m+1):
        List.insert(i)
    List.head = List.head.next
    while remainNumber > 1:
        counter = 1
        while counter < n-1:
            List.head = List.head.next
            counter += 1
        print(List.head.next.value, end=" ")
        List.delete()
        remainNumber -= 1
        List.head = List.head.next
    print(List.head.next.value)


def quickSolution(m, n):
    '''
    Q: 如果只关心最后出列的人员，不考虑数据结构要求，是否还有更快的算法？
    A: 有，使用数学方法.
    '''
    if m == 0:
        return 0
    else:
        return (quickSolution(m-1, n) + n-1) % m+1

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    # This is normal solution 1
    print("Normal Solution 1:")
    normalSolution1(m, n)
    # This is normal solution 2
    print("Normal Solution 2:")
    normalSolution2(m, n)
    # This is a quick solution
    print("Quick Solution:")
    print(quickSolution(m, n))
