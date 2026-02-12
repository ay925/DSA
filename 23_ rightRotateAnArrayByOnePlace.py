nums=[7,3,2,4,5,6,8,0,8,2,3]
n=len(nums)
temp=nums[n-1]
for i in range(n-1,-1,-1):
    nums[i]=nums[i-1]
nums[0]=temp
print(nums)