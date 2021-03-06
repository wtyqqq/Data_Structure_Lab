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


def InfixToPostfix(x):
    """translate infix expression to postfix expression

    Args:
        x (List): the infix expression

    Returns:
        float : the result of postfix expression
    """
    stack1 = [] # stack1 for operator
    stack2 = [] # stack2 for number
    WeightValue = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1} # operator weight
    for i in x: # for each element in the infix expression
        if i.isdigit(): # if the element is a number
            stack2.append(i) # push the number to stack2
        elif i in ['+', '-', '*', '/', '^']: # if the element is an operator
            if stack1 == [] or stack1[-1] == '(': # if stack1 is empty or the last element in stack1 is '('
                stack1.append(i) # push the operator to stack1
            elif WeightValue[i] > WeightValue[stack1[-1]]: # if the weight of the operator is greater than the last element in stack1
                stack1.append(i) # push the operator to stack1
            elif WeightValue[i] <= WeightValue[stack1[-1]]: # if the weight of the operator is less than or equal to the last element in stack1
                while stack1 != [] and WeightValue[i] <= WeightValue[stack1[-1]]: # if the weight of the operator is less than or equal to the last element in stack1
                    stack2.append(stack1.pop())# pop the last element in stack1 and push it to stack2
                stack1.append(i)# push the operator to stack1
        elif i == '(': # if the element is '('
            stack1.append(i) # push the element to stack1
        elif i == ')': # if the element is ')'
            while stack1[-1] != '(': # if the last element in stack1 is not '('
                stack2.append(stack1.pop()) # pop the last element in stack1 and push it to stack2
            stack1.pop() # pop the last element in stack1
    while stack1 != []: # if stack1 is not empty
        stack2.append(stack1.pop()) # pop the last element in stack1 and push it to stack2
    return stack2


def caculateTheResult(operator, num1, num2):
    """caculate the result of the expression

    Args:
        operator (str): the operator of the expression
        num1 (int): the first number of the expression
        num2 (int): the second number of the expression

    Returns:
        float: the result of the expression
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num2 - num1
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num2 / num1
    elif operator == '^':
        return num2**num1
    else:
        return None


def caculatePostfix(x):
    """calculate the result of postfix expression
    
    Args:
        x (List): the postfix expression

    Returns:
        float: the result of postfix expression
    """
    result = [] # result for the result of postfix expression
    post = x
    for i in post: # for each element in postfix expression
        if i.isdigit():# if the element is a number
            result.append(i) # push the number to result
            #print(i,"is a number") 
        else:
            num1 = result.pop()
            num2 = result.pop()
            #print("caculate",int(num1),int(num2),i)
            result.append(caculateTheResult(i, float(num1), float(num2)))
    return result[0]


def caculateInfix(x):
    """calculate the result of infix expression
    
    Args:
        x (List): the infix expression

    Returns:
        float: the result of infix expression
    """
    numberStack = []
    operatorStack = []
    WeightValue = {')': 5, '^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}# operator weight
    for i in x: 
        if i.isdigit(): # if the element is a number
            numberStack.append(i) # push the number to numberStack
        elif i in ['+', '-', '*', '/', '^']: # if the element is an operator
            if operatorStack == [] or WeightValue[i] > WeightValue[
                    operatorStack[-1]]:# if operatorStack is empty or the weight of the operator is greater than the last element in operatorStack
                operatorStack.append(i)
            elif WeightValue[i] <= WeightValue[operatorStack[-1]]:# if the weight of the operator is less than or equal to the last element in operatorStack
                while operatorStack != [] and WeightValue[i] <= WeightValue[
                        operatorStack[-1]]:# if the weight of the operator is less than or equal to the last element in operatorStack
                    number1 = numberStack.pop()# pop the last element in numberStack
                    number2 = numberStack.pop()# pop the last element in numberStack
                    operator = operatorStack.pop()# pop the last element in operatorStack
                    numberStack.append(
                        caculateTheResult(operator, float(number1),
                                          float(number2)))# push the result of caculate to numberStack
                operatorStack.append(i)# push the operator to operatorStack
        elif i == '(':
            operatorStack.append(i)# push the element to operatorStack
        elif i == ')':
            while operatorStack[-1] != '(':# if the last element in operatorStack is not '('
                number1 = numberStack.pop()# pop the last element in numberStack
                number2 = numberStack.pop()# pop the last element in numberStack
                operator = operatorStack.pop()# pop the last element in operatorStack
                numberStack.append(
                    str(caculateTheResult(operator, float(number1),
                                          float(number2))))# push the result of caculate to numberStack
            operatorStack.pop()# pop the last element in operatorStack
    while operatorStack != []: # if operatorStack is not empty
        number1 = numberStack.pop()# pop the last element in numberStack
        number2 = numberStack.pop()# pop the last element in numberStack
        operator = operatorStack.pop()# pop the last element in operatorStack
        #print(caculateTheResult(operator, int(number1), int(number2)))
        numberStack.append(
            str(caculateTheResult(operator, float(number1), float(number2))))# push the result of caculate to numberStack
    return numberStack[0]


if __name__ == '__main__':
    x = input("Please input the infix expression:(' ' between two numbers):")
    processedInput = x.split(' ')
    print("Sovle using postfix expression:")
    print(caculatePostfix(InfixToPostfix(processedInput)))
    print("Sovle using infix expression:")
    print(caculateInfix(processedInput))
