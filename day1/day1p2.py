SAMPLE = """3   4
4   3
2   5
1   3
3   9
3   3"""

def solve(input):
    list = []
    list2_counts = {}
    for l in input.splitlines():
        items = l.split()
        list.append(int(items[0].strip()))
        val2 = int(items[1].strip())
        if val2 in list2_counts:
            list2_counts[val2] += 1
        else:
            list2_counts[val2] = 1
    diff = 0
    for i in list:
        if i in list2_counts:
            diff += list2_counts[i] * i
    return diff

if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))