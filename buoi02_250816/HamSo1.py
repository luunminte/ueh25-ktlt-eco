import math

def y1_fn(x: float) -> float:
    # y1 = 4*(x^2 + 10*sqrt(x) + 3*x + 1)
    if x < 0:
        raise ValueError("x phải >= 0 để tính sqrt(x) trong y1.")
    return 4.0 * (x**2 + 10.0*math.sqrt(x) + 3.0*x + 1.0)

def y2_fn(x: float) -> float:
    # y2 = [sin(pi*x^2) + sqrt(x^2 + 1)] / [e^(2x) + cos(pi*x/4)]
    tu = math.sin(math.pi * x**2) + math.sqrt(x**2 + 1.0)
    mau = math.exp(2.0*x) + math.cos(math.pi * x / 4.0)
    return tu / mau

x = float(input("Nhap x (so thuc): "))
y1 = y1_fn(x)
y2 = y2_fn(x)
print(f"y1 = {y1:.2f}")
print(f"y2 = {y2:.2f}")
