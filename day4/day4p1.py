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

def get_count(i, j, data):
    total = 0
    if len(data[i]) > j + 3:
        if data[i][j+1:j+4] == "MAS":
            total += 1
    if j > 2:
        if data[i][j-3:j] == "SAM":
            total += 1
        
    if len(data) > i + 3:
        if data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
            total += 1
    if i > 2:
        if data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
            total += 1

    if len(data[i]) > j + 3 and len(data) > i + 3:
        if data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
            total += 1
    if len(data[i]) > j + 3 and i > 2:
        if data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
            total += 1
    if j > 2 and len(data) > i + 3:
        if data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
            total += 1
    if j > 2 and i > 2:
        if data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
            total += 1
    return total

def solve(input):
    data = input.splitlines()
    total = 0
    for i, row in enumerate(data):
        for j, letter in enumerate(row):
            if letter == "X":
                total += get_count(i, j, data)
    return total


if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))