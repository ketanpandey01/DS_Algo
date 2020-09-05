from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        # stored as adajency list
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        isVisited = [False] * self.V
        q = []
        q.append(start)
        isVisited[start] = True
        # print(self.graph[start])
        while q:
            start = q.pop(0)
            print(start, end = " ")

            for n in self.graph[start]:
                if(isVisited[n]==False):
                    q.append(n)
                    isVisited[n] = True
    
    def dfs(self, node):
        isVisited = [False] * self.V
        self.dfsRecurse(node, isVisited)

    def dfsRecurse(self, node, visited):
        print(node, end=" ")
        visited[node] = True
        for n in self.graph[node]:
            if(visited[n] == False):
                self.dfsRecurse(n, visited)

g = Graph(6) 
g.addEdge(5, 2)
g.addEdge(5, 0)    
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 

print("BFS: ", end=" ")
g.bfs(5)
print(end='\n')
print("DFS: ", end=" ")
g.dfs(5)
    
