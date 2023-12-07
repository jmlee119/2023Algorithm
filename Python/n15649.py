n, m = map(int, input().split())

s = []


def back():
    print("재귀실행", s)
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        print("append 후 ", s)
        back()
        s.pop()
        print("pop 후", s)


back()
