def d(n):
    result=0
    x=n
    while(1):
        s=x%10
        x=x//10
        result+=s
        if x==0:
            break
    
    return n+result

li=set()

for i in range(1,10000):
    li.add(d(i))
    if i in li:
        continue
    print(i)
            
