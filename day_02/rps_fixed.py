PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    lines = f.readlines()

MOVE_POINTS = {
    'A': 1,  # A | Rock
    'B': 2,  # B | Paper
    'C': 3   # C | Scissor
}

OUTCOME_POINTS = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def outcome_move(outcome, opponent):
    if outcome == 'X': # Lose
        if opponent == 'A':
            return 'C'
        elif opponent == 'B':
            return 'A'
        elif opponent == 'C':
            return 'B'
    elif outcome == 'Y': # Draw
        return opponent
    elif outcome == 'Z': # Win
        if opponent == 'A':
            return 'B'
        elif opponent == 'B':
            return 'C'
        elif opponent == 'C':
            return 'A'


total_score = 0
for line in lines:
    opponent = line[0]
    outcome = line[2]
    player = outcome_move(outcome, opponent)
    total_score += MOVE_POINTS[player]
    total_score += OUTCOME_POINTS[outcome]

print(f'According to the plan my final score will be: {total_score}.')
