def func(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return func(n-1)+func(n-2)
# a=0
# b=1
# for i in range(10):
#     print(a,end=" ")
#     a=b
#     b=a+b
n = 10   # number of terms
a=0
b=1
c=0

for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c


