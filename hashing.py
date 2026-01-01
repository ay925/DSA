# Brute force approch
# m=[10,111,1,9,5,67,2]
# n=[5,3,2,2,1,5,5,7,5,10]
# d={}
# for i in m:
#     count=0
#     for j in n:
#         if i==j:
#             count+=1
#     d[i]=count
# print(d)

# Optimal approch
# m=[10,111,1,9,5,67,2]
# n=[5,3,2,2,1,5,5,7,5,10]
# d={}
# hash_list=[0]*11
# for i in n:
#     hash_list[i]+=1
# # print(hash_list)
# for i in m:
#     if i<0 or i>10:
#         # print(0)
#         pass
#     else:
#         # print(hash_list[i])
#         d[i]=hash_list[i]
# print(d)

#Using Dict
# m=[10,111,1,9,5,67,2]
# n=[5,3,2,2,1,5,5,7,5,10]
# freq_dict={}
# result={}
# for i in n:
#     freq_dict[i]=freq_dict.get(i,0)+1
# for x in m:
#     result[x] = freq_dict.get(x, 0)
# print(result)


# Character Hashing
s="abbcddaddbef"
q=["d","a","y","x"]
hash_list=[0]*27
result={}
for i in s:
    ascii_value=ord(i)
    hash_list[ascii_value-97]+=1
for i in q:
    ascii_value=ord(i)
    result[ascii_value-97]=hash_list[ascii_value-97]
    (result.keys())
print(result)

    
    
        