import time

def find_path_value(path,p):
    n = len(path)
    path_value = 0
    for i in range(1, n):
        path_value += p[path[i-1]][path[i]]
    path_value += p[path[n-1]][path[0]]
    return path_value

def find_all_paths(graph_nodes, path_matrix, start, end, path = []):
    path = path + [start]
    n = len(graph_nodes)
    if start == end:
        return [path]
    if start not in graph_nodes:
        return []
    J = [node
         for node in graph_nodes
         if node not in path
         and path_matrix[start][node]!= None]                         
    if J == []:
        return [] 
    paths = []  
    for node in J:
        newpaths = find_all_paths(graph_nodes, path_matrix, node, end, path)
        for newpath in newpaths:
            if (len(newpath) == n and path_matrix[newpath[-1]][newpath[0]]):
                paths.append(newpath)
    return paths

def find_best_path(path_matrix):
    n = len(path_matrix)
    print("Number of cities =",n)
    graph_nodes = [i for i in range(n)]  
    start_node = 0
    best_path = []
    equal_paths = []
    min_value = float("inf")
    start_time = time.time()
    for end_node in graph_nodes:
        if start_node != end_node:
            path_list = []
            all_paths = find_all_paths(graph_nodes, path_matrix, start_node, end_node)
            for path in all_paths:
                path_value = find_path_value(path, path_matrix)    
                if path_value < min_value:
                    equal_paths = []
                    min_value = path_value
                    best_path = path
                elif path_value == min_value:
                    equal_paths.append(path)
                else:
                    pass
                
    end_time = time.time() - start_time
    print("--- %s seconds ---" % (end_time))                
    print("Min value =", min_value)
    print("Best path:", best_path)
    print("Equal paths:", equal_paths)
    
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
    n = len(path_matrix)
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
