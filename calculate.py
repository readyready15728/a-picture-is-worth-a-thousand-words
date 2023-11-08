import math
from collections import Counter

# Shamelessly stolen from Rosetta Code
def entropy(s):
    p, lns = Counter(s), float(len(s))
    return -sum(count/lns * math.log(count/lns, 2) for count in p.values())

with open('words') as f:
    words = f.readlines()

    entropies = [entropy(word.strip()) for word in words]
    entropy_avg = sum(entropies) / len(entropies)
    print(f'A picture is worth ~1000 × {entropy_avg:.2f}, or ~{1000 * entropy_avg:.2f} bits')
