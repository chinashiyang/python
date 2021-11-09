import numpy as np
import pandas as pd

#接收数据
nums1 = input()
nums2 = input()
num=[]

#合并列表
for item in nums1:
    num.append(item)
    
for item in nums2:
    num.append(item)    
#打印输出测试
print(num)


#冒泡排序
n = len(num)
for i in range(n-1):
    for j in range(0,n-i-1):
        if num[j]>num[j+1]:
            num[j], num[j+1] = num[j+1],num[j]

        
# #删除空元素
while ' ' in num:  
    num.remove(' ')
print(num)