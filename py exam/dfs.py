__problem__ = "Write a program to demonstrate working of DFS"

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


visited = set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

dfs(visited=visited,graph=graph,node='A')
print(visited)