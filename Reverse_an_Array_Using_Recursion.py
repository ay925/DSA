# def func(x,left,right):
#     if(left>=right):
#         return x
#     x[left],x[right]=x[right],x[left]
#     return func(x,left+1,right-1)
# a=func([1,2,3,4,5,6,7],0,6)
# print(a)

# h.w
x=[1,2,3,4,5,6,7]
left=0
right=6
while left<=right:
    x[left],x[right]=x[right],x[left]
    left+=1
    right-=1
print(x)