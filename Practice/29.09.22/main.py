def add_two(x):
    return x + 2


def calc_two(eq: str):
    first, sym, snd = eq.split()
    try:
        first, snd = int(first), int(snd)
    except ValueError:
        print("Формат ввода: VALUE1 <+-*/> VALUE2\nПример: 1 * 2")
    else:
        if sym == "+":
            return first + snd
        elif sym == "-":
            return first - snd
        elif sym == "*":
            return first * snd
        elif sym == "/":
            return first / snd


#print(calc_two("1 + 2"))
