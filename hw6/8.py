import math
from typing import List, Dict
import heapq
import matplotlib.pyplot as plt


class City:
    def __init__(self, id: int, x: float, y: float):
        self.id = id
        self.x = x
        self.y = y

    def distance_to(self, other: 'City') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class CityGraph:
    def __init__(self):
        self.cities: Dict[int, City] = {}
        self.adjacency: Dict[int, List[int]] = {}
        self.raw_data = []

    def add_city(self, id: int, x: float, y: float):
        self.cities[id] = City(id, x, y)
        if id not in self.adjacency:
            self.adjacency[id] = []

    def add_edge(self, city1: int, city2: int):
        if city1 not in self.adjacency:
            self.adjacency[city1] = []
        if city2 not in self.adjacency:
            self.adjacency[city2] = []

        self.adjacency[city1].append(city2)
        self.adjacency[city2].append(city1)

    def get_edge_weight(self, city1: int, city2: int) -> float:
        return self.cities[city1].distance_to(self.cities[city2])

    def dijkstra(self, start: int, end: int) -> tuple[List[int], float]:
        distances = {i: float('inf') for i in self.cities}
        distances[start] = 0
        pq = [(0, start)]
        visited = set()

        parent = {i: None for i in self.cities}

        while pq:
            current_distance, current = heapq.heappop(pq)

            if current == end:
                break

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.adjacency[current]:
                distance = current_distance + self.get_edge_weight(current, neighbor)

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))

        if distances[end] == float('inf'):
            return [], float('inf')

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()

        return path, distances[end]

    def draw_graph(self, shortest_path=None):
        plt.figure(figsize=(12, 8))

        # Draw edges
        for city1 in self.adjacency:
            for city2 in self.adjacency[city1]:
                if city1 < city2:
                    x1, y1 = self.cities[city1].x, self.cities[city1].y
                    x2, y2 = self.cities[city2].x, self.cities[city2].y
                    plt.plot([x1, x2], [y1, y2], 'gray', zorder=1)

        # Draw shortest path
        if shortest_path and len(shortest_path) > 1:
            for i in range(len(shortest_path) - 1):
                city1 = shortest_path[i]
                city2 = shortest_path[i + 1]
                x1, y1 = self.cities[city1].x, self.cities[city1].y
                x2, y2 = self.cities[city2].x, self.cities[city2].y
                plt.plot([x1, x2], [y1, y2], 'red', linewidth=2, zorder=2)

        # Draw nodes
        x_coords = [city.x for city in self.cities.values()]
        y_coords = [city.y for city in self.cities.values()]
        plt.scatter(x_coords, y_coords, c='lightblue', s=500, zorder=3)

        # Add city numbers
        for city_id, city in self.cities.items():
            plt.annotate(f'City {city_id}', (city.x, city.y),
                         xytext=(5, 5), textcoords='offset points')

        # Show raw data in corner
        info_text = "Raw Data:\n"
        info_text += f"Nodes: {self.raw_data[0]}, Edges: {self.raw_data[1]}\n\n"
        info_text += "City Coordinates:\n"
        for line in self.raw_data[2]:
            info_text += f"{line}\n"
        info_text += "\nConnections:\n"
        for line in self.raw_data[3]:
            info_text += f"{line}\n"

        plt.text(0.02, 0.98, info_text,
                 transform=plt.gca().transAxes,
                 verticalalignment='top',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        plt.title("City Graph with Shortest Path")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.grid(True)

        plt.savefig('graph.png')
        print("\nGraph has been saved as 'graph.png'")
        plt.close()


def read_city_graph(filename: str) -> CityGraph:
    graph = CityGraph()

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

            # Read number of nodes and edges
            n_nodes, n_edges = map(int, lines[0].strip().split())
            graph.raw_data.append(n_nodes)
            graph.raw_data.append(n_edges)

            # Read city coordinates
            city_coords = []
            current_line = 2
            for i in range(n_nodes):
                line = lines[current_line + i].strip()
                city_coords.append(line)
                city_id, x, y = map(float, line.split())
                graph.add_city(int(city_id), x, y)
            graph.raw_data.append(city_coords)

            # Read edges
            edges = []
            current_line = current_line + n_nodes + 1
            for i in range(n_edges):
                line = lines[current_line + i].strip()
                edges.append(line)
                city1, city2 = map(int, line.split())
                graph.add_edge(city1, city2)
            graph.raw_data.append(edges)

        return graph
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {str(e)}")


def main():
    filename = input("Please enter the filename: ")

    graph = read_city_graph(filename)
    if graph is None:
        return

    try:
        start_city = int(input("Enter the source city number: "))
        end_city = int(input("Enter the destination city number: "))

        if start_city not in graph.cities or end_city not in graph.cities:
            print("Error: Invalid city number.")
            return

        path, total_distance = graph.dijkstra(start_city, end_city)

        if path:
            print(f"\nShortest path from city {start_city} to city {end_city}:")
            print(f"Path: {' -> '.join(map(str, path))}")
            print(f"Total distance: {total_distance:.2f}")

            graph.draw_graph(path)
        else:
            print(f"\nNo path found between city {start_city} and city {end_city}")
            graph.draw_graph()

    except ValueError:
        print("Error: Please enter valid integers.")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
