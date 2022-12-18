#24480 dfs서준조교님 그만 뵙겠습니당ㅎㅎ
import sys
input = sys.stdin.readline
#재귀 허용 깊이를 수동으로 늘려주는 코드라 함
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
result = [0] * (N + 1)
cnt = 1

#연결된 노드 입력 받아오기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#내림차순 정리
for i in range(N + 1):
    graph[i].sort(reverse = True)


def dfs(node):
	global cnt
	visited[node] = 1
	result[node] = cnt

	for i in graph[node]:
		if visited[i] == 0:
			cnt += 1
			dfs(i)

dfs(R)

for i in range(N + 1):
	if i != 0:
		print(result[i])