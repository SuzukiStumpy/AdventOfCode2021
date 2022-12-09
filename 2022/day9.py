data = [line.strip() for line in open('inputs/day9.txt', 'r')]


class Rope:
    def __init__(self, length: int) -> None:
        self.knots = []
        for _ in range(length + 1):
            self.knots.append({'x': 0, 'y': 0})
        self.visited = set()
        self.visited.add(tuple(list(self.knots[length].values())))

    def process(self, motion: [str]) -> int:
        for line in motion:
            direction, distance = line.split(' ')

            if direction == 'L':
                self.knots[0]['x'] -= int(distance)
            elif direction == 'R':
                self.knots[0]['x'] += int(distance)
            elif direction == 'U':
                self.knots[0]['y'] += int(distance)
            else:
                self.knots[0]['y'] -= int(distance)

            # check tail and move
            for i in range(1, len(self.knots)):
                while self.manhattan(i-1, i) > 1 and not self.touching(i-1, i):
                    self.follow(i-1, i)
                    if i == len(self.knots) - 1:
                        self.visited.add(tuple(list(self.knots[i].values())))

        return len(self.visited)

    def follow(self, head: int, tail: int) -> None:
        """Attempt to have the tail follow the head, then return the new tail
           position.  If the tail is not in the same row or column as the head,
           and not touching it, then it moves diagonally to keep up
        """
        if self.knots[head]['x'] > self.knots[tail]['x']:
            self.knots[tail]['x'] += 1
        if self.knots[head]['y'] > self.knots[tail]['y']:
            self.knots[tail]['y'] += 1
        if self.knots[head]['x'] < self.knots[tail]['x']:
            self.knots[tail]['x'] -= 1
        if self.knots[head]['y'] < self.knots[tail]['y']:
            self.knots[tail]['y'] -= 1

    def manhattan(self, head: int, tail: int) -> int:
        """Return the manhattan distance between the head and the tail"""
        return abs(self.knots[head]['x'] - self.knots[tail]['x']) + abs(self.knots[head]['y'] - self.knots[tail]['y'])

    def touching(self, head: int, tail: int) -> bool:
        """Returns true if the head and tail knots are in contact with one another"""
        return (abs(self.knots[head]['x'] - self.knots[tail]['x']) == 1) and (abs(self.knots[head]['y'] - self.knots[tail]['y']) == 1)


print(f"Part 1: {Rope(1).process(data)}")
print(f"Part 2: {Rope(9).process(data)}")
