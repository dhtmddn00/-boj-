x=int(input())
result=0

for i in range(x):
    inp=input()
    cha=set()
    pre=inp[0]
    k=0
    for j in range(len(inp)):
        if inp[j] in cha and pre!=inp[j]:
            k=1
            break
                
        elif inp[j] not in cha:
            cha.add(inp[j])
        pre=inp[j]
            
    if k==0:
        result+=1

print(result)
