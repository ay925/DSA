nums=[1,4,5,6,8,9,10,11,15,20]

n=len(nums)
ans=-1
low=0
high=n-1
target=15

while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        ans=mid
        break
    elif nums[mid]<=nums[high]:
        if nums[mid]<=target<=nums[high]:
            low=mid+1
        else:
            high=mid-1
    else:
        if nums[low]<=target<=nums[mid]:
            high=mid-1
        else:
            low=mid+1


print(ans)