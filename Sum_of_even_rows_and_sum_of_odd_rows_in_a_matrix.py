r,c= map(int,input().split())
mat = [list(map(int,input().split())) for i in range(r)]
s=0
v=0
for i in range(r):
    for j in range(c):
        if i%2==0:
            s=s+mat[i][j]
        else:
            v=v+mat[i][j]
print(s,v)