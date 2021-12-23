class Specification:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)

    def is_satisfied_by(self, candidate):
        raise NotImplementedError()


class And(Specification):
    def __init__(self, value, *specifications):
        super().__init__(value)
        self.specifications = specifications

    def __and__(self, other):
        if isinstance(other, And):
            self.specifications += other.specifications
        else:
            self.specifications += (other, )
        return self

    def is_satisfied_by(self, candidate):
        satisfied = all([
            specification.is_satisfied_by(candidate)
            for specification in self.specifications
        ])
        return satisfied


class Or(Specification):
    def __init__(self, value, *specifications):
        super().__init__(value)
        self.specifications = specifications

    def __or__(self, other):
        if isinstance(other, Or):
            self.specifications += other.specifications
        else:
            self.specifications += (other, )
        return self

    def is_satisfied_by(self, candidate):
        satisfied = any([
            specification.is_satisfied_by(candidate)
            for specification in self.specifications
        ])
        return satisfied


# TODO: Add classes for specification
class City(Specification):
    def is_satisfied_by(self, apartment):
        return str(apartment[0]) == str(self.value)


class FloorNum(Specification):
    def is_satisfied_by(self, apartment):
        return str(apartment[4]) == str(self.value)


class RoomAmt(Specification):
    def is_satisfied_by(self, apartment):
        return str(apartment[5]) == str(self.value)


class MinSquareAmt(Specification):
    def is_satisfied_by(self, apartment):
        return int(apartment[6]) >= int(self.value)


class MaxSquareAmt(Specification):
    def is_satisfied_by(self, apartment):
        return int(apartment[6]) <= int(self.value)


class MinCost(Specification):
    def is_satisfied_by(self, apartment):
        return int(apartment[7]) >= int(self.value)


class MaxCost(Specification):
    def is_satisfied_by(self, apartment):
        return int(apartment[7]) <= int(self.value)


if __name__ == "__main__":
    apa = [1, 'zp', 'lenina', 5, 4, 3, 80, 218489]
    spec = True and FloorNum(4)
    spec = spec and RoomAmt(3) and MinSquareAmt(90)

    print(spec.is_satisfied_by(apa))
