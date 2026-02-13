def reverse(nums,left,right):
    while(left<=right):
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right -=1
  
nums=[1,2,3,4,5,6,7,8,9]
n=len(nums)
t=3
k=t%n
reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)
print(nums)