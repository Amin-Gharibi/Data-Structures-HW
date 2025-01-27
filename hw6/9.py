from seven import Graph

class ExtendedGraph(Graph):
    def count_and_print_paths(self, start: int, end: int) -> None:
        if not (0 <= start < self.n and 0 <= end < self.n):
            print("Invalid vertices.")
            return

        visited = [False] * self.n
        path = []
        all_paths = []

        def dfs(current, target, visited, path):
            visited[current] = True
            path.append(current)

            if current == target:
                all_paths.append(path.copy())
            else:
                for neighbor in self.adj[current]:
                    if not visited[neighbor]:
                        dfs(neighbor, target, visited, path)

            path.pop()
            visited[current] = False

        dfs(start, end, visited, path)

        print(f"Total paths between {start} and {end} are {len(all_paths)}")
        print("Explanation:")
        if all_paths:
            print(f"The {len(all_paths)} paths between {start} and {end} are:")
            for p in all_paths:
                print(" -> ".join(map(str, p)))
        else:
            print(f"No paths exist between {start} and {end}.")


if __name__ == "__main__":
    graph = ExtendedGraph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)

    graph.count_and_print_paths(0, 4)