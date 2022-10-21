def first_non_repeating_letter(sentence: str) -> str | None:
    checked: set[str] = set()

    def unique(sentence: str, latter: str) -> bool:
        return len(sentence) - \
            len(list(filter(lambda x: x.upper()
                            != latter.upper(), sentence))) == 1

    for i in sentence:
        if i in checked:
            continue
        if unique(sentence, i):
            return i
        else:
            checked.add(i)
    return None


if __name__ == '__main__':
    print(first_non_repeating_letter("ssTreSS"))
    print(first_non_repeating_letter("stress"))
    print(first_non_repeating_letter("aabbcc"))
