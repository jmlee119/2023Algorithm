n, m = map(int, input().split())

s = []
def back():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    if len(s) != 0 and i < s[len(s)-1]: continue
    
    s.append(i)
    back()
    s.pop()

back()