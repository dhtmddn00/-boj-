n=int(input())
li=list(map(int,input().split()))

li.sort()
result=0
for i in range(n):
    result+=(n-i)*li[i]

print(result)

