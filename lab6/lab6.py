#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lab6.py
@Time    :   2022/06/19 09:19:43
@Author  :   Tianyi Wang
@Version :   1.0
@Contact :   tianyiwang58@gmail.com
@Desc    :   None
'''

# here put the import lib

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
 
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
  
# 快速排序函数
def quick_sort(lists,i,j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists

def Bucket_Sort(array, bucketsize):
    minValue = min(array)
    maxValue = max(array)
    res = []
    bucketcount = (maxValue - minValue + 1) // bucketsize
    bucket_lists = [[] for i in range(bucketcount+1)]
    
    for i in array:
        bucket_index = (i - minValue) // bucketsize
        bucket_lists[bucket_index].append(i)
    # 桶内排序
    for j in bucket_lists:
        quick_sort(j, 0, len(j)-1)    

    for j in bucket_lists:
        if len(j) != 0:
            res.extend(j)
    return res

def main():
    '''str = input("请输入待排序的数字序列（用空格分隔）")
    numList = []
    for i in str.split(" "):
        numList.append(int(i))
    '''
    numList = [5,4,3,2,1]
    print("原始序列：", numList)
    print("冒泡排序：", bubbleSort(numList))
    print("快速排序：", quick_sort(numList, 0, len(numList)-1))
    print("桶排序：", Bucket_Sort(numList, 2 ))
if __name__ == '__main__':
    main()