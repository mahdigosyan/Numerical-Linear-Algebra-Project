def f(r, A, P, n):
    """محاسبه تفاضل بین دو سمت معادله برای یافتن ریشه"""
    try:
        return (A / r) * (1 - (1 / (1 + r))**n) - P
    except ZeroDivisionError:
        return float('inf')

def bisection_method(P, A, n, tol=1e-7, max_iter=100):
    """یافتن نرخ سود ماهانه با روش نابجایی"""
    low = 0.000001
    high = 1.0

    for i in range(max_iter):
        mid = (low + high) / 2
        value = f(mid, A, P, n)

        if abs(value) < tol:
            return mid * 12  # نرخ سالانه

        if f(low, A, P, n) * value < 0:
            high = mid
        else:
            low = mid

    # اگر به دقت نرسید، مقدار نهایی رو برمی‌گردونه
    return (low + high) / 2 * 12

def main():
    print("📌 محاسبه نرخ سود وام با روش نابجایی (Bisection)")
    try:
        mablagh_vam = float(input("➤ مبلغ وام (تومان): ").replace(",", ""))
        mablagh_ghest = float(input("➤ مبلغ قسط ماهانه (تومان): ").replace(",", ""))
        tedad_ghest = int(input("➤ تعداد اقساط (ماه): "))

        nerkh_salane = bisection_method(mablagh_vam, mablagh_ghest, tedad_ghest)
        print(f"\n✅ نرخ سود سالانه تقریبی: {nerkh_salane * 100:.2f}%")

    except ValueError:
        print("❌ لطفاً عدد معتبر وارد کنید.")

if __name__ == "__main__":
    main()
