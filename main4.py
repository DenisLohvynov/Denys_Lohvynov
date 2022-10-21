def count(arr: list[int], target: int, test: bool = False) -> int:
    number: int = 0

    for i, a_i in enumerate(arr):
        for j, a_j in enumerate(arr[i+1:]):
            if a_i + a_j == target:
                number += 1
                if test:
                    print(f'a[{i}]+a[{j}] = {a_i} + {a_j} = {target}')

    return number


if __name__ == "__main__":
    # by default no prints
    print(count([1, 3, 6, 2, 2, 0, 4, 5], 5, True))
