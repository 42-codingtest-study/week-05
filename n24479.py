#다시
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
#파이썬 재귀 최대 깊이 설정

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
path = []

result = [0] * (n - 1)
visited = [-1] * (n - 1)

cnt = 1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, len(graph)):
    graph[i].sort()

def dfs(start):
    global cnt
    result[start] = cnt
    graph[start].sort()

    for j in graph[start]:
        if not result[j]:
            cnt += 1
            dfs(j)

dfs(r)

for i in graph[1 : n + 1]:
    print(result[i])