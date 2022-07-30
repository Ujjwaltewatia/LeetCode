#BFS

class Graph:
    
    def __init__(self):
        self.graph={}
        
    def addEdge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[v]
        else:   
            self.graph[u].append(v)
        
    def BFS(self,start):
        queue=[]*len(self.graph)
        visited={}
        visited[start]=True
        queue.append(start)

        
        while queue:
            start=queue.pop(0)
            
            print(start)
            
            for i in self.graph[start]:
                if i not in visited or visited[i]==False:
                    visited[i]=True
                    queue.append(i)
if __name__=="__main__":          
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2,1)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.graph)
    g.BFS(2)      
        
