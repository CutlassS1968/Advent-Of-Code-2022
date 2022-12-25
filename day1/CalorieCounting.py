def part_one():
    text = open("data.txt", "r")
    lines = text.readlines()
    e = 1
    v = 0
    elves = {}

    for line in lines:
        if line == '\n':
            e += 1
            v = 0
        else:
            line.strip().split("\n")
            v += int(line)
            elves[f"{e}"] = v

    me = 0
    mc = 0
    for k in elves:
        m = max(mc, elves[k])
        if m > mc:
            mc = m
            me = k

    print("Elf {0} has {1}".format(me, mc))
    text.close()


def part_two():
    text = open("data.txt", "r")
    lines = text.readlines()
    e = 1
    v = 0
    elves = {}

    for line in lines:
        if line == '\n':
            e += 1
            v = 0
        else:
            line.strip().split("\n")
            v += int(line)
            elves[f"{e}"] = v
    max_value = 0
    max_keys = []
    for c in range(3):
        max_key = max(elves, key=elves.get)
        max_value += elves[max_key]
        max_keys.append(max_key)
        elves.pop(max_key)

    print("Elves {0}, {1}, and {2} have the most calories; Their total being {3}".format(max_keys[0], max_keys[1],
                                                                                         max_keys[2], max_value))
    text.close()


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
