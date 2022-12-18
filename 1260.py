import sys
input = sys.stdin.readline
from collections import deque


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_bfs = [0] * (N + 1)
visited_dfs = [0] * (N + 1)
count = 1
cnt = 1

def bfs(k):
    global count
    
    q= deque([k])
    visited_bfs[k] = 1
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for g in graph[v]:
            if visited_bfs[g] == 0:
                count += 1
                visited_bfs[g] = count
                q.append(g)

def dfs(v):
    global cnt #몇 번째 방문했는지 세는 전역변수
    visited_dfs[v] = cnt
    print(v, end = ' ')
    for i in graph[v]:
        if visited_dfs[i] == 0: #방문 안 한 노드일 경우
            cnt += 1 #순차 증가
            dfs(i)
            
    
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(N + 1):
    graph[i].sort() 
    
dfs(R)
print()
bfs(R)
