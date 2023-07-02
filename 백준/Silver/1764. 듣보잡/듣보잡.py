a,b=map(int,input().split())
visit=set()
for i in range(a):
    visit.add(input())

result=[]
for i in range(b):
    x=input()
    if x in visit:
        result.append(x)

result.sort()
print(len(result))
for i in result:
    print(i)
