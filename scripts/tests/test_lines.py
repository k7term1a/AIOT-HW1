#!/usr/bin/env python3
"""
快速測試：驗證 True Line 和 Fitted Line 的正確性
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 使用與 app.py 相同的參數
np.random.seed(42)
a_value = 2.0
b_value = 5.0
noise_level = 2.0
n_points = 100

# 生成資料（與 app.py 相同）
X = np.random.uniform(-10, 10, n_points)
noise = np.random.normal(0, noise_level, n_points)
y = a_value * X + b_value + noise

print(f"資料生成參數:")
print(f"真實斜率 a = {a_value}")
print(f"真實截距 b = {b_value}")
print(f"噪音等級 = {noise_level}")
print(f"資料點數 = {n_points}")

# 訓練模型
model = LinearRegression()
model.fit(X.reshape(-1, 1), y)

estimated_a = model.coef_[0]
estimated_b = model.intercept_

print(f"\n模型估計參數:")
print(f"估計斜率 a = {estimated_a:.3f}")
print(f"估計截距 b = {estimated_b:.3f}")

# 創建測試線
X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line_pred = model.predict(X_line)  # 擬合線
y_line_true = a_value * X_line.flatten() + b_value  # 真實線（無噪音）

# 測試幾個點
test_points = [-5, 0, 5]
print(f"\n驗證幾個測試點:")
for x_test in test_points:
    y_true = a_value * x_test + b_value  # 真實值（無噪音）
    y_pred = model.predict([[x_test]])[0]  # 模型預測值
    print(f"X = {x_test:2.0f}: 真實值 = {y_true:6.2f}, 預測值 = {y_pred:6.2f}, 差異 = {abs(y_pred - y_true):.3f}")

# 視覺化
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, color='blue', label=f'Data points (with noise σ={noise_level})')
plt.plot(X_line, y_line_pred, color='green', linewidth=2, label=f'Fitted line: y = {estimated_a:.2f}x + {estimated_b:.2f}')
plt.plot(X_line, y_line_true, color='orange', linewidth=2, linestyle='--', label=f'True line: y = {a_value}x + {b_value}')

plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression: True Line vs Fitted Line')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('line_comparison.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"\n結論:")
if abs(estimated_a - a_value) < 0.3 and abs(estimated_b - b_value) < 1.0:
    print("✅ 擬合線與真實線非常接近，這是正常的！")
    print("✅ 真實線顯示理想的線性關係（無噪音）")
    print("✅ 擬合線是從有噪音的資料中學習得到的")
    print("✅ 兩線之間的小差異是由於噪音造成的，這是預期的行為")
else:
    print("❌ 擬合線與真實線差異過大，可能有問題")

print(f"\n圖片已保存為 line_comparison.png")