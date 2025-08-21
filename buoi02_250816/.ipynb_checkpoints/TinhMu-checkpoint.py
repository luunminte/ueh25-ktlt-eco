def luy_thua(a: float, n: int) -> float:
    """Trả về a^n, hỗ trợ n âm, 0, dương."""
    if n == 0:
        return 1.0
    if n > 0:
        kq = 1.0
        for _ in range(n):
            kq *= a
        return kq
    # n < 0
    if a == 0:
        raise ZeroDivisionError("0 không có lũy thừa âm.")
    return 1.0 / luy_thua(a, -n)

a = float(input("Nhap so thuc a: "))
n = int(input("Nhap so mu n: "))
kq = luy_thua(a, n)
print(f"Ket qua {a}^{n} = {kq:g}")