import collections

def bfs(graph, queue, visited, order):
    if not queue:
        return order

    vertex = queue.popleft()
    if vertex not in visited:
        visited.add(vertex)
        order.append(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)

    return bfs(graph, queue, visited, order)

def dfs(graph, vertex, visited, order):
    visited.add(vertex)
    order.append(vertex)
    for i in graph[vertex]:
        if i not in visited:
            dfs(graph, i, visited, order)
    return order

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    bfs_visited = set()
    bfsres = bfs(graph, collections.deque(['A']), bfs_visited, [])
    print("BFS Order:", bfsres)

    dfs_visited = set()
    dfsres = dfs(graph, 'A', dfs_visited, [])
    print("DFS Order:", dfsres)

if __name__ == "__main__":
    main()
