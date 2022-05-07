__problem__ = "Write a program to demonstrate working of BFS"
diagram = """\
       A
     / | \ 
    B  C  D
   / \    | \ 
  E   F   G  H
 /\       /\ 
I  J     K  L"""
graph ={
    'A':['B','C','D'],
    'B':['E','F'],
    'C':[],
    'D':['G','H'],
    'E':['I','J'],
    'F':[],
    'G':['K','L'],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[],
}
queue = []
visited = []
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        x = queue.pop(0)
        print(x,end=" ")
        for neighbour in graph[x]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited=visited,graph=graph,node='A')