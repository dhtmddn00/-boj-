x=input()
result=0
i=0
while i<len(x):
    if i+1==len(x):
        result+=1
        break
    if x[i]=='l' and x[i+1]=='j':
        i+=2
        result+=1
        continue
    if x[i]=='n' and x[i+1]=='j':
        i+=2
        result+=1
        continue
    if x[i]=='c':
        if x[i+1]=='='or x[i+1]=='-':
            i+=2
            result+=1
            continue
    if x[i]=='d':
        if x[i+1]=='-':
            i+=2
            result+=1
            continue
        
        elif i+2<len(x) and x[i+1]=='z' and x[i+2]=='=':
            i+=3
            result+=1
            continue
    if x[i]=='s' and x[i+1]=='=':
        i+=2
        result+=1
        continue
    if x[i]=='z' and x[i+1]=='=':
        i+=2
        result+=1
        continue
    result+=1
    i+=1


print(result)
