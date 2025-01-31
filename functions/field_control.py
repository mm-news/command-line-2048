from numpy import array, zeros


class Field:
    def __init__(self, size):
        self.field = zeros((size, size), dtype=int)

    def __repr__(self):
        ret = ""
        for i in self.field:
            for j in i:
                ret += f"{j:4}"
            ret += "\n\n"
        return ret

    def edit_field(self, x, y, value):
        self.field[x][y] = value

    def get_field(self):
        return self.field

    def get_field_value(self, x, y):
        return self.field[x][y]

    def __eq__(self, value):
        return self.field == value.field

    def __ne__(self, value):
        return self.field != value.field
