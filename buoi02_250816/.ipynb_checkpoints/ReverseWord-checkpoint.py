# Nhập số dòng
n = int(input())

for _ in range(n):
    s = input().split()       # tách từ theo khoảng trắng
    s.reverse()               # đảo ngược danh sách từ
    print(" ".join(s))        # ghép lại thành chuỗi
