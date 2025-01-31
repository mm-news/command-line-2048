def get_random_rc(size):
    from random import randint
    return randint(0, size - 1), randint(0, size - 1)


def get_random_rc_of_empty_field(size, field):
    rc = get_random_rc(size)
    if field.get_field_value(rc[0], rc[1]) == 0:
        return rc
    else:
        return get_random_rc_of_empty_field(size, field)
