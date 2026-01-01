# Worst Solution
# n=2
# factor_list=[]
# for i in range(1,n+1):
#     if(n%i==0):
#         factor_list.append(i)
# print(factor_list)

# Better Solution
# n=2
# factor_list=[]
# for i in range(1,n//2+1):
#     if(n%i==0):
#         factor_list.append(i)
# factor_list.append(n)
# print(factor_list)

# Optimal Solution
from math import sqrt
n=56676
factor_list=[]
for i in range(1,int(sqrt(n))+1):
    if(n%i==0):
        factor_list.append(i)
        also_factor=n//i
        if i!=also_factor:
            factor_list.append(also_factor)
factor_list.sort()
print(factor_list)