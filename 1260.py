# DFS와 BFS
# https://www.acmicpc.net/problem/1260

def dfs(v):
    print(v, end=' ')
    visit[v] = 1	# 방문했으므로 1로 변경 
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:	# dfs이므로 s[v]행에서 다른 간선이 있는지 확인한다
            dfs(i)	# 간선이 존재한다면 다시 재귀

def bfs(v):
    queue = [v]
    visit[v] = 0	# dfs에서 값을 1로 변경해서 이번에는 0으로 방문 여부 확인
    while(queue):
        v = queue[0]
        print(v, end=' ')	# 방문한 점 출력
        del queue[0]
        for i in range(1, n + 1):	# 이번에는 조건문을 만족했을 때 재귀를 도는게 아니라 값을 다 추가해준다.
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)		# 정점이 연결하는 다른 정점들을 queue에 넣어준다.
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]	# 그래프 생성
visit = [0 for i in range(n + 1)]	# 방문여부 확인
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1		# 간선 설정
    s[y][x] = 1		# 간선 설정
    
dfs(v)
print()
bfs(v)