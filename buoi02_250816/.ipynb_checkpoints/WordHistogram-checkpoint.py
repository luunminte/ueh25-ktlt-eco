import re
from collections import OrderedDict

# Nhập số câu
n = int(input())

# Đọc n câu và nối lại
text = ""
for _ in range(n):
    text += input().lower() + " "

# Tách từ, bỏ các dấu câu
words = re.findall(r"[a-zA-ZÀ-Ỵà-ỹ]+", text)

# Đếm tần số xuất hiện theo thứ tự xuất hiện
freq = OrderedDict()
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

# In kết quả theo thứ tự xuất hiện
for k, v in freq.items():
    print(f"{k}: {v}")
