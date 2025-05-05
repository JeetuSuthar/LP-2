import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    closed_set = set()
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        closed_set.add(current_node.position)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)
            if (0 <= neighbor_pos[0] < rows and
                0 <= neighbor_pos[1] < cols and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):
                g_cost = current_node.g + 1
                h_cost = heuristic(neighbor_pos, goal)
                neighbor_node = Node(neighbor_pos, current_node, g_cost, h_cost)
                heapq.heappush(open_set, neighbor_node)
    return None

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)
path = a_star_search(grid, start, goal)
print("Shortest Path:", path)
