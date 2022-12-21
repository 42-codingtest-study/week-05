# DFS와 BFS

from collections import deque
import sys
input = sys.stdin.readline

# n=정점개수, m=간선개수, v=탐색시작점
n, m, v = map(int, input().split())

# 인접영행렬
graph = [[]for _ in range(n+1)]
# [[], [], [], [], []]

# 방문한곳체크기록할 리스트
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)
# print(visited_dfs)
# [0, 0, 0, 0, 0]

#  노드 연결
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort()

#깊이 우선 탐색
cnt_dfs = 1
def dfs(v):
    global cnt_dfs
    # 방문 노드 체크
    visited_dfs[v] = cnt_dfs
    print(v,end=' ')
    # print(graph[v])
    #재귀
    for i in graph[v]:
        if visited_dfs[i] == 0:
            cnt_dfs += 1
            dfs(i)

cnt_bfs = 1
def bfs(v):
  #방문해야할 곳을 순서대로 넣을 
    global cnt_bfs
    queue=deque([v])
    # print(queue)
    visited_bfs[v]=cnt_bfs
    # print(visited_bfs)
    #큐안에 데이터없을때까지
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        
        for g in graph[v]:
            if visited_bfs[g]==0:
            #   방문한 적 없는 인적 노드 방문
                cnt_bfs += 1
                visited_bfs[g]=1
                queue.append(g)


dfs(v)
print()
bfs(v)
