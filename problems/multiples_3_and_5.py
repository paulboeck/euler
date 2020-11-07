class MultiplesOf3And5:
    @staticmethod
    def sum_multiples_of_3_and_5(value):
        return sum((x for x in range(value) if (x % 3 == 0 or x % 5 == 0)))

