#24444 bfs도 서준조교님이시군요
from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)
visited[R] = 1
cnt = 1
q = deque([R])

#연결된 노드 입력 받아오기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#오름차순 정리(dfs니까)
for i in range(N + 1):
    graph[i].sort()

def bfs(node):
	#밖의 cnt를 사용하기 위해
	global cnt
	while q:
		node = q.popleft()
		for i in graph[node]:
			if visited[i] == 0:
				cnt += 1
				visited[i] = cnt
				q.append(i)

bfs(R)

for i in range(N + 1):
    if i != 0:
        print(visited[i])