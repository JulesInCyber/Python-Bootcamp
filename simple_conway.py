import time

def create_grid(x, y):
    return [["-" for i in range(10)] for j in range(10)]

def print_grid(grid):
    for row in grid:
        for element in row:
            print(element, end="")
        print()

def spawn_cell(tuple, grid):
    for row, col in tuple:
        grid[row][col] = 1


if __name__ == "__main__":

    cells = [(1, 1), (5, 5), (3, 8)]
    g1 = create_grid(10,10)
    spawn_cell(cells, g1)
    print_grid(g1)