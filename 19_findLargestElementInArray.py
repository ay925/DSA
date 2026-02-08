nums=[1,2,3,4,5,33,6,7,8,9,22]
minValue=nums[0]
n=len(nums)
for i in range(n):
    if minValue<nums[i]:
        minValue=nums[i]
    

print(minValue)