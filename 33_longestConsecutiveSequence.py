# Brute force approach
nums=[1,99,101,98,2,5,3,100]
n=len(nums)
max_count=0
j=0
for i in range(n):
    num=nums[i]
    count=1
    while num+1 in nums:
        count+=1
        num+=1
    if count>max_count:
        max_count=count
print(max_count)

# Optimal approach
nums=[1,99,101,98,2,5,3,100]
nums.sort()
n=len(nums)
count=0
last_smaller=float("-inf")
langest=0
for i in range(n):
    num=nums[i]
    if num-1 == last_smaller:
        count+=1
        last_smaller=num
    elif num-1 !=last_smaller:
        count=1
        last_smaller=num
    if count>langest:
        langest=count

print(langest)

