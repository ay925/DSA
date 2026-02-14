nums=[1,0,2,4,3,0,0,3,5,1]
n=len(nums)
temp=[]
for i in range(n):
    if(nums[i]!=0):
        temp.append(nums[i])
m=len(temp)
for j in range(m):
    nums[j]=temp[j]

for k in range(m,n):
    nums[k]=0
print(nums)