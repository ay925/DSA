matrix=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]

r=len(matrix)
c=len(matrix[0])

row_track=[0]*r
cols_track=[0]*c

for i in range(r):
    for j in range(c):
        if matrix[i][j]==0:
            row_track[i]=-1
            cols_track[j]=-1
for i in range(r):
    for j in range(c):
        if row_track[i]==-1 or cols_track[j]==-1:
            matrix[i][j]=0

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()




