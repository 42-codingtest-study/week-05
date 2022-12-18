import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

bfs_visited = [False] * (n + 1)
dfs_visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

def bfs(v):
    bfs_visited[v] = True

    queue = deque()
    queue.append(v)

    while queue:
        pop_v = queue.popleft()
        print(pop_v, end=" ")

        for j in range(1, n + 1):
            if not bfs_visited[j] and graph[pop_v][j] == 1:
                queue.append(j)
                bfs_visited[j] = True

def dfs(v):
    dfs_visited[v] = True
    print(v, end=" ")

    for j in range(1, n + 1):
        if not dfs_visited[j] and graph[v][j] == 1:
            dfs(j)

dfs(v)
print()

bfs(v)