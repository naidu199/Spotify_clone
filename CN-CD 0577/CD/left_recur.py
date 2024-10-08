gram = {}

def add(s):
    s = s.replace(" ", "").replace("\n", "")
    x = s.split("->")
    y = x[1]
    x.pop()
    z = y.split("|")
    x.append(z)
    gram[x[0]] = x[1]

def removeDirectLR(gramA, A):
    """gramA is dictionary"""
    temp = gramA[A]
    temper = []
    templner = []
    for i in temp:
        if i[0] == A:
            templner.append(i[1:] + [A + "'"])
        else:
            temper.append(i + [A + "'"])
    temper.append(["e"])
    gramA[A] = temper
    gramA[A + "'"] = templner
    return gramA

def checkForIndirect(gramA, a, ai):
    if ai not in gramA:
        return False
    if a == ai:
        return True
    for i in gramA[ai]:
        if i[0] == ai:
            return False
        if i[0] in gramA:
            return checkForIndirect(gramA, a, i[0])
    return False

def rep(gramA, A):
    temp = gramA[A]
    newTemp = []
    for i in temp:
        if checkForIndirect(gramA, A, i[0]):
            t = []
            for k in gramA[i[0]]:
                t += k
            t += i[1:]
            newTemp.append(t)
        else:
            newTemp.append(i)
    gramA[A] = newTemp
    return gramA

def rem(gram):
    C = 1
    conv = {}
    gramA = {}
    revconv = {}
    for j in gram:
        conv[j] = "A" + str(C)
        gramA["A" + str(C)] = []
        C += 1

    for i in gram:
        for j in gram[i]:
            temp = []
            for k in j:
                if k in conv:
                    temp.append(conv[k])
                else:
                    temp.append(k)
            gramA[conv[i]].append(temp)

    # Processing indirect left recursion
    for i in range(C - 1, 0, -1):
        ai = "A" + str(i)
        for j in range(0, i):
            aj = gramA[ai][0][0]
            if ai != aj:
                if aj in gramA and checkForIndirect(gramA, ai, aj):
                    gramA = rep(gramA, ai)

    # Processing direct left recursion
    for i in range(1, C):
        ai = "A" + str(i)
        for j in gramA[ai]:
            if ai == j[0]:
                gramA = removeDirectLR(gramA, ai)
                break

    op = {}
    for i in gramA:
        a = str(i)
        for j in conv:
            a = a.replace(conv[j], j)
        revconv[i] = a

    for i in gramA:
        I = []
        for j in gramA[i]:
            k = []
            for m in j:
                if m in revconv:
                    k.append(revconv[m])
                else:
                    k.append(m)
            I.append(k)
        op[revconv[i]] = I
    return op

n = int(input("Enter No of Production: "))
for i in range(n):
    txt = input()
    add(txt)

result = rem(gram)

for x, y in result.items():
    print(f"{x} -> ", end="")
    for index, i in enumerate(y):
        for j in i:
            print(j, end="")
        if index != len(y) - 1:
            print(" | ", end="")
    print()
