# def func(sum,i,n):
#     if(i>n):
#         return
#     return func(sum+i,i+1,n)

# print(func(0,0,4))


def sum(n):
    if(n<=0):
        return 0
    return n+sum(n-1)


print(sum(5))