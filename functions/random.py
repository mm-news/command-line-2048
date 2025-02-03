from functions.field_control import Field


def get_random_rc(size):
    from random import randint
    return randint(0, size - 1), randint(0, size - 1)


def get_random_rc_of_empty_field(size: int, field: Field):
    rc = get_random_rc(size)
    if field.get_by_rc(rc[0], rc[1]) == 0:
        return rc
    else:
        return get_random_rc_of_empty_field(size, field)
