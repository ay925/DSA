nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=len(nums)

for i in range(n-1):
    for j in range(i+1,n):
        nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    
for i in range(n):
    nums[i].reverse()

for i in range(n):
    for j in range(n):
        print(nums[i][j],end=" ")
    print()