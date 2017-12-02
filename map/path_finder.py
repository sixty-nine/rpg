from utils import manhattan_distance, PriorityQueue

class PathFinder(object):

    @staticmethod
    def search_path(start, goal, get_neighbors, dist_heuristic = manhattan_distance):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == goal: break

            for next in get_neighbors(current):
                if next not in came_from:
                    priority = dist_heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        if current != goal: return False

        return PathFinder.reconstruct_path(came_from, start, goal)

    @staticmethod
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start) # optional
        path.reverse() # optional
        return path

    @staticmethod
    def search_best_path(from_points, to_points, hm_walkable, grid):
        best = None

        for c1 in from_points:
            for c2 in to_points:
                get_neighbors = PathFinder.dig_wall_neighbors(c2, hm_walkable, grid)
                pf = PathFinder()
                path = pf.search_path(c1, c2, get_neighbors)
                if not best or (path and len(path) < len(best)):
                    best = path

        return best

    @staticmethod
    def dig_wall_neighbors(goal, hm_walkable, grid):

        is_walkable = lambda pos: hm_walkable[pos[0], pos[1]]

        def passable(pos):
            if pos == goal: return True
            if is_walkable(pos): return False
            if grid.neighbors_diag(pos, is_walkable): return False
            return True

        def neighbors(pos):
            return grid.neighbors(pos, passable)

        return neighbors
