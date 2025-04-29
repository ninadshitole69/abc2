import heapq
import math

ROWS, COLS = 9, 10

class cell:
    def __init__(self):  # Fixed constructor
        self.parent = None
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')

def is_valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def heuristic(r, c, end):
    return math.hypot(r - end[0], c - end[1])

def trace_path(cell_info, dest):
    path = []
    r, c = dest
    while cell_info[r][c].parent:
        path.append((r, c))
        r, c = cell_info[r][c].parent
    path.append((r, c))
    path.reverse()
    print('Path:', path)

def a_star(grid, start, end):
    open_list = []
    visited = [[False] * COLS for _ in range(ROWS)]
    cell_info = [[cell() for _ in range(COLS)] for _ in range(ROWS)]

    sr, sc = start
    cell_info[sr][sc].g = 0
    cell_info[sr][sc].h = heuristic(sr, sc, end)
    cell_info[sr][sc].f = cell_info[sr][sc].h
    cell_info[sr][sc].parent = None
    heapq.heappush(open_list, (cell_info[sr][sc].f, sr, sc))

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1),
             (-1, -1), (1, 1), (1, -1), (-1, 1)]

    while open_list:
        _, r, c = heapq.heappop(open_list)
        if (r, c) == end:
            trace_path(cell_info, end)
            return
        visited[r][c] = True
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and grid[nr][nc] and not visited[nr][nc]:
                g = cell_info[r][c].g + 1
                h = heuristic(nr, nc, end)
                f = g + h
                if f < cell_info[nr][nc].f:
                    cell_info[nr][nc].g = g
                    cell_info[nr][nc].h = h
                    cell_info[nr][nc].f = f
                    cell_info[nr][nc].parent = (r, c)
                    heapq.heappush(open_list, (f, nr, nc))
                    print(f"Updated Cell ({nr}, {nc}) -> g: {g:.2f}, h: {h:.2f}, f: {f:.2f}")
    print('No path found!')

def main():
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]
    start, end = (8, 0), (0, 0)
    a_star(grid, start, end)

if __name__ == "__main__":
    main()
