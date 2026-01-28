# def greet():
#     print("hello Anupam")
#     greet()

# greet()




# Head Recursion
#Time complexity O(n)
# Space complexity O(n)
count=1
def greet():
    global count
    print("hello anupam")
    if(count>=4):
        return
    count+=1
    greet()

# greet()

# Tail Recursion
#Time complexity O(n)
# Space complexity O(n)
count=1
def greet2():
    global count
    if(count>=4):
        return
    count+=1
    greet()
    print("hello anupam")
greet2()