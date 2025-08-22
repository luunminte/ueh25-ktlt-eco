import math

# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# Input n, m
n, m = map(int, input().split())

# Nhập ma trận A
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Đếm số nguyên tố theo từng cột
dem_cot = [0] * m
for j in range(m):
    for i in range(n):
        if is_prime(A[i][j]):
            dem_cot[j] += 1

# Tìm số lượng nguyên tố lớn nhất
max_nt = max(dem_cot)

# Lấy ra các cột có nhiều số nguyên tố nhất
cols = [j for j in range(m) if dem_cot[j] == max_nt]

# Output
print("Cac cot nhieu nguyen to nhat:", " ".join(map(str, cols)))
