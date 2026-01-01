# Head Recurstion

# i=0
# def name():
#     global i
#     if(i>5):
#         return
#     print("Anupam")
#     i+=1
#     name()
# name()

#Tail Recurstion

i=1
def name():
    global i
    if(i>5):
        return
    i+=1
    name()
    print("Anupam")
name()