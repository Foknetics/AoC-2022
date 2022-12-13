PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    tree_map_data = f.read().splitlines()

ROWS = len(tree_map_data)
COLS = len(tree_map_data[0])

tree_map = {}
for y, row in enumerate(tree_map_data):
    for x, tree_height in enumerate(row):
        tree_map[(x, y)] = int(tree_height)


def visible(coord):
    x, y == coord
    height = tree_map[(x, y)]

    west_row = [tree_map[(adjacent_x, y)] for adjacent_x in range(0, x)]
    east_row = [tree_map[(adjacent_x, y)] for adjacent_x in range(x+1, COLS)]
    north_col = [tree_map[(x, adjacent_y)] for adjacent_y in range(0, y)]
    south_col = [tree_map[(x, adjacent_y)] for adjacent_y in range(y+1, ROWS)]

    # Visible from west
    if len([tree for tree in west_row if tree >= height]) == 0:
        return True
    # Visible from east
    if len([tree for tree in east_row if tree >= height]) == 0:
        return True
    # Visible from north
    if len([tree for tree in north_col if tree >= height]) == 0:
        return True
    # Visble from south
    if len([tree for tree in south_col if tree >= height]) == 0:
        return True

    return False


visible_map = {}
for y in range(ROWS):
    for x in range(COLS):
        visible_map[(x, y)] = visible((x, y))


# for y in range(ROWS):
#     print(''.join(['V' if visible_map[(x, y)] else 'H' for x in range(COLS)]))


print(f'There are {len([tree for tree in visible_map if visible_map[tree]])} trees visible from outside the grid')


def directional_score(tree_line, height):
    score = 0
    while len(tree_line):
        score += 1
        next_tree = tree_line.pop()
        if next_tree >= height:
            break

    return score


def scenic_score(coord):
    x, y == coord
    height = tree_map[(x, y)]

    west_row = [tree_map[(adjacent_x, y)] for adjacent_x in range(0, x)]
    east_row = [tree_map[(adjacent_x, y)] for adjacent_x in range(x+1, COLS)][::-1]
    north_col = [tree_map[(x, adjacent_y)] for adjacent_y in range(0, y)]
    south_col = [tree_map[(x, adjacent_y)] for adjacent_y in range(y+1, ROWS)][::-1]

    west_score = directional_score(west_row, height)
    east_score = directional_score(east_row, height)
    north_score = directional_score(north_col, height)
    south_score = directional_score(south_col, height)

    return west_score * east_score * north_score * south_score


scenic_map = {}
for y in range(ROWS):
    for x in range(COLS):
        scenic_map[(x, y)] = scenic_score((x, y))

print(f'The most scenic tree has a scenic score of {max([scenic_map[coord] for coord in scenic_map])}')
