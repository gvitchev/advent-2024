SAMPLE = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def is_safe(levels, can_skip=True):
    if levels[0] == levels[1] or abs(levels[1] - levels[0]) > 3:
        return False
    last = levels[1]
    inc = levels[1] > levels[0]
    for i in levels[2:]:
        if inc:
            if i <= last or i > last + 3:
                if can_skip:
                    can_skip = False
                    continue
                else:
                    return False
        else:
            if i >= last or i < last - 3:
                if can_skip:
                    can_skip = False
                    continue
                else:
                    return False
        last = i
    return True

def solve(input):
    safe = 0
    for l in input.splitlines():
        levels = [int(x.strip()) for x in l.split()]
        if is_safe(levels) or is_safe(levels[1:], False) or is_safe([levels[0]] + levels[2:], False):
              safe += 1
    return safe


if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))