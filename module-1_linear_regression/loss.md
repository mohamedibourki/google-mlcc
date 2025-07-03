# 📉 Linear Regression: Understanding Loss

---

## 🔍 What is Loss?

- **Loss** measures how far the predicted value is from the actual value.
- The goal in model training is to **minimize loss**.

There are two common ways to calculate this "distance":
1. Take the **absolute value** of the difference (L1).
2. Take the **square** of the difference (L2).

---

## 📐 Types of Loss Functions

| Loss Type        | Definition                                                          | Formula (for N examples)         |
|------------------|----------------------------------------------------------------------|----------------------------------|
| **L1 Loss**       | Sum of absolute differences                                           | `∑ |actual - predicted|`         |
| **MAE** (Mean Absolute Error) | Average of L1 losses                                        | `(1/N) ∑ |actual - predicted|`   |
| **L2 Loss**       | Sum of squared differences                                            | `∑ (actual - predicted)^2`       |
| **MSE** (Mean Squared Error) | Average of L2 losses                                        | `(1/N) ∑ (actual - predicted)^2` |

🧠 **Note**: Squaring magnifies large errors and minimizes small ones.

---

## 🧮 Example: L2 Loss Calculation

If a 2,370-pound car is predicted to get **23.1 mpg**, but actually gets **26 mpg**:

L2 Loss = (26 - 23.1)^2 = (2.9)^2 = 8.41

---

## ⚖️ MAE vs MSE: Which to Use?

### Outlier Behavior:

- **MSE**: 
  - Penalizes large errors more.
  - Model moves *closer to outliers*.
  - Good when large errors must be strongly avoided.

- **MAE**: 
  - Treats all errors equally.
  - Model stays *closer to most data points*, not outliers.
  - More robust to noise.

### Visual Summary:
- **Model trained with MSE** tilts toward outliers.
- **Model trained with MAE** remains closer to average points.

---

## ✅ Check Your Understanding

**Q**: Which dataset has a higher MSE?
- One with 2 points far off (2 units away)?
- Or one with 4 points only 1 unit away?

✅ **Answer**: The dataset with **2 points 2 units away** has higher MSE (due to squaring).

---

## 📚 Key Terms

- **Loss**: The difference between predicted and actual value.
- **MAE (Mean Absolute Error)**: Average absolute error.
- **MSE (Mean Squared Error)**: Average squared error.
- **L1 / L2**: Loss functions based on absolute/squared differences.
- **Outlier**: A data point far from typical values or model predictions.

---
