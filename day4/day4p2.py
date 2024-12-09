SAMPLE = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# SAMPLE = """ZMZ
# MAS
# ZSZ"""

def has_slash(i, j, data):
    return (data[i-1][j+1], data[i+1][j-1]) in [("S", "M"), ("M", "S")]

def has_backslash(i, j, data):
    return (data[i+1][j+1], data[i-1][j-1]) in [("S", "M"), ("M", "S")]


def is_xmas(i, j, data):
    if i == 0 or j == 0 or len(data) == i + 1 or len(data[i]) == j + 1:
        return False
    if has_slash(i, j, data) and has_backslash(i, j, data):
        return True
    return False

def solve(input):
    data = input.splitlines()
    total = 0
    for i, row in enumerate(data):
        for j, letter in enumerate(row):
            if letter == "A":
                if is_xmas(i, j, data):
                    total += 1
    return total


if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))