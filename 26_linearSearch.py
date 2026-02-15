nums=[1,2,4,5,8,9,0,6,5,3,2,2,4,6,7,8,9,9]

target=1
n=len(nums)
for i in range(n):
    if nums[i]==target:
        print(i)
        break