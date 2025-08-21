def dao_4_chu_so(x: int) -> int:
    x = abs(x)  # nếu nhập âm thì đảo phần trị tuyệt đối
    a = x // 1000
    b = (x // 100) % 10
    c = (x // 10) % 10
    d = x % 10
    return d*1000 + c*100 + b*10 + a

x = int(input("Nhap so nguyen x (4 chu so): "))
if not (1000 <= abs(x) <= 9999):
    print("Vui long nhap dung so co 4 chu so.")
else:
    y = dao_4_chu_so(x)
    print(f"So dao cua {x} la: {y}")