from json import loads, dumps


class ASTAR:

    def __init__(self) -> None:
        self.start = None
        self.end   = None

    def __del__(self) -> None:
        if self.start is not None and self.end is not None:
            self.start = None
            self.end   = None


    def setStartingPoint(self, start):
        self.start = start

    def setEndingPoint(self, end):
        self.end = end


class Node:
    def __init__(self, x, y, g_cost=0, h_cost=0, parent=None):
        self.x = x
        self.y = y
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent
        self.f_cost = self.g_cost + self.h_cost

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def get_neighbors(self, grid):
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = self.x + dx, self.y + dy

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                neighbors.append(Node(x, y, parent=self))

        return neighbors

    def get_path(self):
        path = [(self.x, self.y)]
        node = self

        while node.parent is not None:
            path.append((node.parent.x, node.parent.y))
            node = node.parent

        return path[::-1]


def a_star(start, end, grid):
    open_set    = set()
    closed_set  = set()
    open_set.add(start)

    while open_set:
        current = min(open_set, key=lambda node: node.f_cost)

        if current == end:
            return current.get_path()

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in current.get_neighbors(grid):
            if neighbor in closed_set:
                continue

            if neighbor in open_set:
                if neighbor.g_cost > current.g_cost + 1:
                    neighbor.g_cost = current.g_cost + 1
                    neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                    neighbor.parent = current
            else:
                neighbor.g_cost = current.g_cost + 1
                neighbor.h_cost = abs(end.x - neighbor.x) + abs(end.y - neighbor.y)
                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                neighbor.parent = current
                open_set.add(neighbor)

    return []
