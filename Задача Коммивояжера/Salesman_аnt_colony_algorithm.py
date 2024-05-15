import random
import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
alfa = 1
beta = 1
tau0 = 0.09
iterrations = 1000

def fading(Q,colony,pheromone_matrix):
    p = random.random()
    m = len(colony)
    delta_tau=0
    n = len(pheromone_matrix)
    for i in range(n):
        for j in range(n):
            S = 0
            for k in range(0,m):
                T = colony[k][0]
                L = colony[k][1]
                S += delta_tau_ant(i,j,Q,T,L)
            tau = pheromone_matrix[i][j]
            pheromone_matrix[i][j] = (1 - p) * tau + S

def delta_tau_ant(i,j,Q,T,L):
    delta_tau = 0
    k = len(T)
    for v in range(1,k):
        if i == T[v-1] and j == T[v]:
            delta_tau = Q / L
    if i == T[-1] and j == T[0]:
        delta_tau = Q / L
    return delta_tau

def set_aside_pheromone(Q,T,L,pheromone_matrix):
    k = len(T)
    for i in range(1,k):
        pheromone_matrix[T[i-1]][T[i]] += delta_tau_ant(T[i-1],T[i],Q,T,L)
    pheromone_matrix[T[k-1]][T[0]] += delta_tau_ant(T[k-1],T[0],Q,T,L)

def find_path_value(path,p):
    n = len(path)
    path_value = 0
    for i in range(1, n):
        path_value += p[path[i-1]][path[i]]
    path_value += p[path[n-1]][path[0]]
    return path_value


def find_best_path(path_matrix):
    n = len(path_matrix[0])
    print("Number of cities =",n)
    number_of_ants = n
    graph_nodes = []
    for i in range(n):
        graph_nodes.append(i)
    pheromone_matrix = create_pheromone_matrix(path_matrix)
    path = []
    min_value = 40 
    best_path = []
    dead_end_path = 0
    for t in range(iterrations):
        colony = []
        p = 0
        for k in range(number_of_ants):
            start_node = k
            path = find_path(graph_nodes, path_matrix, start_node, pheromone_matrix)
            if path != []:
                colony.append([])
                path_value = find_path_value(path,path_matrix)
                colony[p].append(path)
                colony[p].append(path_value)
                p += 1
                set_aside_pheromone(min_value,path,path_value,pheromone_matrix)
                if path_value < min_value:
                    min_value = path_value
                    best_path = path
            else:
                dead_end_path += 1
        fading(min_value,colony,pheromone_matrix)
    print("Min value =", min_value)
    print("Best path:", best_path)
    print("Dead paths:", dead_end_path)
    G = nx.DiGraph()
    for i in range(n):
        for j in range(n):
            if path_matrix[i][j] != None:
                G.add_edge(i, j, weight = pheromone_matrix[i][j])
    show_ways(G)
    
    
def find_path(graph_nodes, path_matrix, start, pheromone_matrix, path = []):
    path = path + [start]
    n = len(graph_nodes)
    if len(path) == n:
        if path_matrix[start][path[0]]!= None:
            return path
        else:
            return []
    if start not in graph_nodes:
        return []
    J = []
    for node in graph_nodes:
        if node not in path:
            if path_matrix[start][node]!= None:
                J.append(node)
    if J == []:
        return []
    probabilities = [0]
    for node in graph_nodes:
        if (node not in path and path_matrix[start][node]!= None):
            p = P(path[-1],node,J,path_matrix,pheromone_matrix)
            probabilities.append(probabilities[-1] + p)                
    rand_number = random.random()
    for i in range(1,len(probabilities)):
        if (rand_number > probabilities[i-1] and rand_number < probabilities[i]):
            node = J[i-1]
            newpath = find_path(graph_nodes, path_matrix, node, pheromone_matrix, path)
            return newpath            
            
def P(i,j,J,path_matrix,pheromone_matrix):
    if (j in J):
        S = 0
        for l in J:
            tau = pheromone_matrix[i][l]
            eta = 1 / path_matrix[i][l]
            S += (tau**alfa)*(eta**beta)     
        tau = pheromone_matrix[i][j]
        eta = 1 / path_matrix[i][j]
        p = (tau**alfa) * (eta**beta) / S
    else:
        p = 0  
    return p

def show_ways(G):
    pos = nx.layout.circular_layout(G)

    #node_sizes = [3 + 10 * i for i in range(len(G))]
    M = G.number_of_edges()
    edge_colors = [e[2]['weight'] for e in G.edges(data=True)]      
    edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
    
    nodes = nx.draw_networkx_nodes(G, pos, node_color='grey')
    edges = nx.draw_networkx_edges(G, pos, arrowstyle='->',
                                   connectionstyle = "arc3,rad=0.2",
                                   arrowsize=10, edge_color=edge_colors,
                                   edge_cmap=plt.cm.Wistia, width=2)
    labels = nx.draw_networkx_labels(G, pos, font_color ='white')
    for i in range(M):
        edges[i].set_alpha(edge_alphas[i])

    pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Wistia)
    pc.set_array(edge_colors)
    plt.colorbar(pc)
    ax = plt.gca()
    ax.set_axis_off()
    #ax.set_facecolor('skyblue')
    #plt.savefig("Graph.png", format="PNG")
    plt.show()
    
def create_pheromone_matrix(path_matrix):
    pheromone_matrix = []
    n = len(path_matrix[0])
    for i in range(n):
        pheromone_matrix.append([])
        for j in range(n):
            pheromone_matrix[i].append(tau0)
            if path_matrix[i][j] == None:
               pheromone_matrix[i][j] = 0
    return pheromone_matrix

def create_visibility_matrix(path_matrix):
    visibility_matrix = path_matrix
    n = len(visibility_matrix[0])
    for i in range(n):
        visibility_matrix.append([])
        for j in range(n):
            visibility_matrix[i].append(1 / visibility_matrix[i][j])
    return visibility_matrix

def show_matrix(path_matrix):
    n = len(path_matrix)
    for i in range(n):
        for j in range (n):
            if path_matrix[i][j] == None:
                print('-', end=' ')
            else:
                print(path_matrix[i][j], end=' ')
        print('')
        
def open_matrix(cities_matrix):
    path_matrix = []
    with open(cities_matrix, encoding = 'utf-8') as matrix:
        for line in matrix:
            path_matrix.append(list(map(int, line.split(" "))))
    n = len(path_matrix[0])
    for i in range(n):
        for j in range (n):
            if i == j or path_matrix[i][j] == 0:
                path_matrix[i][j] = None
    show_matrix(path_matrix)
    return path_matrix

def main():
    cities_matrix = 'matrix12.txt'
    path_matrix = open_matrix(cities_matrix)
    find_best_path(path_matrix)

if __name__ == '__main__':
    main()
