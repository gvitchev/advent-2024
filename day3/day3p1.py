import re

SAMPLE = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def solve(input):
    sum = 0
    matches = re.findall("mul\((\d+),(\d+)\)", input)
    for m in matches:
        sum += int(m[0]) * int(m[1])
    return sum


if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))