# Input
d = int(input())
m = int(input())
y = int(input())

# Process
def isleap(y: int) -> bool:
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
pass  # isleap

def days_in_month(m: int, y: int) -> int:
    if m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif m in (4, 6, 9, 11):
        return 30
    elif m == 2:
        return 29 if isleap(y) else 28
    else:
        return 0
pass  # days_in_month

def next_day(d: int, m: int, y: int):
    dm = days_in_month(m, y)
    if d < dm:
        return d + 1, m, y
    else:
        if m < 12:
            return 1, m + 1, y
        else:
            return 1, 1, y + 1
pass  # next_day

nd, nm, ny = next_day(d, m, y)

# Output
print("%d/%d/%d" % (nd, nm, ny))
