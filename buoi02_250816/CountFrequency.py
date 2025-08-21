# Input
A = [1,1,1,1,2,2,2,2,3,3,4,5,5]

# Process
visited = []   # lưu lại các phần tử đã xử lý
result = []

for x in A:
    if x not in visited:        # chỉ đếm khi chưa đếm phần tử này
        count = A.count(x)      # đếm số lần xuất hiện trong list
        result.append((x, count))
        visited.append(x)

# Output
# in theo định dạng: 1:4, 2:4, ...
out_str = ", ".join(f"{val}:{cnt}" for val, cnt in result)
print("Input A =", A)
print("Output =", out_str)
