import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# --- 1. Load Data ---
try:
    housing = fetch_california_housing()
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df["MedHouseVal"] = housing.target
    print("✅ Data loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load data. Error: {e}")
    exit()

# --- 2. Data Preprocessing ---
# We will use ALL available features for the new model
features = housing.feature_names
target = "MedHouseVal"

X = df[features]
y = df[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nData split with {len(features)} features.")

# --- 3. Train and Evaluate BOTH Models for Comparison ---

# == Model 1: Original Linear Regression ==
print("\n--- Training Old Model: Linear Regression ---")
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_pred = linear_model.predict(X_test)
linear_mse = mean_squared_error(y_test, linear_pred)
print(f"📈 Linear Regression MSE: {linear_mse:.4f}")

# == Model 2: New Random Forest Regressor ==
print("\n--- Training New Model: Random Forest ---")
# n_estimators is the number of trees in the forest.
# n_jobs=-1 uses all available CPU cores to speed up training.
forest_model = RandomForestRegressor(
    n_estimators=100, random_state=42, n_jobs=-1)
forest_model.fit(X_train, y_train)
forest_pred = forest_model.predict(X_test)
forest_mse = mean_squared_error(y_test, forest_pred)
# Also calculate R² for the new model
forest_r2 = r2_score(y_test, forest_pred)
print(f"🏆 Random Forest MSE: {forest_mse:.4f} (Lower is better!)")
print(f"🏆 Random Forest R²: {forest_r2:.4f}")


# --- 4. Plotting the Results of the BETTER Model ---
print("\n📊 Generating plot for the better (Random Forest) model...")
plt.figure(figsize=(10, 6))
plt.scatter(y_test, forest_pred, alpha=0.5)

# Add a line for perfect predictions
p1 = max(max(forest_pred), max(y_test.to_numpy()))
p2 = min(min(forest_pred), min(y_test.to_numpy()))
plt.plot([p1, p2], [p1, p2], "r-")

plt.title("Actual vs. Predicted Values (Random Forest)")
plt.xlabel("Actual Values ($100,000s)")
plt.ylabel("Predicted Values ($100,000s)")
plt.grid(True)
plt.show()
