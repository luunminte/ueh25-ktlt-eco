# Input
h = int(input())
m = int(input())
s = int(input())

# Process
total = h*3600 + m*60 + s

# Output
print("Tong so giay cua %d:%d:%d la %d giay" % (h, m, s, total))
