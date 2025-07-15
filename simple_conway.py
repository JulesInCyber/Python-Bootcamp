import time

def create_grid(x, y):
    return [['.' for i in range(10)] for j in range(10)]

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

def next_gen(current_grid):
    rows = len(current_grid)
    cols = len(current_grid[0])
    new_grid = [['.' for _ in range(cols)] for _ in range(rows)]

    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(current_grid,x,y)
            if current_grid[x][y] == 1 and neighbors in [2, 3]:
                new_grid[x][y] = 1 # stays alive
                # print(f"Next Gen of {x},{y}: Alive")
            elif current_grid[x][y] == '.' and neighbors == 3:
                new_grid[x][y] = 1 # born
                # print(f"Next Gen of {x},{y}: Born")
            else:
                new_grid[x][y] = '.' # dies
                # print(f"Next Gen of {x},{y}: Dead") 
    return new_grid

if __name__ == "__main__":

    # Oscillating Forms
    blinker = [(1, 1), (1, 2), (1, 3)]
    clock = [(1, 1),(1, 2),(0, 3), (2, 3), (2,4),(3,2)]
    
    g1 = create_grid(10,10)
    spawn_cell(clock, g1)

    for i in range(10):
        print(f"\nGeneration {i}")
        print_grid(g1)
        g1 = next_gen(g1)
        time.sleep(1)
