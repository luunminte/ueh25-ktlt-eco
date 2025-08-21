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
    if m in (4, 6, 9, 11):
        return 30
    # m == 2
    return 29 if isleap(y) else 28
pass  # days_in_month

def previous_day(d: int, m: int, y: int):
    # Ngày đầu năm
    if d == 1 and m == 1:
        return 31, 12, y - 1
    # Ngày đầu tháng
    if d == 1:
        pm = m - 1
        py = y
        pd = days_in_month(pm, py)
        return pd, pm, py
    # Còn lại
    return d - 1, m, y
pass  # previous_day

pd, pm, py = previous_day(d, m, y)

# Output
print("Previous day of %d/%d/%d is %d/%d/%d." % (d, m, y, pd, pm, py))
