def prim(graph):
    n=len(graph)
    selected = [False] * n
    edge_count = 0
    selected[0]=True
    
    
    print("Edge  \tWeight")
    while edge_count<n-1:
        minimum = 1000
        x=0
        y=0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j]<minimum:
                            minimum=graph[i][j]
                            x=i
                            y=j
                            
        print(f"{x}-{y}  \t{graph[x][y]}")
        selected[y]=True
        edge_count+=1
        
        
if __name__=="__main__":
    graph=[
        [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
        ]
        
prim(graph)
