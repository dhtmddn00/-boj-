
strr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def f(x,y):
    result=""
    while True:
        
        if y//26==0:
            result+=strr[y%26]
            break
        result+=strr[(y%26)]
        y=y//26-1
        
    print(result[::-1]+str(x))
    

while True:
    a=input().split("C")
    
    x=int(a[0][1:])
    y=int(a[1])
    if x==0 and y==0:
        break

    f(x,y-1)
    
