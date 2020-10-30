import itertools
import random

names = [
    "p1",
    "p2",
    "p3",
    "p4",
    "p5",
    "p6",
    "p7",
    "p8"
    ]

all_pairs = list(itertools.combinations(names, 2))
random.shuffle(all_pairs)
used_pairs = []
num_rounds = 7
num_teams = len(names) / 2


for r in range(num_rounds):
    print("\nROUND" + str(r+1), end='')
    used = []
    t = 0
    rep = 0

    while(True):
        
        if t >= 4:
            break
        for p in all_pairs:
            if p[0] not in used and p[1] not in used:
                if t % 2 == 0:
                    print("")
                t += 1
                print("%s\t\t%s\t\t" % (p[0].title(), p[1].title()), end='')
                used.append(p[0])
                used.append(p[1])
                all_pairs.remove(p)
        if rep > 100:
            print(broken)
            break
        rep += 1

