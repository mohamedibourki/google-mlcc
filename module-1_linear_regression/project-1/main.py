import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# --- 1. Load Data from Scikit-learn ---
try:
    # Fetch the dataset
    housing = fetch_california_housing()

    # Create a pandas DataFrame
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    # The target variable is median house value
    df["MedHouseVal"] = housing.target

    print("✅ Data loaded successfully from scikit-learn!")
    print(df.head())

except Exception as e:
    print(f"❌ Failed to load data. Error: {e}")
    exit()

# --- 2. Data Preprocessing ---
features = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population"]
target = "MedHouseVal"

X = df[features]
y = df[target]

print("\n🧹 Data is clean. Preprocessing complete.")

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Data split: {len(X_train)} training samples and {
      len(X_test)} testing samples.")

# --- 3. Model Training ---
model = LinearRegression()
model.fit(X_train, y_train)

print("\n🤖 Model training complete.")

# --- 4. Model Evaluation ---
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📈 Model Evaluation Results:")
print("----------------------------")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# --- 5. Example Prediction ---
example_area = pd.DataFrame(
    {
        "MedInc": [3.5],
        "HouseAge": [15],
        "AveRooms": [5.5],
        "AveBedrms": [1.1],
        "Population": [800],
    }
)
predicted_value = model.predict(example_area)
print("\n🏠 Example Prediction:")
print(
    f"Predicted median house value for the example area: ${
        predicted_value[0] * 100000:,.2f}"
)


# --- 6. Plotting the Results ---
print("\n📊 Generating plot...")
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, label="Predictions")

# Add a line for perfect predictions
p1 = max(max(y_pred), max(y_test.to_numpy()))
p2 = min(min(y_pred), min(y_test.to_numpy()))
plt.plot([p1, p2], [p1, p2], "r-", label="Perfect Prediction")

plt.title("Actual vs. Predicted House Values")
plt.xlabel("Actual Values ($100,000s)")
plt.ylabel("Predicted Values ($100,000s)")
plt.legend()
plt.grid(True)
plt.show()
