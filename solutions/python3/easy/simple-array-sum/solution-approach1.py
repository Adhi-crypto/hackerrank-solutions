# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
# Problem     Simple Array Sum
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-24, 05:16 p.m.
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
