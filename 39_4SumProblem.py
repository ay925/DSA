# Brute force 

nums=[1,0,-1,0,-2,2,8,6,4,3,2,4,5,6,7,78,8,9,0,9,8,78,87,7,7,6,6,5,5,45,4,4,4,4,4,4,4,4,4,4,5]
n=len(nums)
target=0
result=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if nums[i]+nums[j]+nums[k]+nums[l]==target:
                    temp=[nums[i],nums[j],nums[k],nums[l]]
                    temp.sort()
                    if temp not in result:
                        result.append(temp)

print(result)

# Optimal 

nums=[1,0,-1,0,-2,2,8,6,4,3,2,4,5,6,7,78,8,9,0,9,8,78,87,7,7,6,6,5,5,45,4,4,4,4,4,4,4,4,4,4,5]
nums.sort()
n=len(nums)
target=0
result=[]

for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,n):
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        k=j+1
        l=n-1
        while k<l:
            total=nums[i]+nums[j]+nums[k]+nums[l]
            if total==target:
                result.append([nums[i],nums[j],nums[k],nums[l]])
                k+=1
                l-=1
                while k<l and nums[k]==nums[k-1]:
                    k+=1
                while l>k and nums[l]==nums[l+1]:
                    l-=1
            elif total<target:
                k+=1
            else:
                l-=1


print(result)
            




