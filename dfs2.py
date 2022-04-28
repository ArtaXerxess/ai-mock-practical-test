diagram = """\
        A
      / | \ 
     B  C  D
    / \    | \ 
   E   F   G  H
  /|       |\ 
 I J      K  L"""
#     E
#    / \ 
#   C   G
#  / \   \ 
# B   D   H
# """
graph = {
#   'E' : ['C','G'],
#   'C' : ['B', 'D'],
#   'G' : ['H'],
#   'B' : [],
#   'D' : ['H'],
#   'H' : []
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
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node,end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
# Driver Code
print(diagram)
print("Following is the Depth-First Search")
dfs(visited, graph, 'A')