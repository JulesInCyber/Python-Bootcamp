import time

def create_grid(x, y):
    return [[0 for i in range(10)] for j in range(10)]

def print_grid(grid):
    for row in grid:
        for element in row:
            print(element, end="")
        print()

def spawn_cell(tuple, grid):
    for row, col in tuple:
        grid[row][col] = 1

def count_neighbors(grid, x_pos, y_pos):
    count = 0
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if a == 0 and b == 0:
                continue
            dx = x_pos + a
            dy = y_pos + b
            if 0 <= dx < len(grid) and 0 <= dy < len(grid[1]):
                if grid[dx][dy] == 1:
                    count += 1
    return count


if __name__ == "__main__":

    cells = [(1, 1), (2, 2)]
    g1 = create_grid(10,10)
    spawn_cell(cells, g1)
    print_grid(g1)

    for row in range(len(g1)):
        for col in range(len(g1[1])):
            count_neighbors(g1, row, col)
            print(f"{count_neighbors(g1, row, col)} at {row}, {col}")