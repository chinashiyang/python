import numpy as np
import pandas as pd

nums1 = input()
nums2 = input()
num=[]
for item in nums1:
    num.append(item)
    
for item in nums2:
    num.append(item)    
print(num)
n = len(num)
for i in range(n-1):
    for j in range(0,n-i-1):
        if num[j]>num[j+1]:
            num[j], num[j+1] = num[j+1],num[j]
while ' ' in num:  
    num.remove(' ')
print(num)
