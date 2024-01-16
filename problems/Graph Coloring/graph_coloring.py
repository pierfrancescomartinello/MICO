from typing import Dict, List, Set
import math
import random
import igraph
import matplotlib.pyplot as plt

def generate_random_colors(n, min_distance=100):
    """
    Generate a list of random RGB colors with a specified minimum distance between each color.

    Parameters:
    - n (int): The number of colors to generate.
    - min_distance (int): The minimum Euclidean distance between each generated color (default is 100).

    Returns:
    List[str]: A list of hexadecimal representations of RGB colors.

    Example:
        colors = generate_random_colors(5, min_distance=50)
        print(colors)
    """

    def euclidean_distance(color1, color2):
        """
        Calculate the Euclidean distance between two RGB colors.

        Parameters:
        - color1 (List[int]): RGB values of the first color.
        - color2 (List[int]): RGB values of the second color.

        Returns:
        float: The Euclidean distance between the two colors.
        """
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(color1, color2)))

    def generate_color():
        """
        Generate a random RGB color.

        Returns:
        List[int]: RGB values of the generated color.
        """
        return [random.randint(0, 255) for _ in range(3)]

    def rgb_to_hex(rgb):
        """
        Convert RGB values to a hexadecimal color representation.

        Parameters:
        - rgb (List[int]): RGB values of the color.

        Returns:
        str: Hexadecimal representation of the color.
        """
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

    colors = [generate_color()]
    
    while len(colors) < n:
        new_color = generate_color()

        # Check the distance between the new color and existing colors
        distances = [euclidean_distance(new_color, existing_color) for existing_color in colors]

        # If the minimum distance condition is satisfied, add the new color
        if all(distance > min_distance for distance in distances):
            colors.append(new_color)

    hex_colors = [rgb_to_hex(i) for i in colors]
    return hex_colors


def get_color(color_list:Set[int]
)-> int:
    """
    Get the smallest non-negative integer not present in the given set of colors.

    Parameters:
    - color_list (Set[int]): A set containing integers representing used colors.

    Returns:
    int: The smallest non-negative integer not present in the color set.

    Example:
        used_colors = {0, 1, 3, 4}
        next_color = get_color(used_colors)
        print(next_color)
    """

    count = 0
    while count in color_list: count +=1
    return count

def greedy_coloring(G,
                    order:List[str]
):
    
    """
    Perform greedy graph coloring on an undirected graph.

    Parameters:
    - G (Dict[str, List[str]]): An undirected graph represented as an adjacency list.
    - order (List[str]): The order in which nodes are considered for coloring.

    Returns:
    Dict[str, int]: A dictionary where keys are nodes and values are color assignments.

    Example:
        graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
        node_order = ['A', 'B', 'C']
        coloring_result = greedy_coloring(graph, node_order)
        print(coloring_result)
    """

    color = dict()
    for node in order:
        neighbourhing_colours = set([color[neigh] for neigh in G[node] if neigh in color])
        color[node] = get_color(neighbourhing_colours)
    return color


def plot_graph(graph, graph_coloring):
    """
    Plot a graph with vertices colored based on a given graph coloring.

    Parameters:
    - graph (Dict[str, List[str]]): An undirected graph represented as an adjacency list.
    - graph_coloring (Dict[str, int]): A dictionary mapping nodes to their assigned colors.

    Example:
        graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
        coloring = {'A': 0, 'B': 1, 'C': 2}
        plot_graph(graph, coloring)
    """

    vertices = [i for i in graph.keys()]
    colours = generate_random_colors(len(graph_coloring), min_distance=100)
    colours_dict = dict()
    for vertex in vertices: colours_dict[vertex] = colours[graph_coloring[vertex]]
    print(colours_dict)
    g = igraph.Graph()

    for vertex in vertices: g.add_vertex(name=str(vertex), color=colours_dict[vertex])

    g.vs["color"] = [colours_dict[i] for i in vertices]
    for k,v in graph.items():
        for el in v:
            g.add_edge(k,el)
    fig, ax = plt.subplots()
    igraph.plot(g, layout= "kk", target=ax, vertex_color= g.vs["color"])
    plt.show()



# sparse_graph = {
#     'A': ['B', 'C', 'D'],
#     'B': ['A', 'C', 'E'],
#     'C': ['A', 'B', 'D', 'E'],
#     'D': ['A', 'C', 'E', 'F'],
#     'E': ['B', 'C', 'D', 'F'],
#     'F': ['D', 'E', 'G'],
#     'G': ['F']
# }
# 
# colouring = greedy_coloring(sparse_graph, [i for i in sparse_graph.keys()])
# 
# plot_graph(sparse_graph, colouring)