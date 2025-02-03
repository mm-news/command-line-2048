from functions.random import get_random_rc, get_random_rc_of_empty_field


def init_field(field):
    """Initialize field with random values"""
    rc = get_random_rc(4)
    field.edit_field(rc[0], rc[1], 2)

    rc = get_random_rc_of_empty_field(4, field)
    field.edit_field(rc[0], rc[1], 2)

    return field
