from itertools import combinations


def solution(orders, course):
    for i in range(len(orders)):
        orders[i] = sorted(list(orders[i]))
    new = {}

    for order in course:
        for i in range(len(orders)):
            if len(orders[i]) >= order:
                combi = list(combinations(orders[i], order))
                for c in combi:
                    nc = ''.join(c)
                    if nc in new:
                        new[nc] += 1
                    else:
                        new[nc] = 1

    result = []
    for order in course:
        max_num = 0
        max_key = ''
        for key in new:
            if len(key) != order:
                continue
            else:
                if new[key] == 1:
                    continue
                elif new[key] > max_num:
                    max_num = new[key]
                    max_key = key
        for key in new:
            if len(key) != order:
                continue
            if new[key] == max_num:
                result.append(key)

    return sorted(result)