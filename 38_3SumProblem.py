# Brote force approach
arr=[0,1,1]
n=len(arr)
hash_list=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]==0:
                temp=[arr[i],arr[j],arr[k]]
                temp.sort()
                if temp not in hash_list:
                    hash_list.append(temp)
print(hash_list)

# Optimal apparoach
arr=[0,1,1]
n=len(arr)
hash_list=[]
a=n//3
count=1
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]-(arr[i]+arr[j])==0:
            temp=[arr[i],arr[j],-(arr[i]+arr[j])]
            temp.sort()
            if(count<=a):
                if temp not in hash_list:
                    hash_list.append(temp)
                    count+=1
            else:
                break
print(hash_list)