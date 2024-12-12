import network_setup
import router_management

if __name__ == "__main__":
    # Crea la rete iniziale utilizzando network_setup
    network = network_setup.create_network()

    # Simula il Distance Vector Routing
    router_management.simulate_distance_vector_routing(network)

    # Modifica la rete
    print("\nModifying the network...\nAdding node D, connecting it to C with cost 3 and to B with cost 5, and removing the edge between B and C.\n")
    # Modifica dinamicamente la rete
    network_setup.add_node(network, 'D')
    network_setup.add_edge(network, 'C', 'D', 3)
    network_setup.add_edge(network, 'B', 'D', 5)
    network_setup.remove_edge(network, 'B', 'C')

    # Simula il Distance Vector Routing
    router_management.simulate_distance_vector_routing(network)

     # Modifica la rete
    print("\nModifying the network...\nModifying the cost of the edge between B and D to 15.\n")
    # Modifica dinamicamente la rete
    network_setup.add_edge(network, 'B', 'D', 15)

    # Simula il Distance Vector Routing
    router_management.simulate_distance_vector_routing(network)
