# Input n, m
n, m = map(int, input().split())

# Nhập ma trận ký tự
A = []
for i in range(n):
    row = input().split()
    A.append(row)

# Tập hợp nguyên âm
nguyen_am = set("AEIOUaeiou")

# Tìm dòng nhiều nguyên âm nhất
dong_max = -1
so_nguyen_am_max = -1

for i in range(n):
    count = sum(1 for ch in A[i] if ch in nguyen_am)
    if count > so_nguyen_am_max:
        so_nguyen_am_max = count
        dong_max = i + 1   # đánh số dòng từ 1

# Output
print(f"Dong {dong_max} co nhieu nguyen am nhat voi so luong nguyen am la {so_nguyen_am_max}.")
