n,m,xx=map(int,input().split())

li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

graph={}
for i in range(n):
    for j in range(m):
        if li[i][j] not in graph:
            graph[li[i][j]]=1
        else:
            graph[li[i][j]]+=1


tarr=[]

for i in range(min(graph),max(graph)+1):
    time=0
    b=xx
    for j in graph:
        if j-i>0:
            time+=2*(j-i)*graph[j]
            b+=(j-i)*graph[j]
        else:
            time+=(i-j)*graph[j]
            b-=(i-j)*graph[j]
    if b>=0:
        tarr.append((time,i))

if len(graph)==1:
    print(0,li[0][0])
else:
    tarr.sort()
    mxx=0
    mnn,k=tarr[0]
    for a,b in tarr:
        if mnn!=a:
            break
        if mxx<b:
            mxx=b

    print(mnn,mxx)

        
