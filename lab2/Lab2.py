#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Lab2.py
@Time    :   2022/04/17 08:35:44
@Author  :   Tianyi Wang
@Version :   1.0
@Contact :   tianyiwang58@gmail.com
@Desc    :   一个处理多项式相加的程序。

# 输入样例：
3 4 -5 2  6 1  -2 0
5 20  -7 4  3 1



# 输出样例：
15 24 -25 22 30 21 -10 20 -21 8 35 6 -33 5 14 4 -15 3 18 2 -6 1
5 20 -4 4 -5 2 9 1 -2 0
'''

# here put the import lib


def solution1Add(l1, l2):
    '''
    将两个以列表形式存储的多项式相加
    '''
    res = []
    counts_l1 = 0
    counts_l2 = 0
    while counts_l1 <= len(l1) - 1 and counts_l2 <= len(l2) - 1:
        if l1[counts_l1][1] < l2[counts_l2][1]:
            res.append(l2[counts_l2])
            counts_l2 += 1
        elif l1[counts_l1][1] == l2[counts_l2][1]:
            res.append([l1[counts_l1][0] + l2[counts_l2][0], l1[counts_l1][1]])
            counts_l1 += 1
            counts_l2 += 1
        else:
            res.append(l1[counts_l1])
            counts_l1 += 1
    if counts_l1 <= len(l1) - 1:
        res.append(l1[counts_l1])
        counts_l1 += 1
    if counts_l2 <= len(l2) - 1:
        res.append(l2[counts_l2])
        counts_l2 += 1
    for i in range(len(res)-1):
        if res[i][0] == 0:
            res.pop(i)
    return res


def ploynomialSort(l):
    '''
    对多项式按照降幂进行排序
    '''
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i][1] < l[j][1]:
                l[i], l[j] = l[j], l[i]
    return l


def solution1(l1, l2):
    # 这里的输入可以打乱顺序，后面做了降幂排序
    l1 = [[l1[i], l1[i + 1]] for i in range(0, len(l1) - 1, 2)]
    ploynomialSort(l1)
    l2 = [[l2[i], l2[i + 1]] for i in range(0, len(l2) - 1, 2)]
    ploynomialSort(l2)
    #print(l1)
    #print(l2)
    res1 = solution1Add(l1, l2)
    print("The result of adding the two ploynomial is ", res1)


class Node:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None
    def get_data(self):
        return [self.coef, self.exp]

class List:
    def __init__(self, head):
        self.head = head

    def addNode(self, node):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def printLink(self, head):
        res = []
        while head is not None:
            res.append(head.get_data())
            head = head.next
        return res


def adds(l1, l2):
    p1 = l1.head
    p2 = l2.head
    addRes = []
    while (p1 is not None) and (p2 is not None):
        tmp1_exp = p1.exp
        tmp2_exp = p2.exp
        if tmp1_exp == tmp2_exp:
            addRes.append([p1.coef + p2.coef, p1.exp])
            p1 = p1.next
            p2 = p2.next
        if tmp1_exp > tmp2_exp:
            addRes.append([p1.coef, p1.exp])
            p1 = p1.next
        if tmp1_exp < tmp2_exp:
            addRes.append([p2.coef, p2.exp])
            p2 = p2.next
    while p1 is not None:
        addRes.append([p1.coef, p1.exp])
        p1 = p1.next
    while p2 is not None:
        addRes.append([p2.coef, p2.exp])
        p2 = p2.next
    for i in range(len(addRes)-1):
        if addRes[i][0] == 0:
            addRes.pop(i)
    return addRes


def muls(l1, l2):
    p1 = l1.head
    p2 = l2.head
    mulRes = []
    while p1 is not None:
        tmp1 = p1.get_data()
        while p2 is not None:
            tmp2 = p2.get_data()
            mulRes.append([tmp1[0] * tmp2[0], tmp1[1] + tmp2[1]])
            p2 = p2.next
        p2 = l2.head
        p1 = p1.next
    #处理只出现了一次的情况
    exps = []
    for item in mulRes:
        if item[1] not in exps:
            exps.append(item[1])
    # 这里处理的事如果出现了两个相同的项，那么就相加
    d = {}
    for item in mulRes:
        if item[1] not in d.keys():
            d[item[1]] = 0
        d[item[1]] += item[0]

    d = sorted(d.items(), key=lambda x: x[0], reverse=True)

    res2 = []
    for item in d:
        # 如果多项式中出现抵消，即系数为0需要删除
        if item[1] != 0:
            res2.append(item[1])
            res2.append(item[0])
    # 如果最后出现空数组需要输出0 0
    if len(res2) == 0:
        return [0, 0]
    return res2

def sortInput(l):
    l = [[l[i], l[i + 1]] for i in range(0, len(l) - 1, 2)]
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i][1] < l[j][1]:
                l[i], l[j] = l[j], l[i]
    res = []
    for item in l:
        res.append(item[0])
        res.append(item[1])
    return res

def solution2(a1, a2):
    # a1 a2是两个多项式的列表
    # 先处理一下我们的输入
    a1 = sortInput(a1)
    a2 = sortInput(a2)
    #print(a1)
    #print(a2)
    # 变为链表
    if len(a1) != 0:
        head1 = Node(a1[0], a1[1])
        l1 = List(head1)
        if len(a1) > 2:
            for i in range(int(len(a1)/2) - 1):
                node = Node(a1[(i + 1)*2], a1[(i + 1) * 2 + 1])
                l1.addNode(node)
    #print("The first ploynomial is ", l1.printLink(l1.head))
    if len(a2) != 0:
        head2 = Node(a2[0], a2[1])
        l2 = List(head2)
        if len(a2) > 2:
            for i in range(int(len(a2)/2) - 1):
                node = Node(a2[(i + 1) * 2], a2[(i + 1) * 2 + 1])
                l2.addNode(node)
    #print("The second ploynomial is ", l2.printLink(l2.head))
    # 考虑链表长度进行运算
    if len(a1) == 0 and len(a2) == 0:  # 都为0，则输出都为0
        print("The result of adding the two ploynomial is ", [0, 0])
        print("The result of multiplying the two ploynomial is ", [0, 0])
    elif len(a1) == 0 and len(a2) > 0:  # 一个为0，另一个为多项式
        print("The result of adding the two ploynomial is ", adds(l1,l2))
        print("The result of multiplying the two ploynomial is ", [0,0])
    elif len(a2) == 1 and len(a1) > 1: # 一个为多项式，另一个为0
        print("The result of adding the two ploynomial is ", adds(l1,l2))
        print("The result of multiplying the two ploynomial is ", muls(l1,l2))
    else:  # 都为多项式
        print("The result of adding the two ploynomial is ", adds(l1,l2))
        print("The result of multiplying the two ploynomial is ", muls(l1,l2))
def main():
    l1 = list(map(int, input("Please input the first Polynomial:").split()))
    # 将l1的系数和指数存为一个元素的列表 第一个为系数 第二个为指数
    l2 = list(map(int, input("Please input the second Polynomial:").split()))
    # 解法1：使用python自带的字典解决
    print("##################solution 1######################")
    solution1(l1, l2)
    # 解法2：使用链表解决
    print("##################solution 2######################")
    solution2(l1, l2)

if __name__ == '__main__':
    main()