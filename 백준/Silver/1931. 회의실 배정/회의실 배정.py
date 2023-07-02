class meeting:
    def __init__(self,a,b):
        self.start=a
        self.end=b


def sort_key(a):
    return (a.end,a.start)


n=int(input())

k=[]
for i in range(n):
    a,b=map(int,input().split())
    
    k.append(meeting(a,b))

k.sort(key=sort_key)


count=0
prev=0


for i in k:
    if prev>i.start:
        continue
    prev=i.end
    count+=1

print(count)
    
