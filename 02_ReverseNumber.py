num=5873
revnum=0
while num>0:
    ld=num%10
    revnum*=10
    revnum+=ld
    num//=10
print(f"Revrese number is {revnum}")
