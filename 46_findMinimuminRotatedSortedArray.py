nums=[4,5,6,7,0,1,2]

n=len(nums)
mini=nums[0]
low=0
high=n-1

while low<=high:
    mid=(low+high)//2
    if nums[mid]<=nums[high]:
        mini=min(mini,nums[mid])
        high=mid-1
    else:
        mini=min(mini,nums[low])
        low=mid+1
print(mini)