from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    # 1. Add vertex
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    # 2. Add edge
    def add_edge(self, src, dest, weight=1):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adj_list[src].append((dest, weight))
        if not self.directed:
            self.adj_list[dest].append((src, weight))

    # 3. Remove vertex
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
        for v in self.adj_list:
            self.adj_list[v] = [(n, w) for (n, w) in self.adj_list[v] if n != vertex]

    # 4. Remove edge
    def remove_edge(self, src, dest):
        self.adj_list[src] = [(n, w) for (n, w) in self.adj_list[src] if n != dest]
        if not self.directed:
            self.adj_list[dest] = [(n, w) for (n, w) in self.adj_list[dest] if n != src]

    # 5. Display
    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} → {neighbors}")

    # 6. DFS
    def dfs(self, start):
        visited = set()
        result = []

        def _dfs(v):
            visited.add(v)
            result.append(v)
            for neighbor, _ in self.adj_list.get(v, []):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return result

    # 7. BFS
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor, _ in self.adj_list.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result
