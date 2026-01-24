text="nitin"
reversed_text=""
i=len(text)
while i>0:
    reversed_text+=text[i-1]
    i-=1
if(text==reversed_text):
    print("Palandrom")
else:
    print("Not palandrom")
# number
number=121
num=number
revnum=0
while num>0:
    ld=num%10
    revnum*=10
    revnum+=ld
    num//=10
if number==revnum:
    print("Palandrom")
else:
    print("Not palandrom")
