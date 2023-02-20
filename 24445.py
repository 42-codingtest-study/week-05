# 알고리즘 수업 - 너비 우선 탐색 2
# https://www.acmicpc.net/problem/24445

import sys
from collections import deque

input = sys.stdin.readline
N, M, R = map(int, input().split())
visit = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N + 1) :
    graph[i].sort(reverse = True)

dq = deque([R])
visit[R] = 1
cnt = 2
while dq :
    R = dq.popleft()
    for i in graph[R] :
        if visit[i] == 0 :
            dq.append(i)
            visit[i] = cnt
            cnt += 1

print(*visit[1 : ], sep = '\n')