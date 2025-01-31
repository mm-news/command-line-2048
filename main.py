from functions.field_control import Field
from functions.random import get_random_rc

field = Field(4)

# Initialize field with random values
rc = get_random_rc(4)
field.edit_field(rc[0], rc[1], 2)

rc = get_random_rc(4)
field.edit_field(rc[0], rc[1], 2)
