import string


def clean_text(text):
    for sym in string.punctuation:
        text = text.replace(sym, "")
    return text.lower().split()


def get_second(value):
    return value[1]


def count_words(words):
    # 1
    # counted_words = {}
    # for word in set(words):
    #     counted_words[word] = words.count(word)
    #
    # 2
    counted_words = {word: words.count(word) for word in set(words)}
    return sorted(counted_words.items(), key=get_second, reverse=True)


def top_10(text):
    print("***\tTOP 10\t***")
    for word, num in count_words(clean_text(text))[:10]:
        print("{0}\t{1}".format(word, num))


file = open("23.09.22/file.txt", "r")
print(top_10(file.read()))
