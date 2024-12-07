import re

SAMPLE = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def add_mul(input):
    sum = 0
    matches = re.findall("mul\((\d+),(\d+)\)", input)
    for m in matches:
        sum += int(m[0]) * int(m[1])
    return sum


def solve(input):
    sum = 0
    while True:
        next_off = input.find("don't()")
        if next_off == -1:
            sum += add_mul(input)
            break
        sum += add_mul(input[:next_off])
        input = input[next_off:]
        next_on = input.find("do()")
        if next_on == -1:
            break
        input = input[next_on:]
    return sum
        

if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))