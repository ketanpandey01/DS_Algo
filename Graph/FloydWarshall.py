def floydWarshall(graph):

    dist = graph.copy()
    for middle in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][middle] + dist[middle][j])
    printSolution(dist)

def printSolution(dist):
    print ("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                # print "%7s" % ("INF"),
                print('INF')
            else:
                # print "%7d\t" % (dist[i][j]),
                print(dist[i][j])
            if j == V-1:
                print("")


INF = float('inf')
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]
V = len(graph)
floydWarshall(graph)