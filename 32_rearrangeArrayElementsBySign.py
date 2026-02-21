# Brute force apporoach
nums=[5,10,-3,-1,-10,6]
n=len(nums)
positive=[]
negative=[]
result=[]
i=0
for i in range(n):
    if nums[i]>0:
        positive.append(nums[i])
    else:
        negative.append(nums[i])
m=len(positive)

for j in range(m):
    result.append(positive[j])
    result.append(negative[j])

print(result)

# Optimal approach
nums=[5,10,-3,-1,-10,6]
m=len(nums)
result=[0]*m
p=0
n=1
for i in range(m):
    if nums[i]>0:
        result[p]=nums[i]
        p+=2
    else:
        result[n]=nums[i]
        n+=2

print(result)

