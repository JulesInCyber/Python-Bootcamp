import time

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for x in range(width)] for y in range(height)]
        

    def __str__(self):
        return '\n'.join(''.join(str(cell) for cell in row) for row in self.grid)
    
    def spawn_cell(self, x_pos, y_pos):
        spawn = self.grid[x_pos][y_pos].alive = True
        return spawn
    
    def count_neighbors(self, x_pos, y_pos):
        count = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                dx = x_pos + x
                dy = y_pos + y
                if 0 <= dx < self.width and 0 <= dy < self.height:
                    if self.grid[dx][dy].alive == True:
                        count +=1
        return count
    
    def next_gen(self):
        for y_pos in range(self.height):
            for x_pos in range(self.width):
                alive = self.grid[y_pos][x_pos].alive
                neighbors = self.count_neighbors(y_pos, x_pos)
                pass

    
class Cell:
    def __init__(self, x_pos, y_pos, alive=False):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.alive = alive
    
    def __str__(self):
        return "0" if self.alive else "."

if __name__ == "__main__":
    g1 = Grid(10, 10)
    # print(g1)
    g1.spawn_cell(2, 2)
    for x in range(g1.width):
        for y in range(g1.height):
            g1.count_neighbors(x, y)
            print(f"{g1.count_neighbors(x,y)} at [{x}, {y}]")