class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [ [0 for col in range(vertices)] for row in range(vertices)]

    def minDistanceVertex(self, sptSet, dist):
        minDist = float('inf')
        minVertex = None
        for vrtx in range(self.V):
            if(dist[vrtx] < minDist and sptSet[vrtx] == False):
                minDist = dist[vrtx]
                minVertex = vrtx
        
        return minVertex

    def dijkstra(self, source):
        sptSet = [False] * self.V
        distance = [float('inf')] * self.V
        distance[source] = 0
        # sptSet[source] = True

        for index in range(self.V):

            u = self.minDistanceVertex(sptSet, distance)
            sptSet[u] = True

            for v in range(self.V):
                if(self.graph[u][v] > 0 and sptSet[v] == False and distance[v] > distance[u] + self.graph[u][v]):
                    distance[v] = distance[u] + self.graph[u][v]

        for v in range(self.V):
            print(str(v) + "  " + str(distance[v]))



g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.dijkstra(0)