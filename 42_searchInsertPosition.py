nums=[1,3,4,5,6,7,8,9,10,14,18,30]
target=40
n=len(nums)
low=0
ans=n
high=n-1
while(low<=high):
    mid=(low+high)//2
    if(nums[mid]>=target):
        ans=mid
        high=mid-1
    else:
        low=mid+1

print(ans)