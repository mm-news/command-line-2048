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

    def edit_field(self, r, c, value):
        self.field[r][c] = value

    def get_field(self):
        return self.field

    def get_field_value(self, r, c, zero_based=True):
        return self.field[r][c] if zero_based else self.field[r - 1][c - 1]

    def __eq__(self, value):
        return self.field == value.field

    def __ne__(self, value):
        return self.field != value.field
