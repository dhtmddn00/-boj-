n=int(input())
arr=list(map(int,input().split()))
result=[]
result.append(-1)
update=[-1]
upsize=0
prev=arr[n-1]
for i in range(n-2,-1,-1):
    if prev>arr[i]:
        update.append(prev)
        upsize+=1
        result.append(update[upsize])
    else:
        while(1):
            if upsize==0:
                result.append(-1)
                update.append(arr[i])
                upsize+=1
                break
            if arr[i]>=update[upsize]:
                update.pop(upsize)
                upsize-=1
                continue
            else:
                result.append(update[upsize])
                break
        
    prev=arr[i]




for i in range(n-1,-1,-1):
    print(result[i],end=' ')
