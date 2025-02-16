import heapq
import time
import tracemalloc
import matplotlib.pyplot as plt

# 1. Grid and Graph Creation
def initialize_grid():
    return [
        ['S', '.', '.', 'X', 'G'],
        ['.', 'X', '.', '.', '.'],
        ['.', 'X', 'X', 'X', '.'],
        ['.', '.', '.', '.', '.']
    ]

def initialize_graph():
    return {
        'Node1': [('Node2', 2), ('Node3', 4)],
        'Node2': [('Node4', 3)],
        'Node3': [('Node4', 1), ('Goal', 6)],
        'Node4': [('Goal', 5)],
        'Goal': []
    }

# 2. Search Algorithms

# DFS Implementation
def depth_first_search(grid):
    start_point, end_point = (0, 0), (0, 4)
    stack = [start_point]
    visited_nodes = set()
    path_parent = {}

    while stack:
        current_node = stack.pop()
        if current_node in visited_nodes:
            continue
        visited_nodes.add(current_node)

        if current_node == end_point:
            break

        for neighbor in find_neighbors(grid, current_node):
            if neighbor not in visited_nodes:
                stack.append(neighbor)
                path_parent[neighbor] = current_node

    return construct_path(path_parent, start_point, end_point)

# BFS Implementation
def breadth_first_search(grid):
    start_point, end_point = (0, 0), (0, 4)
    queue = [start_point]
    visited_nodes = set()
    path_parent = {}

    while queue:
        current_node = queue.pop(0)
        if current_node in visited_nodes:
            continue
        visited_nodes.add(current_node)

        if current_node == end_point:
            break

        for neighbor in find_neighbors(grid, current_node):
            if neighbor not in visited_nodes:
                queue.append(neighbor)
                path_parent[neighbor] = current_node

    return construct_path(path_parent, start_point, end_point)

# A* Search Implementation
def a_star_search(grid, metric='manhattan'):
    start_point, end_point = (0, 0), (0, 4)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_point))
    cost_to_node = {start_point: 0}
    path_parent = {}

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        if current_node == end_point:
            break

        for neighbor in find_neighbors(grid, current_node):
            tentative_cost = cost_to_node[current_node] + 1
            if neighbor not in cost_to_node or tentative_cost < cost_to_node[neighbor]:
                cost_to_node[neighbor] = tentative_cost
                if metric == 'manhattan':
                    estimated_cost = tentative_cost + manhattan_metric(neighbor, end_point)
                elif metric == 'euclidean':
                    estimated_cost = tentative_cost + euclidean_metric(neighbor, end_point)
                heapq.heappush(priority_queue, (estimated_cost, neighbor))
                path_parent[neighbor] = current_node

    return construct_path(path_parent, start_point, end_point)

# 3. Helper Functions
def find_neighbors(grid, position):
    x, y = position
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 'X':
            neighbors.append((nx, ny))
    return neighbors

def construct_path(parent, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent.get(current)
        if current is None:
            return []  # No path exists
    path.append(start)
    return list(reversed(path))

def manhattan_metric(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean_metric(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# 4. Visualization
def display_path(grid, path):
    grid_copy = [row[:] for row in grid]
    for x, y in path:
        if grid_copy[x][y] not in ('S', 'G'):
            grid_copy[x][y] = '*'
    for row in grid_copy:
        print(' '.join(row))

def plot_grid_with_path(grid, path, title):
    fig, ax = plt.subplots()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'X':
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color='black'))
            elif (i, j) == (0, 0):
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color='green'))
            elif (i, j) == (0, 4):
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color='red'))
            elif (i, j) in path:
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color='yellow'))
    ax.set_xlim(0, len(grid[0]))
    ax.set_ylim(0, len(grid))
    plt.grid(True)
    plt.title(title)
    plt.show()

# 5. Performance Testing
def evaluate_performance(grid, search_function, *args):
    tracemalloc.start()
    start_time = time.time()
    path = search_function(grid, *args)
    end_time = time.time()
    peak_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    execution_time = end_time - start_time
    return execution_time, peak_memory, len(path), path

# Main Execution
if __name__ == "__main__":
    grid = initialize_grid()
    print("Initial Grid:")
    for row in grid:
        print(' '.join(row))

    print("\nDFS Path:")
    exec_time, memory_used, nodes_expanded, path = evaluate_performance(grid, depth_first_search)
    display_path(grid, path)
    plot_grid_with_path(grid, path, "DFS Algorithm")
    print(f"Execution Time: {exec_time:.6f}s, Memory: {memory_used / 1024:.2f} KB, Nodes Expanded: {nodes_expanded}")

    print("\nBFS Path:")
    exec_time, memory_used, nodes_expanded, path = evaluate_performance(grid, breadth_first_search)
    display_path(grid, path)
    plot_grid_with_path(grid, path, "BFS Algorithm")
    print(f"Execution Time: {exec_time:.6f}s, Memory: {memory_used / 1024:.2f} KB, Nodes Expanded: {nodes_expanded}")

    print("\nA* Path (Manhattan):")
    exec_time, memory_used, nodes_expanded, path = evaluate_performance(grid, a_star_search, 'manhattan')
    display_path(grid, path)
    plot_grid_with_path(grid, path, "A* Algorithm (Manhattan)")
    print(f"Execution Time: {exec_time:.6f}s, Memory: {memory_used / 1024:.2f} KB, Nodes Expanded: {nodes_expanded}")

    print("\nA* Path (Euclidean):")
    exec_time, memory_used, nodes_expanded, path = evaluate_performance(grid, a_star_search, 'euclidean')
    display_path(grid, path)
    plot_grid_with_path(grid, path, "A* Algorithm (Euclidean)")
    print(f"Execution Time: {exec_time:.6f}s, Memory: {memory_used / 1024:.2f} KB, Nodes Expanded: {nodes_expanded}")


