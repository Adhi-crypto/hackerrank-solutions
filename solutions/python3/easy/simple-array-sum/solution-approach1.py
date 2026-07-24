# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
# Problem     Simple Array Sum
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-24, 05:16 p.m.
# Technique   linear-summation-loop
# Time        O(n)
# Space       O(1)
# Insight     The function iterates through each element of the input array exactly once, accumulating the sum into a single integer variable.
# Interview   Before: "How would you calculate the sum of an array?" After: "I would iterate through the array once, maintaining a running total. This approach has O(n) time complexity and O(1) space complexity, which is optimal for processing all n elements in the array."
# Pitfalls    (1) Failing to initialize the accumulator variable to zero before starting the summation loop.  (2) Assuming the input array might be empty without verifying if the loop handles an empty list correctly by returning zero.
# ──────────────────────────────────────────────────

import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    total = 0
    
    for num in ar:
        total = total + num
        
    return total
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
