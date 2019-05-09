class Grid:
    def __init__(self, width):
        self.width = width
        self.grid = self.create_grid(self.width)

    def create_grid(self, width):
        grid = []

        # One space buffer on each side of the grid, thus (width + 2)
        for i in range(width+2):
            row = []
            for j in range(width+2):
                row.append(Node(i, j, self.width))
            grid.append(row)

        return grid

    def traverse_grid(self):
        routes = 0

        while self.grid[self.width][1].travel["right"] == True:
            idx = 0
            idy = 1
            last_move = None
            print("Starting at col: {} and row: {}".format(idy, idx))
            while idx < self.width and idy <= self.width +1:
                if self.grid[idx][idy].travel["right"] is not False:
                    if last_move == "right":
                        self.grid[idx][idy].travel["right"] = False

                    idy += 1

                    last_move = "right"

                    print("Moving right to col: {} and row: {}".format(idy, idx))
                else:


                    idx += 1

                    last_move = "down"

                    print("Moving down to col: {} and row: {}".format(idy, idx))

            if routes == 6:
                break
            routes += 1
            print("----------------------------------")

        print(routes)



class Node:
    def __init__(self, x, y, width):
        self.travel = {"up": True,
                         "right": True,
                         "down": True,
                         "left": True}
        if x == 0:
            self.travel["up"] = False
        if x == width:
            self.travel["down"] = False
        if x == (width + 1):
            self.travel["down"] = False
        if y == 0:
            self.travel["left"] = False
        if y == width + 1:
            self.travel["right"] = False



if __name__ == "__main__":
    grid = Grid(3)
    grid.traverse_grid()
