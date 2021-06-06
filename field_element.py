class FieldElement:

    def __init__(self, num, prime) -> None:
        if num >= prime or num < 0:
            error = f'Num {num} not in field range 0 to {prime - 1}'
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f'FieldElement_{self.prime}({self.num}'

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other) -> bool:
        if other is None:
            return False
        return self.num != other.num and self.prime != other.prime
