PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    commands = f.read().splitlines()


def delay(command):
    if command == 'noop':
        return 1
    return 2


register = 1
command_index = -1
command = None
cpu_delay = delay(command)
cycle = 0
row = ''
more_commands = True

sprite_locations = [register-1, register, register+1]
# print(f'Sprite position:', ''.join(['#' if loc in sprite_locations else '.' for loc in range(0, 40)]))

while more_commands:
    # print()
    if command is None:
        command_index += 1
        try:
            command = commands[command_index]
            cpu_delay = delay(command)
            # print(f'Start cycle {cycle+1}: begin executing {command}')
        except IndexError:
            more_commands = False

    # print(f'During cycle {cycle+1}: CRT draws pixel in position {cycle}')

    if len(row) == 40:
        print(row)
        row = ''

    if cycle%40 in sprite_locations:
        row += '#'
    else:
        row += '.'
    # print(f'Current CRT Row: {row}')
    # print()


    cpu_delay -= 1
    if cpu_delay == 0:
        if command != 'noop':
            _, arg = command.split(' ')
            arg = int(arg)
            register += arg
            # print(f'End of cycle {cycle+1}: finish executing {command} (Register is now {register})')
            sprite_locations = [register-1, register, register+1]
            # print(f'Sprite position:', ''.join(['#' if loc in sprite_locations else '.' for loc in range(0, 40)]))
        # else:
            # print(f'End of cycle {cycle+1}: finish executing {command}')
        command = None
    cycle += 1
