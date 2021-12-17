###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 17
data_str = """target area: x=20..30, y=-10..-5"""


def simulate(x_min, x_max, y_min, y_max, x_vel, y_vel):
    x = 0
    y = 0
    max_y = 0

    while 1:
        x += x_vel
        y += y_vel

        if y_vel < 0 and y < y_min:
            return 0

        if x >= x_min and x <= x_max and y <= y_max and y >= y_min:
            return max_y

        if x_vel > 0:
            x_vel -= 1
        if x_vel < 0:
            x_vel += 1

        if y > max_y:
            max_y = y
        
        y_vel -= 1


def task(data_set: list[str]) -> int:
    [_, coordinates] = data_set[0].split(": ")
    [x, y] = coordinates.split(", ")
    x = x[2:]
    [x1, x2] = x.split("..")
    y = y[2:]
    [y1, y2] = y.split("..")
    
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)

    max_y = 0
    for x_vel in range(100):
        for y_vel in range(100):
            next_y = simulate(x_min, x_max, y_min, y_max, x_vel, y_vel)
            if next_y > max_y:
                max_y = next_y

    return max_y
    

aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
