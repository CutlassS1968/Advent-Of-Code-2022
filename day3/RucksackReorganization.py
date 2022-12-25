import time


def part_one():
    # Each rucksack has two compartments
    # All items of a given type go in exactly one of the compartments
    # Item types range from A-z
    # Items that go into each rucksack are defined by one line in the data file
    # First half of line is items in the first compartment
    # Second half of line is items in the second compartment

    # Each item has a given priority
    # Lowercase item types a through z have priorities 1 through 26
    # Uppercase item types A through Z have priorities 27 through 52

    # Find the item type that is found in both compartments
    # EX: AbCDEBAG
    #     1st = AbCD
    #     2nd = EBAG
    #     Common item is A
    #     'A' has priority 27
    #     We would do this with all lines, and add the priorities together

    p = ['a', 'b', 'c', 'd', 'e',
         'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']

    file = open("data.txt")
    lines = file.readlines()
    s = 0
    for line in lines:
        l0 = line[0:len(line) - 1]  # Remove trailing whitespace
        l1 = line[0:int(len(l0) / 2)]  # Get first part
        l2 = line[int(len(l0) / 2):len(l0)]  # Get second part
        v = sum([p.index(c1) + 1 for c1 in l1 if l2.__contains__(c1)])
        s += v
    return s


def part_two():
    p = ['a', 'b', 'c', 'd', 'e',
         'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']

    file = open("data.txt")
    lines = file.readlines()
    ls = []
    v = []

    for i in range(len(lines)):
        ls.append(lines[i].strip())
        if i % 3 == 2:
            c = list(set(list(set(ls[0]) & set(ls[1]))) & set(list(set(ls[0]) & set(ls[2]))))
            v.append(p.index(c[0]) + 1)
            ls.clear()
    return sum(v)


def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
