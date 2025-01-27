from random import random
import heapq
from typing import List, Set, Dict


class Graph:
    def __init__(self, n: int) -> None:
        self.n = n
        self.adj = [[] for _ in range(n)]  # Adjacency list
        self.weighted_edges = {}  # (u, v) -> weight

    def __str__(self) -> str:
        result = "From  To\n"
        for i in range(self.n):
            result += f"{i}:    {','.join(map(str, sorted(self.adj[i])))}\n"
        return result

    def add_edge(self, i: int, j: int, weight: float = 1.0) -> bool:
        if not (0 <= i < self.n and 0 <= j < self.n) or i == j:
            return False
        if j in self.adj[i]:  # Edge already exists
            return False

        self.adj[i].append(j)
        self.adj[j].append(i)
        self.weighted_edges[(i, j)] = weight
        self.weighted_edges[(j, i)] = weight
        return True

    def is_connected(self) -> bool:
        if self.n == 0:
            return True

        visited = set()
        self._dfs_helper(0, visited)
        return len(visited) == self.n

    def _dfs_helper(self, node: int, visited: Set[int]) -> None:
        visited.add(node)
        for neighbor in self.adj[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

    def clear(self):
        self.adj = [[] for _ in range(self.n)]
        self.weighted_edges.clear()

    def randomize(self, p: float) -> None:
        self.weighted_edges.clear()
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if random() <= p:
                    self.add_edge(i, j)

    @staticmethod
    def run_tests(size: int, p0: float, p1: float, steps: int, k: int) -> None:
        d = (p1 - p0) / steps
        g = Graph(size)

        for step in range(steps + 1):
            p = p0 + step * d
            count = 0

            for _ in range(k):
                g.randomize(p)
                if g.is_connected():
                    count += 1

            print(f"p = {p:.3f}    fraction connected = {count / k:.3f}")

    def dfs(self, a: int) -> List[int]:
        visited = set()
        result = []

        def dfs_recursive(node):
            visited.add(node)
            result.append(node)
            for neighbor in sorted(self.adj[node]):  # Sort for consistent output
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(a)
        return result

    def dijkstra(self, start: int) -> Dict[int, float]:
        distances = {i: float('infinity') for i in range(self.n)}
        distances[start] = 0
        pq = [(0, start)]
        visited = set()

        while pq:
            current_distance, current = heapq.heappop(pq)

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.adj[current]:
                distance = current_distance + self.weighted_edges[(current, neighbor)]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def bellman_ford(self, start: int) -> Dict[int, float]:
        distances = {i: float('infinity') for i in range(self.n)}
        distances[start] = 0

        for _ in range(self.n - 1):
            for (u, v), weight in self.weighted_edges.items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Check for negative cycles
        for (u, v), weight in self.weighted_edges.items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

        return distances

    def prim(self) -> List[tuple]:
        if not self.is_connected():
            raise ValueError("Graph is not connected")

        mst = []
        visited = {0}  # Start with node 0
        edges = [] # priority queue

        # Add all edges from starting node
        for neighbor in self.adj[0]:
            heapq.heappush(edges, (self.weighted_edges[(0, neighbor)], 0, neighbor)) # format: weight, from_node, to_node

        while edges and len(visited) < self.n:
            weight, u, v = heapq.heappop(edges)

            if v in visited:
                continue

            visited.add(v)
            mst.append((u, v, weight))

            # Add new edges to consideration
            for neighbor in self.adj[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (self.weighted_edges[(v, neighbor)], v, neighbor))

        return mst

    def kruskal(self) -> List[tuple]:
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, rank, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        mst = []
        edges = []
        for (u, v), weight in self.weighted_edges.items():
            if u < v:  # Add each edge only once
                edges.append((weight, u, v))

        edges.sort()  # Sort edges by weight

        parent = list(range(self.n)) # create a list of all nodes
        rank = [0] * self.n

        for weight, u, v in edges:
            if find(parent, u) != find(parent, v):
                mst.append((u, v, weight))
                union(parent, rank, u, v)

        return mst


if __name__ == "__main__":
    graph = Graph(10)
    # you can test methods here