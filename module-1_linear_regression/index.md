# 📊 Linear Regression - ML Crash Course Summary

This module introduces the concept of **linear regression** in machine learning, a foundational technique for predicting a numeric value based on input features.

---

## 🎯 Learning Objectives

- Understand **loss functions** and how they guide model training.
- Learn how **gradient descent** finds optimal parameters.
- Know how to **tune hyperparameters** for better performance.

---

## 📚 Prerequisites

- Basic understanding of ML concepts from the **Introduction to Machine Learning** module.

---

## 🧠 Key Concepts

### What is Linear Regression?

Linear regression is a statistical method that models the relationship between a numeric **feature** (input) and a **label** (output) by fitting a straight line.

For example, to predict a car’s fuel efficiency (MPG) based on its weight:

| Weight (1000s lbs) | MPG |
|--------------------|-----|
| 3.5                | 18  |
| 3.69               | 15  |
| 3.44               | 18  |
| 3.43               | 16  |
| 4.34               | 15  |
| 4.42               | 14  |
| 2.37               | 24  |

As car weight increases, fuel efficiency usually decreases — this forms a downward-sloping trend.

---

## 📐 Model Equation

### Simple Linear Regression:

ŷ = b + w₁x₁

Where:
- `ŷ`: predicted output (e.g., MPG)
- `x₁`: input feature (e.g., weight)
- `w₁`: weight (slope of the line)
- `b`: bias (y-intercept)

#### Example:
If:
- `w₁ = -4.6`
- `b = 34`

Then, for a 4,000-pound car (i.e., `x₁ = 4`):

ŷ = 34 + (-4.6 × 4) = 15.6 MPG

---

## 🧩 Multiple Features

More realistic models use **multiple features**, each with its own weight:

ŷ = b + w₁x₁ + w₂x₂ + ... + wₙxₙ

### For example:
To predict MPG, we might include:
- `x₁`: Engine displacement
- `x₂`: Acceleration
- `x₃`: Number of cylinders
- `x₄`: Horsepower

Each feature contributes to the output based on its weight:

ŷ = b + w₁(displacement) + w₂(acceleration) + w₃(cylinders) + w₄(horsepower)

Some features have a negative relationship (e.g., horsepower), while others might be positive (e.g., acceleration time).

---

## 🔁 Training the Model

During training, the algorithm adjusts the **weights** and **bias** to minimize prediction error using:

- A **loss function** (measures how bad the prediction is)
- **Gradient descent** (an optimization algorithm to minimize the loss)

Only the **weights** and **bias** are updated during training — not the input features or output labels.

---

## ✅ Exercise Check

**Question:** What parts of the linear regression equation are updated during training?  
**Answer:** ✅ **Bias and Weights**

---

## 🧾 Key Terms

- **Feature**: An input variable (e.g., weight, horsepower)
- **Label**: The output you want to predict (e.g., MPG)
- **Weight**: Coefficient representing feature importance
- **Bias**: Constant added to the prediction (intercept)
- **Parameter**: Tunable values in the model (weights and bias)
- **Linear Regression**: Predicts continuous output using a weighted sum of input features

---
