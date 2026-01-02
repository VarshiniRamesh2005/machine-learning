# Candidate Elimination Algorithm (CEA)

## Overview
The **Candidate Elimination Algorithm (CEA)** is a **concept learning algorithm** used in **machine learning** to identify all hypotheses that are consistent with a given set of training examples. It works on the principle of **version spaces**, where a version space is the set of all hypotheses consistent with the observed examples.

CEA incrementally updates the **specific (S)** and **general (G)** boundaries of hypotheses to narrow down the set of possible concepts.  

- **S (Specific boundary):** The most specific hypothesis that fits all positive examples.  
- **G (General boundary):** The most general hypothesis that fits all negative examples.  

By iterating through examples, the algorithm eliminates inconsistent hypotheses and eventually outputs the final version space.

---

## How it Works
1. **Initialization**:
   - S is initialized as the most specific hypothesis (usually all "Ø" or empty).  
   - G is initialized as the most general hypothesis (usually all "?").

2. **Processing Positive Examples**:
   - Update **S** to generalize only where the current example differs.
   - Remove inconsistent hypotheses from **G** that do not match the positive example.

3. **Processing Negative Examples**:
   - Update **G** to specialize hypotheses to exclude the negative example.
   - Ensure **S** remains more specific than all hypotheses in **G**.

4. **Repeat** for all training examples.  

5. **Output**:
   - **S_final**: The final most specific hypothesis consistent with all positive examples.  
   - **G_final**: The final most general hypotheses consistent with all negative examples.  

---

## Example

```python
concepts = [
    ["Technical", "Senior", "Excellent", "Good", "Urban"],
    ["Technical", "Junior", "Excellent", "Good", "Urban"],
    ["Non-Technical", "Junior", "Average", "Poor", "Rural"],
    ["Technical", "Senior", "Average", "Good", "Rural"],
    ["Technical", "Senior", "Excellent", "Good", "Rural"]
]

target = ["Yes", "Yes", "No", "No", "Yes"]

S_final, G_final = candidate_elimination(concepts, target)

print("Final Specific Boundary:", S_final)
print("Final General Boundary:", G_final)
```

---

## Output

```sql
Final Specific Boundary: ['Technical', '?', 'Excellent', 'Good', '?']
Final General Boundary: [['Technical', '?', 'Excellent', '?', '?'], ['?', '?', 'Excellent', '?', '?'], ['?', '?', 'Excellent', 'Good', '?']]
```

---