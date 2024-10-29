def compress(arr,x,y,size):
    ss=0
    for i in range(y,y+size):
        ss+=sum(arr[i][x:x+size])

    if ss==size*size:
        return "1"
    elif ss==0:
        return "0"
    else:
        q1=compress(arr,x,y,size//2)
        q2=compress(arr,x+size//2,y,size//2)
        q3=compress(arr,x,y+size//2,size//2)
        q4=compress(arr,x+size//2,y+size//2,size//2)
        return "("+q1+q2+q3+q4+")"


N=int(input())
arr=[]
for i in range(N):
    x=[]
    kk=input()
    for j in range(N):
        x.append(int(kk[j]))

    arr.append(x)


    
print(compress(arr,0,0,N))
