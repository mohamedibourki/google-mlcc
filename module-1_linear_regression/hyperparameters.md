# 📘 Hyperparameters in Machine Learning (Linear Regression)

---

## 🧠 What Are Hyperparameters?

- **Hyperparameters** are values **you set** before training a model.
- They control how the model learns, such as:
  - Learning Rate
  - Batch Size
  - Epochs

🔁 **In contrast**, **parameters** (like weights and bias) are **learned by the model** during training.

---

## ⚡ Learning Rate

The **learning rate** controls how much we adjust weights (`w`) and bias (`b`) at each step of gradient descent.

### ➕ A good learning rate:
- Helps the model **converge quickly**.

### ➖ A bad learning rate:
- **Too small** → slow convergence.
- **Too big** → model bounces around and never settles.

### ✅ Example:
If the gradient = `2.5` and the learning rate = `0.01`, the parameter changes by:

2.5 × 0.01 = 0.025

So the model steps just 0.025 in that direction.

---

## 📦 Batch Size

The **batch size** defines how many examples the model looks at **before updating** its weights and bias.

### 🎯 Why not use the whole dataset?

- Datasets can have millions of rows. Using all at once is too slow and heavy.

---

### 🧪 Common Types:

| Type | Description | Pros | Cons |
|------|-------------|------|------|
| **Full Batch** | All data at once | Stable updates | Slow, memory heavy |
| **SGD** | One example per update | Fast, noisy | Very noisy |
| **Mini-batch SGD** | Few examples per update (e.g., 32, 64, 128) | Balanced | Needs tuning |

🧠 Mini-batches combine the benefits of full batch and SGD.

---

## 🔁 Epochs

- An **epoch** means **one full pass** through the entire dataset.
- If your dataset has 1000 examples and batch size = 100 → 10 steps = 1 epoch.
- You usually need **many epochs** to train a good model.

---

### 📊 Comparison of Updates

| Type | Updates per Epoch | Example (1000 samples, 20 epochs) |
|------|-------------------|-----------------------------------|
| Full batch | 1 update per epoch | 20 updates |
| SGD | 1000 updates per epoch | 20,000 updates |
| Mini-batch (size = 100) | 10 updates per epoch | 200 updates |

---

## 🧩 Key Terms

- **Hyperparameter**: Configurations like learning rate, batch size, and epochs.
- **Parameter**: Model-learned values like weights and bias.
- **SGD**: Stochastic Gradient Descent (one sample per update).
- **Mini-batch SGD**: Gradient updates using small groups of examples.
- **Epoch**: One full pass through the dataset.
- **Iteration**: One update step (could be one sample or one batch).
- **Generalization**: Model’s ability to perform well on new, unseen data.

---

## 📌 Notes

- There is **no perfect value** for learning rate or batch size. You need to **experiment**.
- A bit of **noise** in the training (from SGD or mini-batches) can actually help the model **generalize better**.

---

> _"Train smart, not just hard."_ 💡


