# Input
old_index = int(input())   # chỉ số nước cũ
new_index = int(input())   # chỉ số nước mới
people = int(input())      # số người đăng ký sử dụng

# Process
# Đơn giá
PRICE_FIRST4 = 4400
PRICE_NEXT2  = 8300
PRICE_MORE   = 10500

VAT_RATE = 0.05   # 5%
ENV_RATE = 0.10   # 10%

def calc_payment(m3_used, people):
    """Tính tiền nước chưa VAT và phí môi trường."""
    total = 0
    quota = people * 4  # mỗi người được 4 m3 đầu tiên theo bậc 1
    remain = m3_used
    
    # bậc 1: 4 m3 đầu/người
    use = min(remain, quota)
    total += use * PRICE_FIRST4
    remain -= use

    # bậc 2: 2 m3 tiếp theo/người
    quota = people * 2
    use = min(remain, quota)
    total += use * PRICE_NEXT2
    remain -= use

    # bậc 3: những m3 tiếp theo
    if remain > 0:
        total += remain * PRICE_MORE

    return total

def total_payment(old_index, new_index, people):
    m3_used = new_index - old_index
    if m3_used <= 0:
        return 0, m3_used

    base = calc_payment(m3_used, people)
    vat  = base * VAT_RATE
    env  = base * ENV_RATE
    total = base + vat + env
    return int(round(total)), m3_used
pass

amount, used = total_payment(old_index, new_index, people)

# Output
print("The amount to pay for %d m3 consumed in the month is %s VND." %
      (used, f"{amount:,}"))
