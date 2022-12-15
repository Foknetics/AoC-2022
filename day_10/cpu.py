PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    commands = f.read().splitlines()


def delay(command):
    if command == 'noop':
        return 1
    return 2


if commands[-1] == 'noop':
    max_cycles = len(commands) + 1
else:
    max_cycles = len(commands) + 2

signal_strengths = {}
register = 1
command_index = 0
command = commands[command_index]
cpu_delay = delay(command)
cycle = 1
while True:
    signal_strengths[cycle] = register*(cycle)
    # print(f'Start of cycle {cycle+1}, R1: {register}')
    # print(command)
    cpu_delay -= 1
    if cpu_delay == 0:
        if command != 'noop':
            _, arg = command.split(' ')
            arg = int(arg)
            register += arg
        # print('finished')
        command_index += 1
        try:
            command = commands[command_index]
        except IndexError:
            break
        cpu_delay = delay(command)
    cycle += 1

key_strengths = [signal_strengths[cycle+20] for cycle in range(0, 201, 40)]
# print(key_strengths)
total_strength = sum(key_strengths)
print(f'Total Strength is: {total_strength}')
