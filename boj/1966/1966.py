N=int(input())

for i in range(N):
    n,res=map(int,input().split())
    val=list(map(int,input().split()))

    result=[]
    for i in range(n):
        result.append((val[i],i))
    
    count=0
    cnt=0
    for k in range(n):
        for i in range(n):
            flag=0
            for j in range(cnt+1,n):
                if result[cnt][0]<result[j][0]:
                    result.append(result[cnt])
                    result.pop(cnt)
                    flag=1
                    break
            if flag==0:
                cnt+=1
            

        
                

    for i in range(n):
        a,k=result[i]
        if k== res:
            print(i+1)
        
