import numpy as np
from collections import Counter

def levenshtein(source, target):
    if source == target:
        return 0
    elif len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)
    v0 = np.arange(len(target) + 1)
    v1 = np.ones(len(target) + 1) * (len(source) + 1)
    for i, s in enumerate(source):
        v1[0], v0[0] = min(v0[0] + 1, v1[0] + 1, v0[1] + (s != target[0]))
        for j, t in enumerate(target):
            cost = int(s != t)
            v1[j + 1], v0[j + 1] = min(v0[j] + cost, v1[j] + 1, v0[j + 1] + 1)
    return v1[-1]
