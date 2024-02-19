# Task

# A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

# How many points with integer coordinates are located inside the given rectangle (including on its sides)?
# Example

# For a = 6 and b = 4, the output should be 23

# The following picture illustrates the example, and the 23 points are marked green.

# Input/Output

#     [input] integer a

#     A positive even integer.

#     Constraints: 2 ≤ a ≤ 10000.

#     [input] integer b

#     A positive even integer.

#     Constraints: 2 ≤ b ≤ 10000.

#     [output] an integer

#     The number of inner points with integer coordinates.

# Solution:

import math

def rectangle_rotation(a, b):
    ld = (a / math.sqrt(2)) / 2
    sd = (b / math.sqrt(2)) / 2
    rect_ext = [2 * int(ld) + 1, 2 * int(sd) + 1]
    rect_int = [2 * int(ld) + (0 if ld % 1 < 0.5 else 2), 2 * int(sd) + (0 if sd % 1 < 0.5 else 2)]
    return rect_ext[0] * rect_ext[1] + rect_int[0] * rect_int[1]