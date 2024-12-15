SAMPLE="""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

def is_exiting(graph, pos, dir):
    if pos[0] == 0 and dir == UP:
        return True
    if pos[0] == len(graph)-1 and dir == DOWN:
        return True
    if pos[1] == 0 and dir == LEFT:
        return True
    if pos[1] == len(graph[pos[0]]) -1 and dir == RIGHT:
        return True
    return False

def get_new_pos(curr, dir):
    if dir == UP:
        return (curr[0] - 1, curr[1])
    elif dir == DOWN:
        return (curr[0] + 1, curr[1])
    elif dir == LEFT:
        return (curr[0], curr[1] - 1)
    else:
        return (curr[0], curr[1] + 1)

def new_dir(dir):
    if dir == UP:
        return RIGHT
    if dir == RIGHT:
        return DOWN
    if dir == DOWN:
        return LEFT
    if dir == LEFT:
        return UP

def is_loop(base_graph, start, block):
    graph = [i.copy() for i in base_graph]
    graph[block[0]][block[1]] = "#"
    visited = set()
    curr = start
    dir = UP
    i = 0
    while True:
        i += 1
        if i > 10000:
            print(i, block)
            break
        row, col = curr
        if (row, col, dir) in visited:
            return True
        visited.add((row, col, dir))
        if is_exiting(graph, curr, dir):
            return False
        j = 0
        while True:
            j += 1
            if j > 4:
                print(j, block, start, curr, dir)
                return False
            tmp = get_new_pos(curr, dir)
            if graph[tmp[0]][tmp[1]] == "#":
                dir = new_dir(dir)
            else:
                break
        curr = tmp


def solve(input):
    graph = []
    for i, l in enumerate(input.splitlines()):
        if "^" in l:
            j = l.index("^")
            start = (i, j)
            l.replace("^", ".")
        graph.append(list(l))

    visited = set()
    curr = start
    dir = UP
    while True:
        visited.add(curr)
        if is_exiting(graph, curr, dir):
            break
        while True:
            tmp = get_new_pos(curr, dir)
            if graph[tmp[0]][tmp[1]] == "#":
                dir = new_dir(dir)
            else:
                break
        curr = tmp

    total = 0
    for node in visited:
        if is_loop(graph, start, node):
            total += 1

    return total


if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))
