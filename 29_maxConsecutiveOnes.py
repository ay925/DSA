nums=[1,0,1,0,0,1,1,1,1,0,1,1]  
result=0
a=0
n=len(nums)
for i in range(n):
    if nums[i]==1:
        a+=1
    else:
        if(a>result):
            result=a
        a=0
if(a>result):
    result=a
print(result)