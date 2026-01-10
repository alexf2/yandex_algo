import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __mul__(self, m):
        return Vector(self.x * m, self.y * m)

    def __add__(self, addendum):
        return Vector(self.x + addendum.x, self.y + addendum.y)

    def __repr__(self):
        return f'({self.x}, {self.y}) = {abs(self):.2f}'


def main():
    v1 = Vector(2, 5)
    v2 = Vector(-1, 2)

    print(repr(v1))
    print(repr(v2))
    print(v1 + v2)
    print(v1 * 2)


if __name__ == '__main__':
    main()
