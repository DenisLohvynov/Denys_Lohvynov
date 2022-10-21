def IP_staff(IP: int) -> str:
    temp = bin(IP)[2:]
    temp_ = (temp[0:8], temp[8:16], temp[16:24], temp[24:])

    numbers = list(map(lambda x: int(x, 2) if x != '' else 0,
                       filter(lambda x: x != '', temp_)))
    if len(numbers) == 0:
        return "0.0.0.0"
    elif len(numbers) == 1:
        return f"0.0.0.{numbers[0]}"
    elif len(numbers) == 2:
        return f"0.0.{numbers[0]}.{numbers[1]}"
    elif len(numbers) == 3:
        return f"0.{numbers[0]}.{numbers[1]}.{numbers[2]}"
    elif len(numbers) == 4:
        return f"{numbers[0]}.{numbers[1]}.{numbers[2]}.{numbers[3]}"
    return ""


if __name__ == "__main__":
    print(IP_staff(2149583361))
    print(IP_staff(32))
    print(IP_staff(0))
