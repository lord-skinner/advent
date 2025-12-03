import sys
from networkx import Graph, connected_components, minimum_edge_cut
from typing import List, Tuple

# Determine the input file from command line arguments or default to "input.txt"
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def read_lines_to_list() -> List[Tuple[str, List[str]]]:
    """Reads lines from the input file and returns a list of tuples containing nodes and their connections."""
    lines: List[Tuple[str, List[str]]] = []
    
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            node, connections = line.split(": ")
            # Append the node and its connections as a tuple
            lines.append((node, connections.split(" ")))

    return lines

def part_one():
    """Calculates and prints the result for part one of the problem."""
    lines = read_lines_to_list()
    answer = 1  # Initialize answer variable

    graph = Graph()  # Create a new graph

    # Build the graph from the input data
    for node, connections in lines:
        graph.add_node(node)  # Add the main node
        for connection in connections:
            graph.add_node(connection)  # Add each connection as a node
            # Add an edge between the node and its connection (ensuring consistent ordering)
            graph.add_edge(
                *((node, connection) if node > connection else (connection, node))
            )

    # Find the minimum edge cut in the graph
    cut = minimum_edge_cut(graph)
    graph.remove_edges_from(cut)  # Remove edges that are part of the cut

    # Get connected components after removing edges
    components = connected_components(graph)
    
    # Calculate the product of the sizes of each component
    for component in components:
        answer *= len(component)

    print(f"Part 1: {answer}")

def part_two():
    """Placeholder function for part two of the problem."""
    print("Merry Christmas!")

# Execute both parts of the problem
part_one()
part_two()