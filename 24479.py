# 알고리즘 수업 - 깊이 우선 탐색 1
# https://www.acmicpc.net/problem/24479

import sys

sys.setrecursionlimit(10 ** 6)		# 재귀의 깊이 제한을 늘려준다
input = sys.stdin.readline
N, M, R = map(int, input().split())
visited = [0] * (N + 1)
E = [[] for _ in range(N + 1)]
for _ in range(M) :
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
    
for i in range(N + 1) :
    E[i].sort()

cnt = 1

def dfs(R) :
    global cnt	# cnt를 계속 쓰기 위해 전역 변수로 사용
    visited[R] = cnt	# 방문 순서를 알기 위해 cnt입력
    for i in E[R] :
        if (visited[i] == 0) :
            cnt += 1	# 미방문했을 경우 재귀 + cnt 증가
            dfs(i)
            
dfs(R)            
print(*visited[1 : ], sep = '\n')