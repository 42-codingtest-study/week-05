# 강의실 배정
# https://www.acmicpc.net/problem/11000

import sys
import heapq

input = sys.stdin.readline
time = []
N = int(input())
for _ in range(N) :
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key = lambda x : (x[0], x[1]))
answer = []
heapq.heappush(answer, time[0][1])
for i in range(1, N) :
    if time[i][0] < answer[0] :
        heapq.heappush(answer, time[i][1])
    else :
        heapq.heappop(answer)
        heapq.heappush(answer, time[i][1])
print(len(answer))