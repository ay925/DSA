matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
rows=len(matrix)
cols=len(matrix[0])


top=0
bottom=rows-1
left=0
right=cols-1


result=[]
while(top<=bottom and left<=right):
# Left to right
    for i in range(left,right+1):
        result.append(matrix[top][i])
    top+=1

    # Top to bottom
    for i in range(top,bottom+1):
        result.append(matrix[i][right])
    right-=1

    # Important check
    if top<=bottom:
        # right to left
        for i in range(right,left-1,-1):
            result.append(matrix[bottom][i])
        bottom-=1

    # Important check
    if left<=right:
        # Bottom to Top
        for i in range(bottom,top-1,-1):
            result.append(matrix[i][left])
        left+=1

print(result)
