nums=[1,2,3,4,5,6,7,8,9,10,14,18,30]
target=30
n=len(nums)
ans=-1
low=0
high=n-1
while(low<=high):
    mid=(low+high)//2
    if(nums[mid]==target):
        ans=mid
        break
    elif(nums[mid]<target):
        low=mid+1
    else:
        high=mid-1
    
print(ans)
