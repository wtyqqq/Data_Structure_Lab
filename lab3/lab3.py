#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lab3.py
@Time    :   2022/05/07 19:35:38
@Author  :   Tianyi Wang
@Version :   1.0
@Contact :   tianyiwang58@gmail.com
@Desc    :   None
'''


from unittest import result


def InfixToPostfix(x):
    stack1 = []
    stack2 = []
    WeightValue = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    for i in x:
        if i.isdigit():
            stack2.append(i)
        elif i in ['+', '-', '*', '/']:
            if stack1 == [] or stack1[-1] == '(':
                stack1.append(i)
            elif WeightValue[i] > WeightValue[stack1[-1]]:
                stack1.append(i)
            elif WeightValue[i] <= WeightValue[stack1[-1]]:
                while stack1 != [] and WeightValue[i] <= WeightValue[
                        stack1[-1]]:
                    stack2.append(stack1.pop())
                stack1.append(i)
        elif i == '(':
            stack1.append(i)
        elif i == ')':
            while stack1[-1] != '(':
                stack2.append(stack1.pop())
            stack1.pop()
    while stack1 != []:
        stack2.append(stack1.pop())
    return stack2


def caculateTheResult(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num2 - num1
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num2 / num1
    else:
        return None

def caculatePostfix(x):
    result = []
    post = x
    for i in post:
        if i.isdigit():
            result.append(i)
            #print(i,"is a number")
        else:
            num1 = result.pop()
            num2 = result.pop()
            #print("caculate",int(num1),int(num2),i)
            result.append(caculateTheResult(i, int(num1),int(num2)))
    return result[0]

if __name__ == '__main__':
    a = '1+((2+3)*4)-5'
    b = InfixToPostfix(a)
    #print(b)
    print(caculatePostfix(b))