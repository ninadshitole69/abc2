def find_parent(parent,node):
    if parent[node]==node:
        return node
    return find_parent(parent,parent[node])

def union(parent,u,v):
    parent_u = find_parent(parent,u)
    parent_v= find_parent(parent,v)
    parent[parent_u]=parent_v
    
def kruskal_mst(graph):
    edges=sorted(graph,key=lambda x:x[2])
    parent={}
    mst=[]
    
    
    
    for u,v,w in edges:
        parent[u]=u
        parent[v]=v

    for u,v,weight in edges:
        if find_parent(parent,u)!=find_parent(parent,v):
            union(parent,u,v)
            mst.append((u,v,weight))
            
    print("Edges in MST: ")
    total_weight=0
    for u,v,weight in mst:
        print(f"{u}-{v} : {weight}")
        total_weight +=weight
    print("total weight : " , total_weight)
    
if __name__=="__main__":
    graph = [
    ("A", "B", 1),
    ("A", "C", 3),
    ("B", "C", 1),
    ("B", "D", 6),
    ("C", "D", 4),
    ("C", "E", 2),
    ("D", "E", 5)
]

    kruskal_mst(graph)
