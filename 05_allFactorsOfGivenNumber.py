# Brute Force Approach
#Time complexity O(n)
# Space complexity O(k)
number=25
factor_list=[]
for i in range(1,number+1):
    if(number%i==0):
        factor_list.append(i)

print(factor_list)


# Better Approach
# Time complexity O(n/2)≈O(n)
# Space complexity O(k)
number=25
factor_list=[]
for i in range(1,number//2+1):
    if(number%i==0):
        factor_list.append(i)
factor_list.append(number)
print(factor_list)


# Optimal Approach
# Time complexity O(sqrt(n)
# Space complexity O(k)
import math
number=25
factor_list=[]
sqrt_num=math.sqrt(number)
for i in range(1,int(sqrt_num)+1):
    if(number%i==0):
        factor_list.append(i)
        if((i!=(number//i))):
            factor_list.append(number//i)
print(factor_list)
