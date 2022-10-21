from itertools import permutations
from functools import reduce


def nextBigger(num: int) -> int:
    """
    If input is the biggest number, then if'll be returned
    """
    if num < 0:
        raise ValueError("Negative number!")
    if str(num) == 1:
        return num

    if all([str(num)[i] >= str(num)[i] for i in range(len(str(num)))]):
        return num

    num_m: int = int(len(str(num))*max(str(num)))

    for i in permutations(str(num)):
        if num < num_m >=\
                (temp := int(reduce(lambda x, y: x+y, i))) > num:
            num_m = temp
    return num_m


if __name__ == "__main__":
    print(nextBigger(1))
    print(nextBigger(21))
    print(nextBigger(12))
    print(nextBigger(513))
    print(nextBigger(2017))
