from functools import reduce


def all_that_staff_in_here(list_str: str) -> str:
    temp = list(
        map(lambda x: tuple(map(lambda y: y.upper(),
                                x.split(":"))), list_str.split(";")))
    temp.sort(key=lambda x: x[1]+x[0])
    return reduce(lambda x, y: x+y,
                  map(lambda x: "("+x[1]+", "+x[0]+") ", temp))[:-1]


if __name__ == "__main__":
    print(all_that_staff_in_here(
        "Fired:Corwill;Wilfred:Corwill;Barney:"
        "TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael"
        ":Corwill;Alfred:Corwill"))
