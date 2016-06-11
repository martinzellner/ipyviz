import networkx as nx
from networkx.readwrite import json_graph
import json
from IPython.display import HTML
from string import Template


def graph_plot(adjacency_matrix):
    """
    Creates a JavaScript Graph Plot from the graph given by the adjacency matrix
    :param adjacency_matrix: A numpy array returning the adjacency matrix
    :return: an ipython html object
    """
    g = nx.from_numpy_matrix(adjacency_matrix)
    return nx_graph_plot(g)


def nx_graph_plot(nx_graph):
    """
    Creates a JavaScript Graph Plot from the given networkx graph
    :param nx_graph: A networkx graph object
    :return: an ipython html object
    """
    data = json_graph.node_link_data(nx_graph)
    s = json.dumps(data)
    with open("./graph.html") as f:
        html_content = f.read()

    template = Template(html_content)
    return HTML(template.substitute(json=s))