from numpy import array, zeros


class Field:
    def __init__(self, size):
        self.field = zeros((size, size), dtype=int)
        self.size = size

    def __repr__(self):
        ret = ""
        for i in self.field:
            for j in i:
                ret += f"{j:4}"
            ret += "\n\n"
        return ret

    def edit_field(self, r, c, value):
        self.field[r][c] = value

    def get_field(self):
        return self.field

    def get_by_rc(self, r, c, zero_based=True):
        return self.field[r][c] if zero_based else self.field[r - 1][c - 1]

    def __eq__(self, value):
        return self.field == value.field

    def __ne__(self, value):
        return self.field != value.field

    def __getitem__(self, key):
        return self.field[key]

    # Moving functions
    # TODO: - Make them recursive to do all the moves in one turn
    # TODO: - Check if the two cells are the same before merging

    def move(self, source: tuple, destination: tuple, method: str):
        if method == "merge":
            self.field[destination[0]][destination[1]
                                       ] += self.field[source[0]][source[1]]
            self.field[source[0]][source[1]] = 0
        elif method == "replace":
            self.field[destination[0]][destination[1]
                                       ] = self.field[source[0]][source[1]]
            self.field[source[0]][source[1]] = 0
        elif method == "swap":
            self.field[destination[0]][destination[1]], self.field[source[0]][source[1]] = \
                self.field[source[0]][source[1]
                                      ], self.field[destination[0]][destination[1]]
            # TODO: Make it more readable
        else:
            raise ValueError("Invalid method")

    def move_up(self):
        for c in range(self.size):
            for r in range(self.size-1):
                self.move((r+1, c), (r, c), "merge")

    def move_down(self):
        for c in range(self.size):
            for r in range(self.size-1, 0, -1):
                self.move((r-1, c), (r, c), "merge")

    def move_left(self):
        for r in range(self.size):
            for c in range(self.size-1):
                self.move((r, c+1), (r, c), "merge")

    def move_right(self):
        for r in range(self.size):
            for c in range(self.size-1, 0, -1):
                self.move((r, c-1), (r, c), "merge")
