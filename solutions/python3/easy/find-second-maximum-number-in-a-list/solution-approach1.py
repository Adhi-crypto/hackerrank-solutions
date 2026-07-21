# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-22, 12:45 a.m.
# Technique   set-sort-indexing
# Time        O(N log N)
# Space       O(N)
# Trick       The set() constructor removes duplicates, allowing sorted() to order unique elements for easy access via the [-2] index.
# Hint        set() does not preserve input order.
# ──────────────────────────────────────────────────

n = int(input())
scores = list(map(int, input().split()))

unique_scores = sorted(set(scores))

print(unique_scores[-2])
