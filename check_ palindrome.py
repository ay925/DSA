n=121
num=n
revn=0
while num>0:
    ld=num%10
    num=num//10
    revn=(revn*10)+ld
if(n==revn):
    print("this is a palendrom")
else:
    print("this is not a palndrom")
