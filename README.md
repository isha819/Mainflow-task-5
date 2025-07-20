This repository contains a collection of Python programs that implement classic algorithmic problems and simulations. Each program takes user input and demonstrates concepts such as recursion, dynamic programming, data structures, simulation, and validation.

✅ 1. All Permutations of a String

Objective: Generate all possible permutations of a string using recursion.

Input: A string from the user.

Output: All permutations in any order.

Approach:
Recursively swap characters to explore all combinations.
Base case: when the left index == right index, store the string.
Backtrack after each recursive call.

Key Challenge: Efficient character swapping and handling duplicate cases (if needed).

✅ 2. N-th Fibonacci Number (DP)

Objective: Find the nth Fibonacci number efficiently using Dynamic Programming.

Input: Integer n.

Output: The nth Fibonacci number.

Approach:
Use bottom-up DP with a memoization list (dp[i] = dp[i-1] + dp[i-2]).
Optional: Use two variables for space optimization.

Key Challenge: Preventing stack overflow (vs recursion) and optimizing space.

✅ 3. Find Duplicates in a List

Objective: Identify all duplicate elements in a list of integers.

Input: List of integers.

Output: List of duplicate values.

Approach:
Use collections.Counter to count frequency of elements.
Filter those with count > 1.

Key Challenge: Handling large lists and maintaining time efficiency.

✅ 4. Longest Increasing Subsequence

Objective: Find the length of the Longest Increasing Subsequence (LIS).

Input: A list of integers.

Output: Integer representing LIS length.

Approach:
Use DP: For each element, check previous elements and build dp[i].
Final result: max(dp).

Key Challenge: Nested loops (O(n²)), but clear logic. Can be improved to O(n log n) if needed.

✅ 5. Find K Largest Elements

Objective: Return the k largest numbers from a list.

Input: List of integers and value k.

Output: A list of k largest numbers.

Approach:
Method 1: Sort the list and pick the last k elements.

Key Challenge: Avoiding full sort when only a few large elements are needed.

✅ 6. Rotate Matrix (90° Clockwise)

Objective: Rotate a 2D matrix 90 degrees clockwise.

Input: 2D list of integers (matrix).
Output: Rotated matrix.

Approach:
Step 1: Transpose the matrix using zip(*matrix).
Step 2: Reverse each row to get 90° clockwise rotation.

Key Challenge: Handling non-square matrices (optional extension).

✅ 7. Sudoku Validator

Objective: Validate if a given 9x9 Sudoku board is valid.

Input: 9x9 grid with integers (0 for empty cells).

Output: True or False.

Approach:
Check for duplicates in each row, column, and 3x3 subgrid.
Ignore 0 (empty cells).

Key Challenge: Properly indexing subgrids and handling incomplete boards.

✅ 8. Virtual Stock Market Simulator

Objective: Simulate a basic stock market environment without using real APIs.

Input: User commands via a menu (buy, sell, update prices).

Output: Console display of stock prices, transactions, portfolio, etc.

Approach:
Use random fluctuations to simulate price changes.
Maintain a portfolio dictionary and balance.
Record transaction history.

Key Features:
Random price simulation (±5% fluctuation)
buy/Sell functionality with quantity checks
Portfolio and cash tracking
Transaction logs

Key Challenges:
Realistic simulation of market behavior without real data
Managing state: stock prices, balance, owned shares
Designing an intuitive menu system
