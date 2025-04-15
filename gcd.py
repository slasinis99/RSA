def gcd(a, b, prnt = True):
    d = {}
    v = __gcd(a, b, d)
    while not d[v][1] == a and not d[v][3] == b:
        d[v] = (d[v][2], d[d[v][3]][1], d[v][0]+d[v][2]*d[d[v][3]][2], d[v][1])
    if prnt: print(f'gcd({a}, {b}) = {v} = ({d[v][0]})({d[v][1]}) + ({d[v][2]})({d[v][3]})')
    return v, d[v][0], d[v][2] 

def __gcd(a, b, d = {}):
    if b > a: a, b = b, a
    q = a // b
    r = a % b
    d[r] = (1, a, -q, b)
    if r == 0:
        return b
    return __gcd(b, r, d)

def find_modular_inverse(b, n, prnt = True):
    if b == 0:
        print(f'0 cannot have a multiplicative inverse.')
        return
    v, _, y = gcd(n, b, prnt=False)
    if prnt: print(y % n)
    return y % n