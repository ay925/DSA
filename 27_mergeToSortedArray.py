nums1=[1,1,1,2,4,6]
nums2=[1,2,3,6,7,8,9,10]
n=len(nums1)
m=len(nums2)
merge_arr=[]
freq_dict={}
for i in range(n):
    freq_dict[nums1[i]]=0

for j in range(m):
    freq_dict[nums2[j]]=0    

for k in freq_dict.keys():
    merge_arr.append(k)
merge_arr.sort()    
print(merge_arr)