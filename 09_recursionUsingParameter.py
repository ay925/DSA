# def func(x,n):
#     if(n<=0):
#         return
#     print(x)
#     func(x,n-1)

# func(3,10)


# Print 1 to n
# Head Recursion
# def func(x,n):
#     if(x>n):
#         return
#     print(x)
#     func(x+1,n)

# func(1,10)



# Print 1 to n
# Tail Recursion
def func(x,n):
    if(x>n):
        return
    func(x+1,n)
    print(n-(x-1))

func(1,10)

