x=int(input())
c=0
d=[0]*(x+1)

for i in range(2,x+1):
	d[i]=d[i-1]+1
	if i%3==0:
		d[i]=min(d[i],d[i//3]+1)
	if i%2==0:
		d[i]=min(d[i],d[i//2]+1)
	

print(d[x])

def min(a,b):
	if a>b:
		return b
	else:
		return a