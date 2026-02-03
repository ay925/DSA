nums=[5,4,6,8,3,9,1,7,4]
n=len(nums)
for i in range(n):
    minindex=i
    for j in range(i+1,n):
        if nums[minindex]>nums[j]:
            minindex=j
    nums[i],nums[minindex]=nums[minindex],nums[i]    
print(nums)