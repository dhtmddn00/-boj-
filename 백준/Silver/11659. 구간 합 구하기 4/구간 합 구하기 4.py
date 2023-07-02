import sys

input = sys.stdin.readline


a,b=map(int,input().split())

su=[]
summ=0
for k in input().split():
    summ+=int(k)
    su.append(summ)
for i in range(b):
    result=0
    x,y=map(int,input().split())
    if x==1:
        print(su[y-1])
    else:
        print(su[y-1]-su[x-2])
    
    

