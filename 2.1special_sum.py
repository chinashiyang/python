
#Implement a function that takes a natural number 𝑛 as an argument and
#calculates 12 *2+ 22 *3+...+ (𝑛−1)2 *𝑛 sum. Use only one comprehension expression in your solution.
#Asymptotical complexity of the algorithm should be 𝑂(𝑛).
#Note. Name your function calculate_special_sum and save it into a special_sum.py file.
#Example
#assert calculate_special_sum ( 3 ) == 14
imput 'shuru'n
i=0
item=0
calculate_special_sum=0
while (n>i):
  calculate_special_sum=calculate_special_sum+item
  i++
  item=n*[(n+1)**2]
print calculate_special_sum
