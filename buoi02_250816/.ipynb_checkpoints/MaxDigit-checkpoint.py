# Input
n = int(input())

# Process
def max_digit_4(n: int) -> int:
    """Trả về chữ số lớn nhất của số nguyên 4 chữ số n."""
    n = abs(n)  # phòng khi người dùng nhập âm
    # lấy lần lượt 4 chữ số bằng toán học chia lấy dư
    m = -1
    for _ in range(4):
        d = n % 10
        if d > m:
            m = d
        n //= 10
    return m
pass  # max_digit_4

ans = max_digit_4(n)

# Output
print("%d" % ans)
