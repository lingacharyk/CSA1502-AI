import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic (estimated cost from current node to goal node)
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, end):
    open_set = []
    heapq.heappush(open_set, start)
    closed_set = set()
    
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.position == end.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
        
        closed_set.add(current_node.position)
        neighbors = get_neighbors(grid, current_node)
        for neighbor in neighbors:
            if neighbor.position in closed_set:
                continue
            tentative_g = current_node.g + 1  # Assuming the cost to move from one node to its neighbor is 1
            if neighbor not in open_set or tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor.position, end.position)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)
    
    return None  # No path found

def get_neighbors(grid, node):
    neighbors = []
    row, col = node.position
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != 1:
            neighbors.append(Node((new_row, new_col), node))
    return neighbors

def heuristic(pos1, pos2):
    # Manhattan distance heuristic
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Example usage
grid = [[0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]]

start = Node((0, 0))
end = Node((4, 4))

path = astar(grid, start, end)
print(path)
