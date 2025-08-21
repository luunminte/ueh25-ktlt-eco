# Input
m = int(input())   # tháng
y = int(input())   # năm

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
        return 0  # tháng không hợp lệ
pass  # days_in_month

ans = days_in_month(m, y)

# Output
print("%d" % ans)
