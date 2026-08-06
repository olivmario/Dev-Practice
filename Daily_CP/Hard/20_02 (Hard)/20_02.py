def length_longest_path(input: str) -> int:
    max_length = 0
    path_len = {0: 0}

    for line in input.split('\n'):
        depth = line.count('\t')
        name = line.lstrip('\t')

        current_length = path_len[depth] + len(name)

        if '.' in name:
            max_length = max(max_length, current_length)
        else:
            path_len[depth + 1] = current_length + 1

    return max_length