# Brute force solution
nums=[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
maxi=float("-inf")
for i in range(n):
    total=0
    for j in range(i,n):
        total+=nums[j]
        if total>maxi:
            maxi=total

print(maxi)

#Optimal Solution
nums=[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
total=0
maxi=float("-inf")
a=[]
for i in range(n):
    total+=nums[i]
    if total>maxi:
        maxi=total
    if total<0:
        total=0
    a.append(maxi)
print(maxi)
print(a)
