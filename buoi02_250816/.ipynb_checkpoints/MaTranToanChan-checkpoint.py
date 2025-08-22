# Input n, m
n, m = map(int, input().split())

# Nhập ma trận A
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Kiểm tra ma trận toàn chẵn
toan_chan = True
for i in range(n):
    for j in range(m):
        if A[i][j] % 2 != 0:   # gặp số lẻ
            toan_chan = False
            break
    if not toan_chan:
        break

# Output
if toan_chan:
    print("Mang A toan chan!")
else:
    print("Mang A khong toan chan!")
