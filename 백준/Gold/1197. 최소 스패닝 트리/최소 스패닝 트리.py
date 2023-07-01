class edge:
    def __init__(self,a,b,c):
        self.start=a
        self.dest=b
        self.weight=c
        
        
def find(k,fi):
    if k==fi[k]:
        return k
    else:
        fi[k]=find(fi[k],fi)
        return fi[k]
    
            
def kruskalmst(graph,vertex):
    visited=set()
    result=0
    findlist=[]
    findlist.append(0)
    for i in range(1,vertex+1):
        findlist.append(i)
    
    for i in graph:
        
        if find(i.start,findlist)==find(i.dest,findlist):
            continue 
        
        else:
            visited.add(i.start)
            visited.add(i.dest)
            if i.dest not in visited and i.start in visited:
                findlist[i.dest]=find(i.start,findlist)
            elif i.start not in visited and i.dest in visited:
                findlist[i.start]=find(i.dest,findlist)
            else:
                findlist[find(i.dest,findlist)]=find(i.start,findlist)
            result+=i.weight
            
    print(result)
    
    
        
        
        
        

a = list(map(int, input().split()))
graph = []

for _ in range(a[1]):
    edgeinput = list(map(int, input().split()))
    if edgeinput[0]<edgeinput[1]:
        graph.append(edge(edgeinput[0],edgeinput[1],edgeinput[2]))
    else:
        graph.append(edge(edgeinput[1],edgeinput[0],edgeinput[2]))

    
graph.sort(key=lambda x: x.weight)

kruskalmst(graph,a[0])
