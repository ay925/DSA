# num_list=[1,2,3,4,5,5,5,6,6,7,8,9,0,11,1,1,1,2,3]
# fre_dict={}
# for n in num_list:
#     if n in fre_dict:
#         fre_dict[n]+=1
#     else:
#         fre_dict [n]=1   
# print(fre_dict)

# Anthor way
num_list=[1,2,3,4,5,5,5,6,6,7,8,9,0,11,1,1,1,2,3]
fre_dict={}
for n in num_list:
    fre_dict[n]=fre_dict.get(n,0)+1
print(fre_dict)