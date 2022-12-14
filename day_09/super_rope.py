import math
import json

PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    rope_movement_data = f.read().splitlines()


def adjacent_coords(coord):
    coords = []
    for y_offset in range(1, -2, -1):
        for x_offset in range(-1, 2):
            coords.append((coord[0] + x_offset, coord[1] + y_offset))
    return coords


def distance(coord_1, coord_2):
    x1, y1 = coord_1
    x2, y2 = coord_2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

knots = {}

for knot in range(10):
    knots[knot] = {'x': 0, 'y': 0}

tail_locations = [(0, 0)]

for move in rope_movement_data:
    print(f'=={move}==')
    direction, steps = move.split(' ')
    steps = int(steps)
    for steps in range(0, steps):
        if direction == 'L':
            knots[0]['x'] -= 1
        elif direction == 'R':
            knots[0]['x'] += 1
        elif direction == 'U':
            knots[0]['y'] += 1
        elif direction == 'D':
            knots[0]['y'] -= 1

        for knot in range(1, 10):
            adjacent_to_next = adjacent_coords((knots[knot-1]['x'], knots[knot-1]['y']))
            if (knots[knot]['x'], knots[knot]['y']) not in adjacent_to_next:
                potential_moves = adjacent_coords((knots[knot]['x'], knots[knot]['y']))
                viable_moves = list(set(adjacent_to_next).intersection(set(potential_moves)))
                viable_moves = sorted(viable_moves, key=lambda move: distance(move, (knots[knot-1]['x'], knots[knot-1]['y'])))
                knots[knot]['x'] = viable_moves[0][0]
                knots[knot]['y'] = viable_moves[0][1]
                if knot == 9:
                    tail_locations.append((knots[knot]['x'], knots[knot]['y']))

    known_coords = {}
    for knot in knots:
        if (knots[knot]['x'], knots[knot]['y']) in known_coords:
            continue
        known_coords[(knots[knot]['x'], knots[knot]['y'])] = knot

    for row in range(15, -15, -1):
        row_output = ''
        for col in range(-15, 15):
            if (col, row) == (0, 0):
                row_output += 'S'
                continue
            if (col, row) in known_coords:
                if known_coords[(col, row)] == 0:
                    row_output += 'H'
                else:
                    row_output += str(known_coords[(col, row)])
            else:
                row_output += '.'
        print(row_output)
    print()

tail_locations = list(set(tail_locations))
print(f'Tail visited {len(tail_locations)} locations.')
for row in range(15, -15, -1):
    row_output = ''
    for col in range(-15, 15):
        if (col, row) == (0, 0):
            row_output += 'S'
            continue
        if (col, row) in tail_locations:
            row_output += '#'
        else:
            row_output += '.'
    print(row_output)
print()
