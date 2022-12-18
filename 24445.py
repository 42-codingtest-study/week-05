import sys
input = sys.stdin.readline
from collections import deque


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

def bfs(k):
    global count
    
    q= deque([k])
    visited[k] = 1
    while q:
        v = q.popleft()
        graph[v].sort(reverse = True)
        for g in graph[v]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                q.append(g)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
bfs(R)

for i in visited[1:]:
    print(i)