
# Problem 1 — Linear Interpolator with Duplicate-x Tie Rules

## Description

You are given `n` 2D points (knots) with possibly duplicated x-coordinates. You must compute the linearly interpolated (or extrapolated) y-value at a query `x_input`, following **specific tie-breaking rules** for duplicate x’s.

## Rules

1. For any x that appears multiple times, compress all points at that x into a pair:

   * `min_y(x)` = smallest y among those points
   * `max_y(x)` = largest y among those points
2. When evaluating at `x_input`:

   * If `x_input` exactly equals a knot x: **return `min_y(x)`**.
   * If interpolating between two adjacent distinct x’s, `x0 < x_input < x1`:

     * Use `y0 = max_y(x0)` for the left endpoint.
     * Use `y1 = min_y(x1)` for the right endpoint.
     * Interpolated value = `y0 + (y1 - y0) * (x_input - x0)/(x1 - x0)`.
3. Extrapolation:

   * If `x_input` is **left of all x**: use the two smallest distinct x’s and take **min\_y** at both endpoints.
   * If `x_input` is **right of all x**: use the two largest distinct x’s and take **max\_y** at both endpoints.
4. If **all points share the same x**:

   * If `x_input <= x`: return `min_y(x)`.
   * Else: return `max_y(x)`.

## Function Signature

```
float linear_interpolate(int n, list<float> x_knots, list<float> y_knots, float x_input)
```

## Constraints

* `1 ≤ n ≤ 2 * 10^5`
* Coordinates are real numbers (floats).
* Input lists may be unsorted.
* Multiple points may share the same x.

## Output

* A single float: interpolated or extrapolated y at `x_input` using the rules above.

## Example

**Input**

```
n = 5
x = [1, 1, 3, 4, 4]
y = [2, 5, 6, 9, 12]
x_input = 2
```

**Processing**

* Distinct xs: 1, 3, 4
* At x=1: (min=2, max=5). At x=3: (6,6). At x=4: (min=9, max=12)
* 1 < 2 < 3 ⇒ use y0 = max\_y(1)=5, y1 = min\_y(3)=6
* y = 5 + (6-5) \* (2-1)/(3-1) = 5.5
  **Output**

```
5.5
```

## Edge Cases

* All x equal
* x\_input equals a knot
* Many duplicates at an x
* Unsorted inputs

---

# Problem 2 — NYC Temperatures: Q1–Q6

## Description

You are given a table of daily temperatures for multiple locations: one column is `"NYC"` and the others are `"Town1"`, `"Town2"`, … `"TownP"`. Answer six analytics questions.

## Function Signatures

```
list q1_q5(pd.DataFrame df)  # returns [Q1, Q2, Q3, Q4, Q5a, Q5b]
list q6(pd.DataFrame df)     # returns [best5_town_names...]
```

* `df` columns include `"NYC"`, `"Town1"`, …, `"TownP"` (strings) with numeric daily temperatures.

## Questions

* **Q1:** Column (place) with the **largest standard deviation** (break ties by standard pandas `.idxmax()` behavior).
* **Q2:** Take rows where **Town2 ∈ \[90, 100]** (inclusive). Compute the **median of NYC** on those rows; **round to nearest integer**.
* **Q3:** For each town `i`, fit a **simple linear regression** with intercept:
  `NYC = a_i + b_i * Town_i`.
  Compute **sum of |b\_i|** over all towns, and **round to nearest integer**.
* **Q4:** Which **single town** minimizes MSE of predicting NYC using `a + b * Town_i`? Return the **town name**.
* **Q5:** Which **pair of towns** minimizes MSE of predicting NYC using `a + b1 * Town_i + b2 * Town_j`? Return the **two town names** (flattened as two separate items).
* **Q6:** Choose **five towns** via **greedy forward selection** to minimize MSE of predicting NYC using a linear model with intercept. At each step, add the town that yields the **lowest MSE** when combined with already-selected towns. Break ties lexicographically by town name. Return the **list of 5 town names** in the order selected.

## Constraints

* Number of rows (days) `N` may be up to \~10^5.
* Number of towns `P` may be up to a few dozen.
* All columns are numeric; missing values are absent or pre-cleaned.

## Outputs

* `q1_q5(df)` returns `[Q1_string, Q2_int, Q3_int, Q4_string, Q5a_string, Q5b_string]`.
* `q6(df)` returns a **list of 5 strings**: the chosen town names.

## Example (Illustrative)

Suppose `Town1` and `Town2` jointly predict NYC best, then:

```
q1_q5(df) -> ["NYC", 64, 5, "Town2", "Town1", "Town2"]
q6(df)    -> ["Town3", "Town1", "Town2", "Town5", "Town4"]
```

## Notes & Edge Cases

* Keep `"NYC"` **out of predictor sets** in Q3–Q6.
* For Q4–Q5–Q6, use ordinary least squares with an **intercept**.
* For Q2, if no rows satisfy the filter, define behavior (common choices: return 0, or raise). Most graders ensure there is at least one match.
* Ensure shapes align (1-D arrays for MSE computations).
* For Q5 ties in MSE, choose lexicographically smaller pair for determinism.

---

# Problem 3 — Compute Betas (No-Intercept), Batch/Online

## Description

You are given return series for matched assets: predictors `x0..xK` and responses `y0..yK`. For each i, compute the **no-intercept** regression coefficient (beta) in:

```
y_i ≈ β_i * x_i
```

by:

```
β_i = (Σ_t x_i[t] * y_i[t]) / (Σ_t x_i[t]^2)
```

### Part 1

**Function**

```
List[float] compute_betas(pd.DataFrame dfx, pd.DataFrame dfy)
```

* `dfx` has columns `x0..xK`, `dfy` has columns `y0..yK`.
* Return `[β_0, β_1, …, β_K]` (truncate to min(#x, #y) if unequal).

### Part 2 (Online / Batches)

Now data arrives in **batches**. You are given **lists** of aligned DataFrames:

```
List[pd.DataFrame] dfxs, List[pd.DataFrame] dfys
```

Each pair `(dfxs[b], dfys[b])` contains the same columns (`x0..xK`, `y0..yK`) for batch `b`.

**Function**

```
List[List[float]] compute_betas_online(dfxs, dfys)
```

* For each batch `b`, compute β\_i using the same no-intercept formula applied **within that batch**.
* Return a list of beta-lists: one inner list per batch.

> (If the intended variant is to **aggregate across batches** to produce a single β\_i per i, use the global sums:
> `β_i = (Σ_b Σ_t x_i y_i) / (Σ_b Σ_t x_i^2)`.)

## Constraints

* Each batch may contain thousands of rows.
* Columns are numeric; order of x and y columns matches by index (x0 with y0, etc.).
* No NaNs in test data.

## Outputs

* Part 1: list of floats `[β_0..β_K]`.
* Part 2: list of lists, one for each batch.

## Example

**Input (single batch):**

```
x0: [1, 2], y0: [2, 4]   → β0 = (1*2 + 2*4) / (1^2 + 2^2) = 10 / 5 = 2.0
x1: [1, 0], y1: [3, 0]   → β1 = (3 + 0) / (1 + 0) = 3.0
```

**Output:**

```
[2.00, 3.00]
```

## Edge Cases

* If `Σ x_i^2 == 0`, define β\_i = 0.0.
* If `dfx` and `dfy` differ in number of columns, use the minimum common count.
