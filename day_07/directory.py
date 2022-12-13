PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    terminal_output = f.read().splitlines()

directories = {'files': []}
directory_stack = [directories]
for output in terminal_output:
    if output[:4] == '$ cd':
        if output[5:7] == '..':
            directory_stack.pop()
            continue
        cd_name = output[5:]
        if cd_name not in directory_stack[-1]:
            directory_stack[-1][cd_name] = {'files': []}
        directory_stack.append(directory_stack[-1][cd_name])
    elif output[:4] == '$ ls':
        continue

    elif output[:3] == 'dir':
        dir_name = output[4:]
        if dir_name not in directory_stack[-1]:
            directory_stack[-1][dir_name] = {'files': []}

    else:
        size, name = output.split(' ')
        size = int(size)
        directory_stack[-1]['files'].append({'name': name, 'size': size})

# import json
# print(json.dumps(directories, indent=2))

small_directories = []


def folder_size(directory):
    size = sum(file['size'] for file in directory['files'])
    for folder in directory:
        if folder != 'files':
            directory_size = folder_size(directory[folder])
            if directory_size <= 100000:
                small_directories.append(directory_size)
            size += directory_size
    return size


USED_SPACE = folder_size(directories)
print(f'The sum of the small directories is {sum(small_directories)}')

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000
FREE_SPACE = TOTAL_SPACE - USED_SPACE
NEEDED_SPACE = REQUIRED_SPACE - FREE_SPACE

potential_directories = []


def evaluate_for_deletion(directory):
    size = sum(file['size'] for file in directory['files'])
    for folder in directory:
        if folder != 'files':
            directory_size = evaluate_for_deletion(directory[folder])
            if directory_size >= NEEDED_SPACE:
                potential_directories.append(directory_size)
            size += directory_size
    return size


evaluate_for_deletion(directories)

potential_directories.sort()
print(f'We can delete a directory sized {potential_directories[0]} to make room')
