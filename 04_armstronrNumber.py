number=153
n=number
result=0
l=len(str(number))
while n>0:
    ld=n%10
    result+=(ld**l)
    n//=10
if(number==result):
    print("This is a Armstrong Number")
else:
    print("This is not a Armstrong Number")