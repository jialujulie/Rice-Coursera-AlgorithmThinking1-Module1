""" define three graphs"""

EX_GRAPH0 = {0:set([1,2]),1:set([]), 2:set([])}

EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), \
             8:set([1,2]), 9:set([0,4,5,6,7,3])}

# docstring make complete graph

def make_complete_graph(num_nodes):
    """docstring"""
    dictionary = dict()
    if num_nodes <= 0:
        return dictionary
    else:
        for node in range(num_nodes):
            dictionary[node] = set(other_node for other_node in range(num_nodes))
            dictionary[node].remove(node)

    return dictionary

def compute_in_degrees(digraph):
    """count in_degree for each node"""

    dictionary = dict()

    for key in digraph.keys():
        in_nodes = 0
        for other_key in digraph.keys():
            for node in digraph[other_key]:
                if key == node:
                    in_nodes += 1
                    break

        dictionary[key] = in_nodes

    return dictionary

def in_degree_distribution(digraph):
    """count number of nodes of each in_degree"""

    dictionary = dict()
    keys = compute_in_degrees(digraph).values()
    #print keys
    for key in keys:
         dictionary[key] = keys.count(key)

    return dictionary


#print in_degree_distribution(GRAPH1)
#print compute_in_degrees(GRAPH1)

#print make_complete_graph(3)