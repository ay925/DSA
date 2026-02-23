nums=[[1,2,3],[4,5,6],[7,8,9]]
# Upper
rows=len(nums)
cols=len(nums[0])

for i in range(rows):
    for j in range(cols):
        if j>=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# Lower
print("\n")
for i in range(rows):
    for j in range(cols):
        if j<=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# Diognal
print("\n")
for i in range(rows):
    for j in range(cols):
        if j==i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# Reverese Diognal
print("\n")
for i in range(rows):
    for j in range(cols):
        if j+i==rows-1:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
