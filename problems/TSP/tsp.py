import random
import math
import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(point_one, point_two):
        """
        Calculate the Euclidean distance between two 2-D Coordinates.

        Parameters:
        - color1 (List[int]): RGB values of the first color.
        - color2 (List[int]): RGB values of the second color.

        Returns:
        float: The Euclidean distance between the two colors.
        """
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point_one, point_two)))

def greedy_TSP(towns):
    circuit = list()
    temp_city = towns[int(random.randint(0, len(towns)))]
    del towns[towns.index(temp_city)]
    circuit.append(temp_city)
    while len(towns) > 0:
        relative_distance = {i:euclidean_distance(temp_city, i) for i in towns}
        new_city = (sorted(relative_distance.items(), key= lambda x: x[1])[0])[0]
        temp_city = new_city
        del towns[towns.index(temp_city)]
        circuit.append(temp_city)
    return circuit

def plot_TSP(towns, circuit):
#    x_coord = [town[0] for town in towns]
#    y_coord = [town[1] for town in towns]
#    
#    for i in range(len(towns)):    
#        plt.plot(x_coord[i], y_coord[i], color="blue")
#    
#    for i in range(len(circuit) -1):
#        plt.plot([circuit[i][0], circuit[i+1][0], circuit[i][1], circuit[i+1][1]], color="black", linestyle="dashed", linewidth=1)
#    plt.plot([circuit[-1][0], circuit[0][0], circuit[-1][1], circuit[0][1]], color="black", linestyle='dashed', linewidth=1)
#    
#    plt.grid(False)
#    plt.axis('off')
#    # Show the plot
#    plt.show()
     
    fig, ax = plt.subplots(2, sharex=True, sharey=True)         # Prepare 2 plots
    ax[0].set_title('Raw nodes')
    ax[1].set_title('Optimized tour')
    for town in towns:
        ax[0].scatter(town[0], town[1])             # plot A
        ax[1].scatter(town[0], town[1])             # plot B
    start_node = 0
    distance = 0.
    circuit.append(circuit[0])
    for i in range(len(circuit)-1):
        start_pos = circuit[i]
        end_pos = circuit[i+1]
        ax[1].annotate("",
                xy=start_pos, xycoords='data',
                xytext=end_pos, textcoords='data',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3"))
        distance += np.linalg.norm(euclidean_distance(end_pos, start_pos))

    textstr = "N nodes: %d\nTotal length: %.3f" % (len(circuit)-1, distance)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax[1].text(0.05, 0.95, textstr, transform=ax[1].transAxes, fontsize=14, # Textbox
            verticalalignment='top', bbox=props)

    plt.tight_layout()
    plt.show()


def generate_2d_coordinates(num_points):
    return [(round(random.uniform(0, 100),2), round(random.uniform(0, 100), 2)) for _ in range(num_points)]


coordinates_2d = generate_2d_coordinates(100)
circuit = greedy_TSP(coordinates_2d)

plot_TSP(coordinates_2d, circuit)