class Graph:
    def __init__(self):
        self.graph={}

    def addEdge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[v]
        else:
            self.graph[u].append(v)
            
    def dfs(self,start):
        ans=[]*len(self.graph)
        visited={ key: False for key in self.graph.keys()}
        self.dfsUtils(start,ans,visited)
        for v in visited.keys():
            if visited[v]==False:
                self.dfsUtils(v,ans,visited)
        return ans
        
                
    def dfsUtils(self,start,ans,visited):
        visited[start]=True
        ans.append(start)
        for i in self.graph[start]:
            if visited[i]==False:
                self.dfsUtils(i,ans,visited)

                
g=Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,5)
g.addEdge(5,6)
g.addEdge(6,3)
g.addEdge(3,1)
g.addEdge(3,4)
g.addEdge(4,0)
g.addEdge(0,4)
g.addEdge(4,3)
g.addEdge(3,6)
g.addEdge(6,5)
g.addEdge(5,2)
g.addEdge(2,1)
g.addEdge(1,0)
g.addEdge(1,3)
g.addEdge(7,8)
g.addEdge(8,7)
print(g.graph)
        
print(g.dfs(3))
        
    
