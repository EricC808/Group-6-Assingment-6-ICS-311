from typing import Dict, List, Tuple

# Dijkstra's algorithm to find shortest path
def shortest_path_group1(graph: Dict[str, List[Tuple[str, int]]], start: str, end: str) -> Tuple[List[str], int]:
    import heapq

    # Priority queue: (cost, current_node, path_so_far)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == end:
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return [], float('inf')  # If no path found
