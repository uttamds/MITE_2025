Thanks! Now that you've confirmed the input is:

```
100 100 200
200 180
```

Let’s solve this **step by step**.

---

## 📌 Step 1: Interpret the input

| Value | Meaning                                                        |
| ----- | -------------------------------------------------------------- |
| `100` | Height of the cylinder (`h`)                                   |
| `100` | Radius of the cylinder (`r`)                                   |
| `200` | Distance of bug from the top of cylinder (`s`)                 |
| `200` | Vertical coordinate `t` of the destination (on curved surface) |
| `180` | Angular coordinate `p` (degrees) from bug’s topmost point B    |

---

## 📐 Step 2: What kind of surface?

Since the destination is `(200, 180)` → **both coordinates are positive**, so the destination is on the **curved surface** of the cylinder.

---

## 🧾 Step 3: Use the distance formula for curved surface (unwrapped)

When unwrapped, the curved surface becomes a rectangle:

* **Height**: up to `h = 100` (not used here since both points are at same height)
* **Width**: full circumference = `2πr = 2 × π × 100 ≈ 628.318`

### 📍Bug's location:

* At `(s = 200, 0)` → on curved surface, vertical 200 units below top, angle `0°`

### 📍Destination:

* At `(t = 200, p = 180°)`

Both are at the same height ⇒ vertical difference = 0

Now, convert angle `p = 180°` to **horizontal distance**:

$$
\text{Horizontal distance} = \frac{180}{360} \cdot 2\pi r = \pi r = 3.1416 \times 100 = 314.16
$$

---

## 🧮 Step 4: Total Distance

$$
\text{distance} = \sqrt{(s - t)^2 + (\text{horizontal distance})^2}
$$

$$
= \sqrt{(200 - 200)^2 + (314.16)^2}
= \sqrt{0 + 98696.04}
≈ \boxed{314.16}
$$

---

## ✅ Final Answer

$$
\boxed{314}
$$

This is the **shortest distance the bug would travel** on the curved surface to reach the destination `(200, 180)` from its position at `(200, 0)`.

Let me know if you want a version where `s ≠ t` or destination is on the **top surface**!
