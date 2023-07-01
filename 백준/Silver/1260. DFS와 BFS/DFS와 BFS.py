def dfs(start,graph):
    visited=set()
    result=[]

    def dfsfunc(u):
        if u in visited:
            return
        visited.add(u)
        result.append(u)
        if u in graph:
            for i in graph[u]:
                dfsfunc(i)
            
    dfsfunc(start)
            
    for i in result:
        print(i,end=' ')


def bfs(start,graph):
    visited=set()
    result=[]

    def bfsfunc(u):
        queue=[u]
        visited.add(u)
        while queue:
            new=queue.pop(0)
            result.append(new)
            if new in graph:
                for i in graph[new]:
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
    bfsfunc(start)
    for i in result:
        print(i,end=' ')




a=list(map(int,input().split()))
graph={}
for i in range(a[1]):
    edge=list(map(int,input().split()))
    if edge[0] in graph:
        graph[edge[0]].append(edge[1])
    else:
        graph[edge[0]]=[edge[1]]
    if edge[1] in graph:
        graph[edge[1]].append(edge[0])
    else:
        graph[edge[1]]=[edge[0]]

for i in graph.keys():
    graph[i].sort()

dfs(a[2],graph)
print()
bfs(a[2],graph)



