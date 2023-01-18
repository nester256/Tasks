def cadaver(template, word):
    vowel = ["а", "о", "и", "ы", "у" "и", "э"]
    consonant = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш",
                 "щ"]

    def val_word(temp, n_word):
        for i, ch in enumerate(temp):
            if ch == "1" and consonant.count(n_word[i]) > 0:
                continue
            elif ch == "0" and vowel.count(n_word[i]) > 0:
                continue
            elif ch == "?" and consonant.count(n_word[i]) > 0 or vowel.count(n_word[i]) > 0:
                continue
            else:
                return False
        return True

    if template.count("*") == 1:
        left, right = template.split("*")
        lft = len(word) - len(right)
        rgt = len(word) - len(left)
        if len(left) == 0:
            l = True
        else:
            l = val_word(left, word[:len(left)])
        if len(right) == 0:
            r = True
        else:
            r = val_word(right, word[len(word) - len(right):])
        return r and l
    else:
        return val_word(template, word)


print(cadaver("10*010", "молоко"))
print(cadaver("10*01?", "молоко"))
print(cadaver("10*", "молоко"))
