# Input
total = int(input())

# Process
h = total // 3600
r = total % 3600
m = r // 60
s = r % 60

# Output
print("%d co dang %d:%d:%d" % (total, h, m, s))
