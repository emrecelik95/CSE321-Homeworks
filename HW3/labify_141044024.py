
def findMinimumCostToLabifyGTU(x, y, mapOfGTU):

    if(x < y):
        return len(mapOfGTU) * x
    
    c = connectedCount(mapOfGTU)   # number of connected graphs
    r = len(mapOfGTU) - c          # number of roads

    return c*x + r*y 

def connectedCount(mapOfGTU):
    n = len(mapOfGTU)
    visited = [-1]*n
    count = 0
    for v in mapOfGTU.keys():
        if(visited[v - 1] == -1):
            count = count + 1
            vect = bfs(mapOfGTU, v)
            for a in vect:
                visited[a - 1] = 1

    return count

def bfs(mapGraph,start):
    n = len(mapGraph)
    nodes = []*n
    visited = [-1]*n
    queue = []
    queue.append(start)
    while(len(queue) > 0):
        x = queue.pop(0)
        if(visited[x - 1] == -1):
            nodes.append(x)
            visited[x - 1] = 1
            adjs = mapGraph[x]
            for v in adjs:
                if(visited[v - 1] == -1):
                    queue.append(v)

    return nodes


mapOfGTU = {
            1 : set([2,3]),
            2 : set([1,3,4]),
            3 : set([1,2,4]),
            4 : set([3,2]),
            5 : set([6]),
            6 : set([5])
           }
minCost = findMinimumCostToLabifyGTU(5,2,mapOfGTU)
print(minCost)
