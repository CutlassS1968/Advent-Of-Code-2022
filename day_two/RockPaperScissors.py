def part_one():
    file = open("data.txt")
    lines = file.readlines()
    book = {
        "X": "C",
        "Y": "A",
        "Z": "B"
    }
    score = 0
    for line in lines:
        o = line[0]  # Opponent's Move
        p = line[2]  # Player's Move
        mv = 0
        v = 0

        if p == 'X':
            mv = 1
            if o == 'A':  # Round was a draw
                v = 3
            elif o == 'C':
                v = 6
        if p == 'Y':
            mv = 2
            if o == 'B':  # Round was a draw
                v = 3
            elif o == 'A':
                v = 6
        if p == 'Z':
            mv = 3
            if o == 'C':  # Round was a draw
                v = 3
            elif o == 'B':
                v = 6
        score += v + mv

    print(score)


def part_two():
    file = open("data.txt")
    lines = file.readlines()

    moves = ['A', 'B', 'C']  # All possible moves
    s = 0  # Total score
    for line in lines:
        v = 0  # Score for current move
        o = 0  # Offset for moves list
        c = line[0]  # Opponent's move
        if line[2] == 'X':
            v = 0
            o = 2  # Loose means offset by 2
        if line[2] == 'Y':
            v = 3
            o = 0  # Draw means offset by 0
        if line[2] == 'Z':
            v = 6
            o = 1  # Win means offset by 1
        a = o + moves.index(c)
        if a > 2:
            a -= 3  # Account for wrap around
        v += a + 1
        s += v
    print(s)


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
