#Brute force solution 
"""
nums=[3,0,1]
n=len(nums)
result=0 
for i in range(n):
    if i not in nums:
        result =i
print(result)    
"""
#  Better solution
"""
nums=[3,0,1]
n=len(nums)
freq_dict={}
result=0
for i in range(n):
    freq_dict[i]=0

for num in nums:
    freq_dict[num]=1

for k,v in freq_dict.items():
    if v==0:
        result=k

print(result)
"""  

#  Optimal solution
nums=[3,0,1]
n=len(nums)
sumOfNums=0
sumOfIteration=0

for i in range(n+1):
    sumOfIteration+=i
for j in nums:
    sumOfNums+=j
result = sumOfIteration-sumOfNums
print(result)