from typing import Any, Callable, List, Tuple

class Bin:

    """
    A class representing a bin in a bin-packing problem.

    Attributes:
    - element_list (List[bool]): List of booleans representing the presence or absence of elements in the bin.
    - occupied_size (int | float): The occupied size of the bin.

    Methods:
    - __init__(element_list: List[bool], occupied_size: int | float): Constructor to initialize the bin with the given attributes.
    """

    element_list:List[bool]
    occupied_size:int|float = 0

    def __init__(self,
                 element_list:List[bool],
                 occupied_size:int|float
    ):
        
        """
        Initialize a Bin instance.

        Parameters:
        - element_list (List[bool]): List of booleans representing the presence or absence of elements in the bin.
        - occupied_size (int | float): The occupied size of the bin.
        """

        self.element_list = element_list
        self.occupied_size = occupied_size
    

def bin_packing(elements:List[Any], # Elements are defined as their weight
                bin_size:float
)->List[Bin]:
    list_of_bins = []
    for index,element in enumerate(elements):
        if not list_of_bins or all(element>(bin_size - b.occupied_size) for b in list_of_bins):
            bin_rep = [False if i != index else True for i in range(len(elements))]
            list_of_bins.append(Bin(bin_rep, element))
        else:
            list_of_bins = sorted(list_of_bins, key=lambda x: x.occupied_size, reverse=True)
            for bin in list_of_bins:
                if bin_size - bin.occupied_size>=element:
                    bin.element_list[index] = True
                    bin.occupied_size = bin.occupied_size + element
                    break
                else:
                    continue
    return list_of_bins


def draw(bins:List[Any]):
    num = [i.element_list.count(True) for i in bins]
    ind = [[i for i,v in enumerate(b.element_list) if v == True] for b in bins]

    for i in range(len(bins)):
        print(i, "*"*num[i])


bins = bin_packing([5, 8, 2, 7, 1, 4, 6], 15)
num = [i.element_list.count(True) for i in bins]
ind = [[i for i,v in enumerate(b.element_list) if v == True] for b in bins]


for i in range(len(bins)):
    print(i, "*"*num[i])
    print(ind[i])