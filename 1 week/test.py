A = [2,2,4,5,8,9,13,16,22,55,56]
B = [0,1,3,3,4,8,11,13,15,15,20,23,35,37,42,74]


C = []

i = 0
j = 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1
while i < len(A):
        C.append(A[i])
        i += 1
while j < len(B):
        C.append(B[j])
        j += 1
print(C)
