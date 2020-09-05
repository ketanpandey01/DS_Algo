from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def topologicalSort(self):
        isVisited = [False] * self.V
        tempStack = []
        for node in range(self.V):
            if(isVisited[node] == False):
                self.topologicalSortRecurse(node, isVisited, tempStack) 
        
        print(*tempStack[::-1])
    
    def topologicalSortRecurse(self, node, visited, tempStack):
        visited[node] = True
        for n in self.graph[node]:
            if(visited[n] == False):
                self.topologicalSortRecurse(n, visited, tempStack)

        tempStack.append(node)

    
g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0);    
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print("Topological Sort: ", end=" ")
g.topologicalSort() 
