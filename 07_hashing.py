# Brute Force Approach
#Time complexity O(n^2)
# Space complexity O(1)

n=[5,3,2,2,1,5,5,7,5,10]
m =[10,101,9,5,67,27,2]

frequancy_dict={}
for i in m:
    count =0
    for j in n:
        if i not in n:
            frequancy_dict[i]=0
        elif(i==j):
            count+=1
            frequancy_dict[i]=count
            
        

print(frequancy_dict)
# Optimal Approach

# Condition 
# 1.1<=n[i]<=10
# 2.n can have 10^8 element
# 3.m can have 10^8 element
#Time complexity O(2*n)≈O(n)
# Space complexity O(11)≈O(1)
n=[5,3,2,2,1,5,5,7,5,10]
m =[10,101,9,5,67,27,2]
hash_list=[0]*11
for i in n:
    hash_list[i]+=1
for j in m:
    if j<1 or j>10:
        print(0,end=" ")
    else:
        print(hash_list[j],end= " ")
print()
# Character hasing
# 1.a<=s[i]<=z
# 2.n can have 10^8 element
# 3.m can have 10^8 element
s="azzcmnseendwwym"
q=["d","m","n","c","~"]
hash_list=[0]*26
for i in s:
    ascii_value=ord(i)
    Index=ascii_value-97
    hash_list[Index]+=1

for j in q:
    ascii_j=ord(j)
    Index=ascii_j-97
    if ascii_j<97 or ascii_j>122:
        print(0,end=" ")
    else:
        print(hash_list[Index],end=" ")



    