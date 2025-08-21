# Input
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# Process
def max5(a, b, c, d, e):
    m = a
    if b > m: m = b
    if c > m: m = c
    if d > m: m = d
    if e > m: m = e
    return m
pass  # max5

def min5(a, b, c, d, e):
    m = a
    if b < m: m = b
    if c < m: m = c
    if d < m: m = d
    if e < m: m = e
    return m
pass  # min5

mi = min5(a, b, c, d, e)
ma = max5(a, b, c, d, e)

# Output
print("%d %d" % (mi, ma))
