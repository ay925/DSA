nums=[3,5,6,8,9,10,12]
n= len(nums)
result=True
for i in range(1,n):
    if(nums[i-1]>nums[i]):
        result=False
        break
print(result)