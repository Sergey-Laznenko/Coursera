def next_idx(idx):
    return idx + 1 if idx < len(b) - 1 else idx


_ = input()
s = sorted([(d, i + 1) for i, d in enumerate(map(int, input().split()))])
_ = input()
b = sorted([(d, i + 1) for i, d in enumerate(map(int, input().split()))])
idx, res = 0, []
for d, i in s:
    while abs(d - b[next_idx(idx)][0]) < abs(d - b[idx][0]):
        if idx < next_idx(idx):
            idx = next_idx(idx)
        else:
            break
    res.append([i, b[idx][1]])
print(*[n for i, n in sorted(res)])
