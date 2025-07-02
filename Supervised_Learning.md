# 🧠 Supervised Learning — Google ML Crash Course

Supervised learning involves teaching a model to make predictions using labeled data. It's commonly used in tasks like spam detection or weather forecasting.

---

## 🧱 Core Concepts

1. **Data**
2. **Model**
3. **Training**
4. **Evaluating**
5. **Inference**

---

## 📊 1. Data

- **Data** is the foundation of ML.
- Stored in **datasets**, made up of individual **examples**.
- Each example includes:
  - **Features**: Input data used to make predictions.
  - **Label**: The correct output (the “answer”).
- Example:
  - Weather dataset:
    - Features: temperature, humidity, pressure, etc.
    - Label: rainfall amount.

### ✔ Labeled vs Unlabeled Data

| Type            | Has Features? | Has Label? |
|-----------------|---------------|------------|
| Labeled Example | ✅            | ✅         |
| Unlabeled Example | ✅          | ❌         |

### 📏 Good Dataset Attributes

- **Size**: More examples = better learning
- **Diversity**: Covers a broad range of situations
- ✅ Ideal: **Large + High Diversity**

---

## 🧮 2. Model

- A **model** is a mathematical representation that maps features → labels.
- Learns patterns from data during training.

---

## 🏋️ 3. Training

- The model is trained on **labeled examples**.
- It makes predictions and compares them to actual labels.
- The **difference = loss**. The model adjusts to reduce the loss.
- Repeats for all examples → improves over time.
- Practitioners may tweak:
  - Feature selection (e.g., removing irrelevant features)

---

## 📈 4. Evaluating

- After training, the model is tested with **new labeled data**.
- Only **features** are given → predictions are compared to true labels.
- Goal: Measure performance before real-world use.

---

## 🔍 5. Inference

- Once the model performs well, it is used to make predictions on **unlabeled data**.
- E.g. Given current weather → predict rainfall amount.

---

## 🧾 Key Terms

- `example`: A single data row (features + label)
- `feature`: Input used to make predictions
- `label`: Output the model learns to predict
- `labeled example`: Has both features and label
- `training`: The process of teaching the model
- `loss`: The error between predicted and actual values
- `prediction`: The model's output
- `inference`: Using a trained model to predict on new data

---

## 📅 Last Updated

April 16, 2025

---


