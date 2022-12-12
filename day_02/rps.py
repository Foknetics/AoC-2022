PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    lines = f.readlines()

MOVE_POINTS = {
    'X': 1,  # A | Rock
    'Y': 2,  # B | Paper
    'Z': 3   # C | Scissor
}

def outcome_points(opponent, player):
    if opponent == 'A':     # Rock V
        if player == 'X':   # Rock - Draw
            return 3
        elif player == 'Y': # Paper - Win
            return 6
        elif player == 'Z': # Scissor - Loss
            return 0
    elif opponent == 'B':   # Paper V
        if player == 'X':   # Rock - Loss
            return 0
        elif player == 'Y': # Paper - Draw
            return 3
        else:               # Scissor - Win
            return 6
    elif opponent == 'C':   # Scissor V
        if player == 'X':   # Rock - Win
            return 6
        elif player == 'Y': # Paper - Loss
            return 0
        elif player == 'Z': # Scissor - Draw
            return 3


total_score = 0
for line in lines:
    opponent = line[0]
    player = line[2]
    total_score += MOVE_POINTS[player]
    total_score += outcome_points(opponent, player)

print(f'According to the plan my final score will be: {total_score}.')
