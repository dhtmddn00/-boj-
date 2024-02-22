from collections import deque


n,m=map(int,input().split())


gph=[]
for i in range(n+1):
    gph.append([100000]*(n+1))

for i in range(1,n+1):
    gph[i][i]=0


for i in range(m):
    a,b=map(int,input().split())
    gph[a][b]=1
    gph[b][a]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if gph[i][k]+gph[k][j]<gph[i][j]:
                gph[i][j]=gph[i][k]+gph[k][j]
                

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if gph[i][k]+gph[k][j]<gph[i][j]:
                gph[i][j]=gph[i][k]+gph[k][j]            

result=[]
for i in range(1,n+1):
    ssm=0
    for j in range(1,n+1):
        if gph[i][j]<100000:
            ssm+=gph[i][j]

    result.append((ssm,i))

result.sort()

print(result[0][1])
