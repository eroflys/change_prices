sh = 1023456789876543200
while True:
    sh += 1
    ss = str(sh)
    f = ''
    s = ''
    m = ''
    if len(ss) % 2 == 0:
        f = ss[:len(ss) // 2]
        s = ss[:len(ss) // 2 - 1:-1]
    else:
        f = ss[:len(ss) // 2]
        s = ss[:len(ss) // 2 :-1]
        m = ss[len(ss) // 2]
    if f == s and '0' in ss and '1' in ss and '2' in ss and '3' in ss and '4' in ss and '5' in ss and '6' in ss and '7' in ss and '8' in ss and '9' in ss and sh % 9 == 0:
        print(sh)
        break
    else:
        print(f, s)