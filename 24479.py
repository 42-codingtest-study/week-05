# _*_ coding: utf-8 _*_
# 알고리즘 수업 - 깊이 우선 탐색 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) #런타임 에러 방지

N, M, R = map(int, input().split()) #정점의 수(N), 간선의 수(M), 시작 정점(R) 입력 받기
graph = [[] for _ in range(N + 1)] #[] [] [] [] [] []
visited = [0] * (N + 1) #방문 횟수 [0 0 0 0 0 0]
cnt = 1 

def dfs(graph, v, visited):
    global cnt #몇 번째 방문했는지 세는 전역변수
    visited[v] = cnt
    for i in graph[v]:
        if visited[i] == 0: #방문 안 한 노드일 경우
            cnt += 1 #순차 증가
            dfs(graph, i, visited)
            
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(N + 1):
    graph[i].sort() #오름차순 정리
    
dfs(graph, R, visited)
    
for i in range(N + 1):
    if i != 0: #첫 번째 값 0 출력 방지
        print(visited[i]) #visited 인덱스값이 0인 것은 보기 편하게 하기 위해서 한 것이므로 인덱스의 값이 0일 때 값 빼고 출력하기