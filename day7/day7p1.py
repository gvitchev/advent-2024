SAMPLE="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def works(total, nums):
    possible_values = [nums[0]]
    for i in range(1, len(nums)-1):
        new_possible_values = []
        for v in possible_values:
            new_possible_values.append(v + nums[i])
            new_possible_values.append(v * nums[i])
        possible_values = new_possible_values

    for v in possible_values:
        if v + nums[-1] == total or v * nums[-1] == total:
            return True
    return False

def solve(input):
    total = 0
    for l in input.splitlines():
        line_total = int(l.split(":")[0])
        nums = [int(x) for x in l.split(":")[1].strip().split(" ")]
        if works(line_total, nums):
            total += line_total
    return total


if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))
