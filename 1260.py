import sys
input = sys.stdin.readline
from collections import deque


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1