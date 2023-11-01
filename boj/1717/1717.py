import sys
input=sys.stdin.readline

sys.setrecursionlimit(10**5)
n,m=map(int,input().split())
arr=[]


def find(x):
    if arr[x]!=x:
        arr[x]=find(arr[x])
    return arr[x]


    
for i in range(n+1):
    arr.append(i)
    
for i in range(m):
    a,b,c=map(int,input().split())
    x=find(b)
    y=find(c)
    if not a:
        if x<y:
            arr[y]=x
        elif y<x:
            arr[x]=y
    else:
        if x==y:
            print("YES")
        else:
            print("NO")
