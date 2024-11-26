n=int(input())
li=list(map(int,input().split()))


result=[0]*n
for i in range(n):
    count=0
    for j in range(n):
        if count==li[i] and result[j]==0:
            result[j]=i+1
            break
        if result[j]==0:
            count+=1

for i in result:
    print(i,end=' ')
    
