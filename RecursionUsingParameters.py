# def func(x,n):
#     if(n==0):
#         return
#     print(x)
#     func(x,n-1)
# func(15,5)

#print 1 to n
def func(i,n):
    if(n<i):
        return
    func(i+1,n)
    print(n-i+1,end=" ")
func(1,20)