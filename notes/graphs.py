# theres some commons themes to these uestions i want to write down :

# first off, we have represetation : 
#   - this refers to how we store the graph, the typical data structure is 

graph = {node: [neighbors]}

# then we have traversal, which is how we explore the graph, you can do this with either:

# dfs (stack / recursion)

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

# bfs (queue)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    steps = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            # process node.
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

            steps += 1

# and then finally we have the tracking state, which is usually a visited array.

visited = [False] * n

# there are variations of graphs too :

# undirected graph requires two way edges, similar to what was done in the 1466 reorder routes problem.

graph = {i: [] for i in range(n)}
for a, b in connections:
    graph[a].append(b)
    graph[b].append(a)

# or directed. this would only require one way edges like this.

graph = {i: [] for i in range(n)}
for a, b in connections:
    graph[a].append(b)

# and then finally we have weighted graphs, which require a "running cost".

graph = {i: [] for i in range(n)}
for a, b, w in edges:
    graph[a].append((b, w))