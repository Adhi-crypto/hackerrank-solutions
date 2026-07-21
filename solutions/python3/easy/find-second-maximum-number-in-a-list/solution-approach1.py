# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-22, 12:45 a.m.
# ──────────────────────────────────────────────────

n = int(input())
scores = list(map(int, input().split()))

unique_scores = sorted(set(scores))

print(unique_scores[-2])
