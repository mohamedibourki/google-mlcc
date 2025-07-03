# 📉 Linear Regression and Gradient Descent - Summary

---

## 📌 What is Gradient Descent?

Gradient Descent is an **iterative optimization algorithm** used to find the best `weight (w)` and `bias (b)` that minimize the model's **loss** (error).

---

## 🔁 How Gradient Descent Works

1. **Initialize Parameters**  
   Start with `weight = 0` and `bias = 0` (or values close to zero).

2. **Calculate the Loss**  
   Use the Mean Squared Error (MSE) loss function:
   \[
   \text{Loss} = \frac{1}{M} \sum (f(x_i) - y_i)^2
   \]

3. **Calculate the Slope**  
   Find the gradient (slope) of the loss with respect to `w` and `b`.

4. **Update Parameters**  
   Move the `weight` and `bias` in the direction that **reduces the loss**:
   \[
   \text{new\_weight} = \text{weight} - \alpha \cdot \text{weight\_slope}
   \]
   \[
   \text{new\_bias} = \text{bias} - \alpha \cdot \text{bias\_slope}
   \]
   Where `α` is the learning rate.

5. **Repeat**  
   Loop this process for several iterations until the model **converges** (loss doesn't improve anymore).

---

## 🧪 Example Dataset (Car MPG vs Weight)

| Pounds (1000s) | MPG (label) |
|----------------|-------------|
| 3.5            | 18          |
| 3.69           | 15          |
| 3.44           | 18          |
| 3.43           | 16          |
| 4.34           | 15          |
| 4.42           | 14          |
| 2.37           | 24          |

Initial values:
- Weight: 0  
- Bias: 0  
- Learning Rate: 0.01

### ⏱ Example Iterations

| Iteration | Weight | Bias | Loss (MSE) |
|-----------|--------|------|-------------|
| 1         | 0      | 0    | 303.71      |
| 2         | 1.20   | 0.34 | 170.84      |
| 3         | 2.05   | 0.59 | 103.17      |
| 4         | 2.66   | 0.78 | 68.70       |
| 5         | 3.09   | 0.91 | 51.13       |
| 6         | 3.40   | 1.01 | 42.17       |

---

## 🧠 Model Convergence

- As training continues, the **loss keeps decreasing**.
- Eventually, the model reaches a point where further changes to weight/bias don’t reduce the loss. This is called **convergence**.
- A **loss curve** can help visualize this process. It usually looks like:
  - Steep drop early on
  - Then slowly flattens
  - Finally stabilizes near minimum loss

---

## 🧮 Convex Loss Surface

- The loss surface for linear models is **convex** (shaped like a bowl).
- This means gradient descent is guaranteed to find the global minimum loss.
- Think of the process like a **ball rolling downhill** until it settles at the bottom of the bowl.

---

## 🏁 Final Model

The best model is found when the loss is minimized. In the example:

- **Best weight** = `-5.44`
- **Best bias** = `35.94`
- **Lowest loss** = `5.54`

This final line fits the data points the best.

---

## 🗝️ Key Terms

- **Gradient Descent**: Algorithm to minimize loss.
- **Loss Curve**: Graph showing loss over time.
- **Convergence**: Point where training no longer improves the model.
- **Convex Function**: A surface where gradient descent can find the true minimum.

