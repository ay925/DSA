# Brute force solution
nums=[-2,1,-3,4,-1,2,3,-5,4]
n=len(nums)
total=nums[0]
maxi=float("-inf")
for i in range(n):
    for j in range(i+1,n):
        total+=nums[j]
    if total>maxi:
        maxi=total
    total=nums[i]

print(maxi)