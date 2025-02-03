from functions.random import get_random_rc, get_random_rc_of_empty_field
from functions.field_control import Field

# Initialize field
field = Field(4)

# Initialize field with random values
rc = get_random_rc(4)
field.edit_field(rc[0], rc[1], 2)

rc = get_random_rc_of_empty_field(4, field)
field.edit_field(rc[0], rc[1], 2)

from app import worker  # noqa
from app import game  # noqa

g = game.g
