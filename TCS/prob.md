<img width="432" height="557" alt="image" src="https://github.com/user-attachments/assets/9ec5d297-6361-43b9-8820-9f50e0249256" />
Absolutely! Let me break it down in simple, clear language. 🐞🧊

---

## 🧩 Problem Summary

You have a **cube** of size **10×10×10 cm**, and there's a **beetle** that moves on its **outer surface**.

The beetle has to visit a list of **points** on the cube's surface, one after another, and it measures how far it walks.

### 🚫 Important Rule:

The beetle **never walks on the bottom face** (z = 0). All other 5 faces are allowed.

---

## 🛣️ How the Beetle Moves

### ✅ Case 1: **Both points on the same face**

* Example: Two points on the **top** face, or both on the **left** face.
* Then the beetle walks in an **arc**, like a part of a circle.
* The arc is **60°** of a circle.
* To calculate distance:
  👉 First, calculate the straight-line distance between the two points (called the **chord**).
  👉 Then the arc distance is:

  $$
  \text{Arc distance} = \frac{\pi}{6} \times \text{chord length}
  $$

---

### ✅ Case 2: **Points are on different faces**

* Example: One point on the **front**, the other on the **right**.
* Now the beetle takes the **shortest surface path** from one to the other — like sliding over the cube's outer skin.
* The cube is **unfolded** in the beetle’s mind, like flattening a box.

#### 🧠 What is "Unfolding the Cube"?

Imagine taking a cardboard cube and opening it up flat. You’ll get a "net" that shows connected cube faces on a flat surface.

Now the beetle can "walk straight" across adjacent faces — just not over the bottom!

We simulate this in code by trying a few "unfolding" directions (top-front, top-left, etc.) and picking the **shortest distance** that does **not touch the bottom**.

---

## 🧮 Example

### 📥 Input:

```text
3
0,0,10, 10,0,10, 10,10,10
```

This means:

1. Start at (0, 0, 10) → front-left corner on **top face**
2. Go to (10, 0, 10) → front-right corner on **top face**
3. Go to (10, 10, 10) → back-right corner on **top face**

All 3 points are on the **top face**.

So, the beetle uses **arc movement** for both steps.

#### Step 1:

From (0,0,10) to (10,0,10)
Straight line = 10
Arc distance = π/6 × 10 ≈ 5.24

#### Step 2:

From (10,0,10) to (10,10,10)
Straight line = 10
Arc distance = π/6 × 10 ≈ 5.24

#### Total distance:

5.24 + 5.24 = **10.48**
(Rounded to **two decimal places per step** before adding.)

✅ So the beetle reports: `10.48`

---

## 🔄 Summary of Steps in Code

1. **Read the list of 3D points.**
2. **Check each pair of points:**

   * If same face → use arc formula
   * Else → try "walking around the cube" using shortest surface path
3. **Round each step's distance** to 2 decimal places.
4. **Add them all up.**

---

