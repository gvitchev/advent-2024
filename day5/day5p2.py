SAMPLE = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def is_valid(update, rules):
    nums_so_far = set()
    for num in update:
        if num in rules:
            if any(x in nums_so_far for x in rules[num]):
                return False
        nums_so_far.add(num)
    return True

def fixed_value(update, rules):
    for i in range(len(update)):
        if update[i] not in rules:
            continue
        for j, prev_num in enumerate(update[:i]):
            if update[i] in rules and prev_num in rules[update[i]]:
                tmp = update[i]
                for x in range(i, j, -1):
                    update[x] = update[x-1]
                update[j] = tmp
    return update[len(update)//2]
                

def solve(input):
    updates = []
    rules = {}
    for l in input.splitlines():
        if "|" in l:
            x, y = (int(i) for i in l.split("|"))
            if x not in rules:
                rules[x] = set()
            rules[x].add(y)
        if "," in l:
            updates.append([int(x) for x in l.split(",")])

    total = 0
    for update in updates:
        if not is_valid(update, rules):
            total += fixed_value(update, rules)
    return total


if __name__ == "__main__":
    print(solve(SAMPLE))
    file = open("input.txt", "r")
    content = file.read()
    print(solve(content))