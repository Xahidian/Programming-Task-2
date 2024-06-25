from collections import defaultdict, deque

# Function to load the graph from a file
def load_graph(file_name, directed):
    print(f"Loading graph from file {file_name}...")
    graph = defaultdict(list)
    nodes = set()

    with open(file_name, 'r') as file:
        header = file.readline()  # Skip header
        for line in file:
            v1, v2, weight, edge_id = line.strip().split('\t')
            weight = int(weight)
            graph[v1].append((v2, weight))
            nodes.add(v1)
            nodes.add(v2)
            if not directed:
                graph[v2].append((v1, weight))
    
    print("Graph loaded successfully!")
    return graph, nodes

# Dijkstra's algorithm to compute the minimum weighted path
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    nodes = list(graph.keys())

    while nodes:
        current_node = min(nodes, key=lambda node: distances[node])
        nodes.remove(current_node)

        if distances[current_node] == float('inf'):
            break

        for neighbor, weight in graph[current_node]:
            alt = distances[current_node] + weight
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous_nodes[neighbor] = current_node

    path, current_node = deque(), end
    while previous_nodes[current_node] is not None:
        path.appendleft(current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.appendleft(current_node)
    
    return list(path), distances[end]

# Function to find all paths between two nodes
def all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node, weight in graph[start]:
        if node not in path:
            newpaths = all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Function to compute the maximum weighted path
def max_weighted_path(graph, start, end):
    paths = all_paths(graph, start, end)
    max_path = None
    max_weight = float('-inf')

    for path in paths:
        weight = sum(graph[path[i]][graph[path[i]].index((path[i+1], next(w for n, w in graph[path[i]] if n == path[i+1])) if path[i+1] in [n for n, w in graph[path[i]]] else 0)][1] for i in range(len(path) - 1))
        if weight > max_weight:
            max_weight = weight
            max_path = path

    return max_path, max_weight

# Main function
def main():
    file_name = "input.tsf"
    directed = input("Is the graph directed? (y/n): ").strip().lower() == 'y'
    graph, nodes = load_graph(file_name, directed)
    
    print("Nodes of the graph:", sorted(nodes))
    
    while True:
        u = input("Enter the start node: ").strip()
        if u not in nodes:
            print(f"Error: Node {u} does not exist in the graph. Please enter a valid node.")
            continue
        v = input("Enter the end node: ").strip()
        if v not in nodes:
            print(f"Error: Node {v} does not exist in the graph. Please enter a valid node.")
            continue
        
        min_path, min_weight = dijkstra(graph, u, v)
        max_path, max_weight = max_weighted_path(graph, u, v)
        
        if min_path:
            print(f"The minimum weighted path from {u} to {v} is: {' -> '.join(min_path)} with a total weight of: {min_weight}")
        else:
            print(f"No path found from {u} to {v}")
        
        if max_path:
            print(f"The maximum weighted path from {u} to {v} is: {' -> '.join(max_path)} with a total weight of: {max_weight}")
        else:
            print(f"No path found from {u} to {v}")
        
        cont = input("Would you like to continue with a new pair of nodes? (y/n): ").strip().lower()
        if cont == 'n':
            break

if __name__ == "__main__":
    main()
