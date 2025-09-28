import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load data
d = pd.read_csv("md.csv")

X = d[["age", "bmi"]]
y = d["charges"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("MAE:", mae)
print("R²:", r2)

# Cross-validation
cs = cross_val_score(model, X, y, cv=5, scoring="r2")  # use r2 as accuracy
print("\n==========\n", cs, "\n===========\n")
print("Cross-validation scores:", cs)
print("Average R²:", np.mean(cs))

# -----------------
# 📊 Charts
# -----------------

# 1. Actual vs Predicted
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolor='k')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)  # perfect line
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Charges")
plt.show()

# 2. Residuals plot
residuals = y_test - y_pred
plt.figure(figsize=(6,4))
plt.scatter(y_pred, residuals, alpha=0.6, edgecolor='k')
plt.axhline(y=0, color="r", linestyle="--")
plt.xlabel("Predicted Charges")
plt.ylabel("Residuals (Errors)")
plt.title("Residual Plot")
plt.show()

# 3. Cross-validation scores bar chart
plt.figure(figsize=(6,4))
plt.bar(range(1, len(cs)+1), cs, color="skyblue", edgecolor="k")
plt.axhline(y=np.mean(cs), color="r", linestyle="--", label="Average R²")
plt.xlabel("CV Fold")
plt.ylabel("R² Score")
plt.title("Cross-validation Performance")
plt.legend()
plt.show()
