from collections import deque


def solution(priorities, location):
    priorities_list = {}
    print_list = deque()
    priorities = deque(priorities)

    priorities[location] = str(priorities[location])

    for i in range(len(priorities)):
        if int(priorities[i]) not in priorities_list:
            priorities_list[int(priorities[i])] = 1
        else:
            priorities_list[int(priorities[i])] += 1

    priorities_list.sort()
    cnt = 0
    while priorities_list:
        for i in range(len(priorities)):
            if int(priorities[0]) < priorities_list[-1]:
                priorities.append(priorities.popleft())
            else:
                if type(priorities[0]) == str:
                    cnt += 1
                    return cnt
                else:
                    priorities.popleft()
                    cnt += 1
        priorities_list.pop()

    return cnt