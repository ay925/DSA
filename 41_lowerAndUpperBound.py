# Lower Bound
nums=[1,2,2,2,3,4,5,6,7,8,9,10,14,18,30]
target=2
n=len(nums)
low=0
lb=n
high=n-1
while(low<=high):
    mid=(low+high)//2
    if(nums[mid]>=target):
        lb=mid
        high=mid-1
    else:
        low=mid+1

print(lb)

# Upper bound
nums=[1,2,2,2,3,4,5,6,7,8,9,10,14,18,30]
target=2
n=len(nums)
low=0
ub=n
high=n-1
while(low<=high):
    mid=(low+high)//2
    if(nums[mid]>target):
        ub=mid
        high=mid-1
    else:
        low=mid+1

print(ub)