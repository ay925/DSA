n=1634
num=n
result=0
num_len=len(str(n))
while num>0:
    ld=num%10
    result+=(ld**num_len)
    num=num//10
if result==n:
    print("This number is Armstrong Number ")
else:
    print("This number is not Armstrong Number ")