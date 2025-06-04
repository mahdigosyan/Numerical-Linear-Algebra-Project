import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

weeks = np.array([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
weights = np.array([1, 2, 4, 7, 14, 23, 43, 70, 100, 140, 190, 240, 300, 360, 430, 501, 600, 660, 760, 875, 1005, 1153, 1319, 1502, 1702, 1918, 2146, 2383, 2622, 2859, 3083, 3288, 3462])

def model(x, A, B):
    return A * x * np.exp(B * x)

params, _ = curve_fit(model, weeks, weights, p0=[0.01, 0.1])
A, B = params

print(f"A = {A:.6f}, B = {B:.6f}")

predicted_weights = model(weeks, A, B)

plt.scatter(weeks, weights, label='داده‌های واقعی', color='blue')
plt.plot(weeks, predicted_weights, label='مدل پیش‌بینی', color='red')
plt.xlabel('سن جنین (هفته)')
plt.ylabel('وزن جنین (گرم)')
plt.legend()
plt.grid()
plt.show()