import math

x1 = float(input("Nhap x1: "))
y1 = float(input("Nhap y1: "))
x2 = float(input("Nhap x2: "))
y2 = float(input("Nhap y2: "))

kc = math.hypot(x2 - x1, y2 - y1)  # sqrt((dx)^2 + (dy)^2)
print(f"Khoang cach AB = {kc:g}")