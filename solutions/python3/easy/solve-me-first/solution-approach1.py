# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/solve-me-first/problem?isFullScreen=true
# Problem     Solve Me First
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-24, 05:03 p.m.
# Technique   arithmetic-summation
# Time        O(1)
# Space       O(1)
# Insight     The function computes the sum of two integers by applying the addition operator to the provided input parameters.
# Interview   Before: "How would you implement a function to add two integers?" After: "The implementation uses the addition operator to return the sum in O(1) time, handling the integer inputs as specified in the problem constraints."
# Pitfalls    (1) Assuming the input values exceed the standard integer range, which might cause overflow in languages with fixed-width integer types.  (2) Failing to handle potential input parsing errors if the provided input is not a valid integer string.
# ──────────────────────────────────────────────────



def solveMeFirst(a,b):
    sum = a + b
    
    return sum

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
