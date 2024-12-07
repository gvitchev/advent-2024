SAMPLE = """3   4
4   3
2   5
1   3
3   9
3   3"""

def solve(input):
    list1, list2 = [], []
    for l in input.splitlines():
        items = l.split()
        list1.append(int(items[0].strip()))
        list2.append(int(items[1].strip()))
    list1.sort()
    list2.sort()
    diff = 0
    for (i, j) in zip(list1, list2):
        diff += abs(i - j)
    return diff

if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))