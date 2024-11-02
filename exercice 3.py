
T1 = [4, 8, 7, 12]
T2 = [3, 6, 2, -1]
T = []
i, j = 0, 0
while i < len(T1) or j < len(T2):
    if i < len(T1):
        T.append(T1[i])
        i += 1
    if j < len(T2):
        T.append(T2[j])
        j += 1
print("Tableau T:", T)