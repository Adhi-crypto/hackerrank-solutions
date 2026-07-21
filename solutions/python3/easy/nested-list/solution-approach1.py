# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-22, 12:29 a.m.
# Technique   set-sort-filter
# Time        O(N log N)
# Space       O(N)
# Trick       The code uses set() to extract unique scores and sorted() to identify the second lowest value efficiently.
# Hint        set() loses original order, requiring a second pass.
# ──────────────────────────────────────────────────

students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# Get unique grades and sort them
grades = sorted(set(score for name, score in students))

# Second lowest grade
second_lowest = grades[1]

# Get names with the second lowest grade
names = sorted(name for name, score in students if score == second_lowest)

# Print each name
for name in names:
    print(name)
