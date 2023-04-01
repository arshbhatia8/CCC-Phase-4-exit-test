import heapq

def minCost(g_nodes, g_from, g_to, g_weight):
    # Create adjacency list for original graph
    adj_list = [[] for _ in range(g_nodes)]
    for i in range(len(g_from)):
        adj_list[g_from[i] - 1].append((g_to[i] - 1, g_weight[i]))

    # Create new graph with all possible edges and weights of 1
    new_edges = []
    for i in range(g_nodes):
        for j in range(g_nodes):
            if i != j and (i+1, j+1) not in zip(g_from, g_to):
                new_edges.append((i, j, 1))

    # Add new graph to original graph
    for i, j, w in new_edges:
        adj_list[i].append((j, w))

    # Initialize distances to infinity except for node 1
    distances = [float('inf')] * g_nodes
    distances[0] = 0

    # Initialize priority queue with node 1
    pq = [(0, 0)]

    while pq:
        dist, node = heapq.heappop(pq)

        # Check if we have already visited this node
        if dist > distances[node]:
            continue

        # Update distances to neighbors
        for neighbor, weight in adj_list[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances[-1]
