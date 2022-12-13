PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    tree_map_data = f.read().splitlines()

ROWS = len(tree_map_data)
COLS = len(tree_map_data[0])

tree_map = {}
visible_map = {}
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


for y in range(ROWS):
    for x in range(COLS):
        visible_map[(x, y)] = visible((x, y))


for y in range(ROWS):
    print(''.join(['V' if visible_map[(x, y)] else 'H' for x in range(COLS)]))


print(f'There are {len([tree for tree in visible_map if visible_map[tree]])} trees visible from outside the grid')
