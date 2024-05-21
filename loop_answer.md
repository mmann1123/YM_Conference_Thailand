# Challenge 1 - Solution

## Answer

The code snippet will print each combination of the characters `'A'`, `'B'`, `'C'` from the outer loop with the numbers `1`, `2`, `3` from the inner loop. Here is the expected output:

``` bash
A 1
A 2
A 3
B 1
B 2
B 3
C 1
C 2
C 3
```

To better understand the execution and visualize how each step in the loop contributes to this output, I can create a visual representation using Python code that simulates each iteration step-by-step.

## Output Explanation

The code snippet you've provided is an example of nested loops in Python. Nested loops are loops within loops, where the inner loop runs to completion before the outer loop advances by one iteration. Let's go through how this particular nested loop operates and why it produces the output it does.

Here is the code snippet again for reference:

```python
for i in ['A', 'B', 'C']:  # outer loop
    for j in [1, 2, 3]:    # inner loop
        print(i, j)
```
 
Here's a detailed step-by-step explanation of how the loops execute:

1. **First Iteration of Outer Loop**:
   - `i` is set to `'A'`.
   - The inner loop then starts its execution:
     - **First Iteration of Inner Loop**:
       - `j` is set to `1`.
       - `print(i, j)` outputs `A 1`.
     - **Second Iteration of Inner Loop**:
       - `j` is set to `2`.
       - `print(i, j)` outputs `A 2`.
     - **Third Iteration of Inner Loop**:
       - `j` is set to `3`.
       - `print(i, j)` outputs `A 3`.
   - The inner loop completes all its iterations for `i = 'A'`.

2. **Second Iteration of Outer Loop**:
   - `i` is now set to `'B'`.
   - The inner loop repeats its full cycle:
     - `j` takes values `1`, `2`, and `3` sequentially, resulting in the output of `B 1`, `B 2`, and `B 3`.

3. **Third Iteration of Outer Loop**:
   - `i` is now set to `'C'`.
   - The inner loop again performs three prints: `C 1`, `C 2`, and `C 3`.
 