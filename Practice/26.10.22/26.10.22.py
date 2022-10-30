def find_c_symbols():
    st = input().lower()
    count = 0
    for i in set(st):
        if st.count(i) > 1:
            count += 1
    print(count)


def counter_2(s):
    return len([ch for ch in (set(s.lower())) if s.lower().count(ch) > 1])
