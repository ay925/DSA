nums=[55,32,97,55,45,32,88,21]
largest=nums[0]
seclargest=nums[0]
n= len(nums)
for i in range(n):
    if(largest<nums[i]):
        seclargest=largest
        largest=nums[i]
    if(seclargest<nums[i] and nums[i]!=largest):
        seclargest=nums[i]
print(seclargest)