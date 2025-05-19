from collections import deque

def bfs(start, goal, walls, width, height):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if (x, y) == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            next_pos = (nx, ny)
            if 0 <= nx < width and 0 <= ny < height and next_pos not in walls and next_pos not in visited:
                visited.add(next_pos)
                queue.append(path + [next_pos])
    return [start]
