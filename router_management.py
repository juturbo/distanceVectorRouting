from tabulate import tabulate

def initialize_routing_table(network):
    """Inizializza le tabelle di routing per ogni nodo nella rete."""
    routing_table = {}
    for node in network:
        routing_table[node] = {
            'distances': {dest: (0 if node == dest else float('inf')) for dest in network},
            'next_hop': {dest: (node if node == dest else None) for dest in network}
        }
    return routing_table

def update_routing_table(node, neighbors, routing_table):
    """Aggiorna la tabella di routing di un nodo usando l'algoritmo di Bellman-Ford."""
    updated = False
    for neighbor, cost in neighbors.items():
        for dest, dest_cost in routing_table[neighbor]['distances'].items():
            new_cost = cost + dest_cost
            if new_cost < routing_table[node]['distances'][dest]:
                routing_table[node]['distances'][dest] = new_cost
                routing_table[node]['next_hop'][dest] = neighbor
                updated = True
    return updated

def propagate_updates(network, routing_table):
    """Propaga gli aggiornamenti delle tabelle di routing fino alla convergenza."""
    converged = False
    iteration = 0
    while not converged:
        if iteration > 0:
            print(f"Iteration {iteration}:")
            print_routing_tables(routing_table)
        converged = True
        for node, neighbors in network.items():
            if update_routing_table(node, neighbors, routing_table):
                converged = False
        iteration += 1
        print("\n\n")

def print_routing_tables(routing_table):
    """Stampa le tabelle di routing in formato tabellare."""
    for node, table in routing_table.items():
        print(f"Routing table for {node}:")
        data = [
            (dest, table['distances'][dest], table['next_hop'][dest] if table['next_hop'][dest] else "-")
            for dest in table['distances']
        ]
        print(tabulate(data, headers=["Destination", "Cost", "Next Hop"], tablefmt="grid"))
        print()

def simulate_distance_vector_routing(network):
    """Esegue la simulazione del Distance Vector Routing."""
    routing_table = initialize_routing_table(network)    
    propagate_updates(network, routing_table)
