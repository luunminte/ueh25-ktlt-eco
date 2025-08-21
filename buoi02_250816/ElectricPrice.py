# Input
old_kwh = int(input())     # Chỉ số điện cũ
new_kwh = int(input())     # Chỉ số điện mới

# Process
# Bảng giá bậc thang (kWh, đơn giá VND/kWh)
TIERS = [
    (100, 1242),   # 0 - 100
    (50, 1304),    # 101 - 150
    (50, 1651),    # 151 - 200
    (100, 1788),   # 201 - 300
    (100, 1912),   # 301 - 400
    (float('inf'), 1962)   # 401+
]

VAT_RATE = 0.10

def tier_cost(kwh):
    """Tính tiền điện (chưa VAT) theo bậc thang."""
    if kwh <= 0:
        return 0
    remain = kwh
    total = 0
    for qty, price in TIERS:
        use = min(remain, qty if qty != float('inf') else remain)
        total += use * price
        remain -= use
        if remain <= 0:
            break
    return total

def total_amount_with_vat(kwh):
    """Tổng tiền phải trả đã gồm 10% VAT."""
    base = tier_cost(kwh)
    return int(round(base * (1 + VAT_RATE)))

def safe_kwh(old_val, new_val):
    """Tính sản lượng tháng, trả 0 nếu dữ liệu không hợp lệ."""
    return max(0, new_val - old_val)

pass  # helpers

kwh = safe_kwh(old_kwh, new_kwh)
amount = total_amount_with_vat(kwh)

# Output
# Ví dụ mẫu yêu cầu: "The amount to pay for 187 kWh consumed in the month is 275,536 VND."
print("The amount to pay for %d kWh consumed in the month is %s VND." %
      (kwh, f"{amount:,}"))
