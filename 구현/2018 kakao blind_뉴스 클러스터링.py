from string import ascii_lowercase
import math

def solution(str1, str2):
    alphabet = list(ascii_lowercase)
    s1 = {}
    s2 = {}
    str1 = str1.lower()
    str2 = str2.lower()

    for i in range(len(str1)):
        if i == 0:
            continue
        else:
            if str1[i - 1] in alphabet and str1[i] in alphabet:
                if (str1[i - 1] + str1[i]) in s1:
                    s1[str1[i - 1] + str1[i]] += 1
                else:
                    s1[str1[i - 1] + str1[i]] = 1

    for i in range(len(str2)):
        if i == 0:
            continue
        else:
            if str2[i - 1] in alphabet and str2[i] in alphabet:
                if (str2[i - 1] + str2[i]) in s2:
                    s2[str2[i - 1] + str2[i]] += 1
                else:
                    s2[str2[i - 1] + str2[i]] = 1
    inter = 0
    union = 0
    for key in s1:
        if key in s2:
            inter += min(s1[key], s2[key])
            union += max(s1[key], s2[key])
        else:
            union += s1[key]
    for key in s2:
        if key not in s1:
            union += s2[key]

    if union == 0:
        answer = 65536
    else:
        answer = math.trunc(inter / union * 65536)
    return None




