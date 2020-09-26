"""
Каждый из N школьников некоторой школы знает Mᵢ языков. Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""

n = int(input())
all = list()
vse = set()
just = set()
for i in range(n):
    p = set()
    m = int(input())
    for j in range(m):
        p.add(input())
    all.append(p)
vse = all[0]
just = all[0]
for i in range(1, len(all)):
    vse = vse | all[i]
    just = just & all[i]
print(len(just))
for i in range(len(just)):
    print(just.pop())
print(len(vse))
for i in range(len(vse)):
    print(vse.pop())
