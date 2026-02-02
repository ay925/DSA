# st="nitin"
# revstr=""
# i=len(st)-1
# while(i>=0):
#     revstr+=st[i]
#     i-=1
# if(st==revstr):
#     print("Palindrome")
# else:
#     print("Not Palindrome")



def ispalindrom(s,l,r):
    if(l>=r):
        return True
    if(s[r]!=s[l]):
        return False
    return ispalindrom(s,l+1,r-1)

s="12345678987654321"
l=0
r=len(s)-1
result=ispalindrom(s,l,r)
print(result)
