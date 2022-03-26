from collections import deque
import sys

dq = deque()

n = int(input())
for _ in range(n):
    line = sys.stdin.readline().split()

    if line[0] == 'push_front':
        dq.appendleft(int(line[1]))
    elif line[0] == 'push_back':
        dq.append(int(line[1]))
    elif line[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif line[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(dq))
    elif line[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif line[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif line[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)

