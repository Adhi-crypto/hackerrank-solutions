# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
# Problem     List Comprehensions
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-22, 12:03 a.m.
# ──────────────────────────────────────────────────

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] for i in range(x + 1)
                    for j in range(y + 1)
                    for k in range(z + 1)
                    if i + j + k != n]

print(result)
