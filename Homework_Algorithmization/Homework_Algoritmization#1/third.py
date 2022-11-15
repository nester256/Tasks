def jewelry(jewels, stones):
    count = 0
    for i in jewels:
        count += stones.count(i)
    return count


print(jewelry(jewels="aA", stones="aAAbbbb"))
