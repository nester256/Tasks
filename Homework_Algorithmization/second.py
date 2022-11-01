def numberOfMatches(n: int) -> int:
    matches = 1
    while n != 2:
        matches += int(n / 2)
        n = round(n / 2)
    return matches


print(numberOfMatches(7))
