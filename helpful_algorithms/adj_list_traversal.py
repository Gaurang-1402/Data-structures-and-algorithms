# For Adjacency Matrix


# For Adjacency List
# NOT SURE IF THIS WORKS
def dfs_adjacency_list(adj_list, currNode, visited, array):
    if len(adj_list[currNode]) == 0:
        # leaf node
        array.append(currNode)
        return array
    else:
        if currNode not in visited:
            visited[currNode] = True
            array.append(currNode)
        for child in adj_list[currNode]:
            if child not in visited:
                visited[child] = True
                array.append(child)
                array = dfs_adjacency_list(adj_list, child, visited, array)
        return array


def bfs_adjacency_list(adj_list):
    visited = {}
    queue = []
    array = [0]

    queue.append(0)

    while len(queue) != 0:
        node = queue.pop(0)
        for child in adj_list[node]:
            array.append(child)
            queue.append(child)

    return array













