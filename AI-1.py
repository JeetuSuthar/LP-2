class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        if start not in visited:
            print(start)
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)


def main():
    g = Graph()
    n = int(input("Enter number of edges: "))
    print("Enter each edge as 'u v':")
    for _ in range(n):
        u, v = input().split()
        g.add_edge(u, v)

    start = input("Start vertex: ")

    print("DFS")
    g.dfs(start)
    print("\nBFS")
    g.bfs(start)

if __name__ == "__main__":
    main()
