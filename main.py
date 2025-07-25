# main.py

from shortest_path import shortest_path_group1

def main():
    # Create a graph for testing (replace with your graph format)
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('A', 2), ('C', 1), ('D', 7)],
        'C': [('A', 4), ('B', 1), ('D', 3)],
        'D': [('B', 7), ('C', 3)]
    }

    print("=== Group 1: Shortest Path ===")
    start_node = 'A'
    end_node = 'D'
    path, cost = shortest_path_group1(graph, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {path}, cost: {cost}")
    print()

    print("=== Group 2: Placeholder ===")
    # TODO: Call Group 2’s function here
    # Example: result = group2_function(graph)
    print("Group 2 function output goes here")
    print()

    print("=== Group 3: Placeholder ===")
    # TODO: Call Group 3’s function here
    # Example: result = group3_function(graph)
    print("Group 3 function output goes here")
    print()

if __name__ == "__main__":
    main()
