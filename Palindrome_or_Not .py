x="ABCDEFEDCBA"
l=0
r=len(x)-1
# check=False
# while l<=r:
#     if x[l]==x[r]:
#         check=True
#     else:
#         check=False
#         break
#     l+=1
#     r-=1
# if check==True:
#     print("Palndrom")
# else:
#     print("Not palandrom")

def func(x,l,r):
    if l>=r:
            return "Palandrom"
    if x[l]!=x[r]:
            return "Not palandrom"
    return func(x,l+1,r-1)
print(func(x,l,r))

    

    
        
