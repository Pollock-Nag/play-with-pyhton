import collections
def bfs(graph, root):
    queue = collections.deque([root])
    visited =[root]

    while(queue):
        vartex = queue.popleft()
        for i in graph[vartex]:   #visit all adjecent nodes of vartex
            if i not in visited:
                queue.append(i)
                visited.append(i)

    print(visited)


#  0----1
#  | \  |
#  |  \ |
#  |   \|
#  3    2 -----4
graph = {
  0:[1,2,3],
  1:[0,2],
  2:[0,1,4],
  3:[0],
  4:[2]
}
bfs(graph,0)