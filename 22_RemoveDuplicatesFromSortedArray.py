# nums=[1,1,1,2,3,4,4,7,9,9,9,10]
# freq_dict={}
# j=0
# for i in nums:
#     freq_dict[i]=0

# j=0     
# for k in freq_dict:
#     nums[j]=k
#     j+=1
# print(nums)



nums=[1,1,1,2,3,4,4,7,9,9,9,10]
n=len(nums)
i=j=0
while(j<n):
    if nums[i]!=nums[j]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
         
    j+=1
print(nums)