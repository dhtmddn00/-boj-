from collections import deque 
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    qq=deque()
    mv=[(1,0),(-1,0),(0,1),(0,-1)]
    X=characterX
    Y=characterY

    qq.append((X,Y,0))
    
    visit=set()
    visit.add((X,Y))
    flgg=0
    while qq:
        XX,YY,h=qq.popleft()
        print(XX,YY,h)
        if XX==itemX and YY==itemY:
            result=h
            break
        for mx,my in mv:
            if (XX+mx,YY+my) in visit:
                continue


            flag=0
            for aa in rectangle:
                if aa[0]<XX+(mx/2)<aa[2] and aa[1]<YY+(my/2)<aa[3]:
                    flag=1
                    break
            if flag==1:
                continue
            for aa in rectangle:

                if my==0 and aa[0] <= XX+(mx/2) <=aa[2] and (YY+my==aa[1] or YY+my==aa[3]):
                    qq.append((XX+mx,YY+my,h+1))
                    visit.add((XX+mx,YY+my))
                    break
                elif mx==0 and aa[1]<=YY+(my/2)<=aa[3] and (XX+mx==aa[0] or XX+mx==aa[2]):
                    qq.append((XX+mx,YY+my,h+1))
                    visit.add((XX+mx,YY+my))
                    break
                
    return result


