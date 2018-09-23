PARSE1 = '#'
PARSE_1 = ' '
ignored = "\n"


def parse_txt_to_shape(__input_file: str, __size: int) -> list:
    file = open(__input_file, "r+")
    lines = file.readlines()
    file.close()
    result = []
    for line in lines:
        line = line.replace(ignored, "")
        for char in line:
            if char == PARSE1:
                result.append(1)
            elif char == PARSE_1:
                result.append(-1)

        if len(line) < __size:
            for _ in range(len(line), __size):
                result.append(-1)
    return result


def from_shape_to_txt(__shape: list, __output_path: str, __size: int):
    assert len(__shape) == __size ** 2
    file = open(__output_path, "w+")
    lines = []
    for i in range(0, __size):
        line = ""
        for value in __shape[i * __size:(i + 1) * __size]:
            if value == 1:
                line += PARSE1
            elif value == -1:
                line += PARSE_1
        lines.append(line + "\n")
    file.writelines(lines)
