def add_node(network, node):
    """Aggiunge un nuovo nodo alla rete."""
    if node not in network:
        network[node] = {}
        for existing_node in network:
            if existing_node != node:
                network[existing_node][node] = float('inf')
                network[node][existing_node] = float('inf')

def add_edge(network, node1, node2, cost):
    """Aggiunge un collegamento tra due nodi con un costo specificato."""
    if node1 in network and node2 in network:
        network[node1][node2] = cost
        network[node2][node1] = cost

def remove_edge(network, node1, node2):
    """Rimuove il collegamento tra due nodi."""
    if node1 in network and node2 in network:
        if node2 in network[node1]:
            del network[node1][node2]
        if node1 in network[node2]:
            del network[node2][node1]

def remove_node(network, node):
    """Rimuove un nodo e i suoi collegamenti dalla rete."""
    if node in network:
        for neighbor in list(network[node].keys()):
            del network[neighbor][node]
        del network[node]

def create_network():
    """Crea una rete iniziale utilizzando add_node e add_edge."""
    network = {}
    
    # Aggiungi i nodi
    add_node(network, 'A')
    add_node(network, 'B')
    add_node(network, 'C')
    
    # Aggiungi gli archi con i costi
    add_edge(network, 'A', 'B', 1)
    add_edge(network, 'A', 'C', 4)
    add_edge(network, 'B', 'C', 2)
    
    return network
