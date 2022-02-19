from collections import deque
from sys import stdin

move = ['<','>','-']
T = int(stdin.readline())

for j in range(T) :
    L = list(stdin.readline().strip())
    password = []
    save = []

    for i in range(len(L)):
        if L[i] not in move:
            password.append(L[i])
        elif L[i] == '<' and password :
            save.append(password.pop())
        elif L[i] == '>' and save :
            password.append(save.pop())
        elif L[i] == '-' and password :
            password.pop()

    while save :
        password.append(save.pop())

    answer = ''.join(password)

    print(answer)


