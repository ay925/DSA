# Brute force Approach
nums=[7,6,4,3,1]
n=len(nums)
max_profit=0
for i in range(n):
    for j in range(i+1,n):
        profit=nums[j]-nums[i]
        if(max_profit<profit):
            max_profit=profit
            
            
print(max_profit)

# Optimal Approach

nums=[7,1,5,3,6,4]
n=len(nums)
buy=nums[0]
profit=0
for i in range(n):
    if nums[i]<buy:
        buy=nums[i]
    if profit<nums[i]-buy:
        profit=nums[i]-buy    
        
    
print(profit)
