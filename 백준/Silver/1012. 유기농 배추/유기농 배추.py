q=int(input())
for i in range(q):
    m,n,k=map(int,input().split())


    mapp=[]
    for i in range(n):
        mapp.append([])
        for j in range(m):
            mapp[i].append(0)
            
    for x in range(k):
        a,b=map(int,input().split())
        mapp[b][a]=1
    cnt=0


    move=[(0,1),(1,0),(0,-1),(-1,0)]
    visited=set()

    while(1):
        queue=[]
        fla=0
        for i in range(n):
            for j in range(m):
                
                if (j,i) not in visited and mapp[i][j]==1:
                    fla=1
                    queue.append((j,i))
                    visited.add((j,i))
                    break
                
            if fla==1:
                break
        
        if not queue:
            print(cnt)
            break
            
        
        while(queue):
            x,y=queue.pop(0)
            for i in move:
                dx,dy=i
                mx=x+dx
                my=y+dy
                if mx<0 or mx>m-1 or my<0 or my>n-1 or ((mx,my) in visited) or mapp[my][mx]==0:
                    continue
                queue.append((mx,my))
                visited.add((mx,my))
                

        cnt+=1
