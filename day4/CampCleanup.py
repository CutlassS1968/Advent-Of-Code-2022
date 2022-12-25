# Had some help from this person: https://www.reddit.com/r/adventofcode/comments/zc0zta/comment/izkd8yb/?utm_source=share&utm_medium=web2x&context=3


def part_one():
    file = open('data.txt')
    lines = file.readlines()
    c = 0
    for line in lines:
        ln = line.replace('-', ' ').replace(',', ' ').strip()
        nn = ([int(c) for c in ln.split(' ')])
        s1 = set(range(nn[0], nn[1] + 1))
        s2 = set(range(nn[2], nn[3] + 1))
        if len(s1 & s2) == len(s1) or len(s1 & s2) == len(s2):
            c += 1
    return c


def part_two():
    file = open('data.txt')
    lines = file.readlines()
    c = 0
    for line in lines:
        ln = line.replace('-', ' ').replace(',', ' ').strip()
        nn = ([int(c) for c in ln.split(' ')])
        s1 = set(range(nn[0], nn[1] + 1))
        s2 = set(range(nn[2], nn[3] + 1))
        if len(s1 & s2) > 0:
            c += 1
    return c


def main():
    print(part_one())
    print(part_two())


if __name__ == '__main__':
    main()
