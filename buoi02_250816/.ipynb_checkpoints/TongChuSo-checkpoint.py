# Nạp thư viện
import math
# Nhập dữ liệu
n = int(input("Moi ban nhap so nguyen n (co bon chu so): "))
# tách dữ liệu
a = n // 1000           # chữ số hàng nghìn
b = (n // 100) % 10     # chữ số hàng trăm
c = (n // 10) % 10      # chữ số hàng chục
d = n % 10              # chữ số hàng đơn vị
tong = a + b + c + d
# Xuất dữ liệu
print(f"{n} = {a} + {b} + {c} + {d} = {tong}")