import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = {
    'day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'price_ons': [2000, 2050, 1980, 2100, 2080, 1950, 2020, 2060, 1990, 2110, 2070, 1970, 2030, 2090, 2040],
    'price_usd': [50000, 51000, 49000, 52000, 51500, 48000, 50500, 51200, 49500, 52500, 51800, 48500, 50800, 52200, 51000],
    'news': [3, 2, 4, 1, 2, 5, 3, 2, 4, 1, 2, 5, 3, 1, 2],
    'coin_price': [12000000, 12200000, 11800000, 12500000, 12350000, 11500000, 12100000, 12250000, 11900000, 12600000, 12400000, 11700000, 12150000, 12480000, 12300000]
}

X = np.column_stack((data['price_ons'], data['price_usd'], data['news']))
y = np.array(data['coin_price'])

model = LinearRegression()
model.fit(X, y)

a1 = model.coef_[0]
a2 = model.coef_[1]
a3 = model.coef_[2]
b = model.intercept_

print("\nضرایب مدل رگرسیون:")
print(f"ضریب قیمت انس (a1): {a1:.2f}")
print(f"ضریب قیمت دلار (a2): {a2:.2f}")
print(f"ضریب اخبار (a3): {a3:.2f}")
print(f"عرض از مبدأ (b): {b:.2f}")

print("\n فرمول نهایی مدل رگرسیون خطی:")
print(f"coin_price = ({a1:.2f} * price_ons) + ({a2:.2f} * price_usd) + ({a3:.2f} * news) + ({b:.2f})")

new_data = np.array([
    [2010, 50300, 3],
    [2120, 53000, 1]
])
predicted_prices = model.predict(new_data)

print("\nپیش‌بینی قیمت سکه:")
for i, price in enumerate(predicted_prices):
    print(f"داده {i+1}: {int(price):,} تومان")

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
print(f"\nدقت مدل (R-squared): {r2:.4f}")
