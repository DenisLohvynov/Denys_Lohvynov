def digital_root(x: int) -> int:
    if type(x) is not int or x < 0:
        raise ValueError("Invalid input")

    def sub_sum(x: int) -> int:
        S: int = 0
        while x > 0:
            S += x % 10
            x -= x % 10
            x //= 10
        return S

    while (answer := sub_sum(x)) >= 10:
        x = answer
    return answer


if __name__ == '__main__':
    print(digital_root(16))
    print(digital_root(777))
    print(digital_root(54546))
