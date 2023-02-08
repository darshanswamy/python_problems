# Solve linkedin connection level and traversal path with breadth first search 
from queue import Queue
# examples of first level connections in linkedin
linkedin_connections = {
    'Mike': ['Rob'],
    'Rob': ['David', 'Mike'],
    'David': ['Rob', 'Sam', 'Steve'],
    'Sam': ['David'],
    'Steve': ['David']
}




def get_linkedin_level(user1, user2):
    visited = {}
    level = {}
    parent = {}
    bfs_traversal_output  = []
    que = Queue()
    for node in linkedin_connections.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    # set inital seed as user 1
    s = user1
    visited[s] = True
    level[s] = 0
    que.put(s)

    while not que.empty():
        u = que.get()
        bfs_traversal_output.append(u)
        print(linkedin_connections[u])
        for v in linkedin_connections[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                que.put(v)
    print("levels: ", level)
    # traveral path between user 1 and user 2
    print("Path btw user1 and user2: ", bfs_traversal_output)
    return level[user2]

print(get_linkedin_level('Mike', 'Sam'))
print(get_linkedin_level('Mike', 'David'))