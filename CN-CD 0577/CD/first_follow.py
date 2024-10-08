gram = {
  "E": ["E+T", "T"],
  "T": ["T*F", "F"],
  "F": ["(E)", "i"]
}

def removeDirectLR(gramA, A):
    temp = gramA[A]
    tempCr = []
    tempInCr = []
    for i in temp:
        print(i)
        if i[0] == A:
            tempInCr.append(list(i[1:]) + [A + "'"])  # Convert i[1:] to a list
        else:
            tempCr.append(list(i) + [A + "'"])
    tempInCr.append(["e"])  # Add epsilon for the recursive rule
    gramA[A] = tempCr
    gramA[A + "'"] = tempInCr
    return gramA

def checkForIndirect(gramA, a, ai):
    if ai not in gramA:
        return False
    if a == ai:
        return True
    for i in gramA[ai]:
        if i[0] in gramA:
            return checkForIndirect(gramA, a, i[0])
    return False

def rep(gramA, A):
    temp = gramA[A]
    newTemp = []
    for i in temp:
        if checkForIndirect(gramA, A, i[0]):
            for k in gramA[i[0]]:
                newTemp.append(k + i[1:])
        else:
            newTemp.append(i)
    gramA[A] = newTemp
    return gramA

def rem(gram):
    gramA = gram.copy()
    for i in gram:
        for j in gramA[i]:
            # print(i, j)
            if i == j[0]:
                gramA = removeDirectLR(gramA, i)
                break
    return gramA

def first(gram, term):
    a = []
    if term not in gram:
        return [term]
    for i in gram[term]:
        if i[0] not in gram:
            a.append(i[0])
        else:
            a += first(gram, i[0])
    return a

result = rem(gram)
print(result)
firsts = {}
for i in result:
    firsts[i] = first(result, i)
    print(f'First({i}): ', firsts[i])

def follow(gram, term):
    a = []
    for rule in gram:
        for i in gram[rule]:
            if term in i:
                indx = i.index(term)
                if indx + 1 != len(i):
                    a += first(gram, i[indx + 1])
                else:
                    if rule != term:
                        a += follow(gram, rule)
    return a

follows = {}
for i in result:
    follows[i] = list(set(follow(result, i)))
    follows[i].append("$")
    print(f'Follow({i}):', follows[i])










# gram={"E":["E+T","T"],
#       "T":["T*F","F"],
#       "F":["(E)","i"]
#      }

# def removeDirectLR(gramA,A):
# 	temp=gramA[A]
# 	tempCr=[]
# 	tempInCr=[]
# 	for i in temp:
# 		if i[0]==A:
# 			tempInCr.append(i[1:]+[A+""])
# 		else:
# 			tempCr.append(i+[A+""])
# 	tempInCr.append(["e"])
# 	gramA[A]=tempCr
# 	gramA[A+""]=tempInCr
# 	return gramA

# def checkForIndirect(gramA,a,ai):
# 	if ai not in gramA:
# 		return False
# 	if a==ai:
# 		return True
# 	for i in gramA[ai]:
# 		if i[0]==ai:
# 			return False
# 		if i[0] in gramA:
# 			return checkForIndirect(gramA,a,i[0])
# 	return False

# def rep(gramA,A):
# 	temp=gramA[A]
# 	newTemp=[]
# 	for i in temp:
# 		if checkForIndirect(gramA,A,i[0]):
# 			t=[]
# 			for k in gramA[i[0]]:
# 				t=[]
# 				t+=k
# 				t+=i[1:]
# 				newTemp.append(t)
# 		else:
# 			newTemp.append(i)
# 	gramA[A]=newTemp
# 	return gramA

# def rem(gram):
# 	c = 1
# 	conv = {}
# 	gramA = {}
# 	reconv= {}
# 	for j in gram:
# 		conv[j] = "A" + str(c)
# 		gramA["A"+str(c)] = []
# 		c += 1

# 	for i in gram:
# 		for j in gram[i]:
# 			temp = []
# 			for k in j:
# 				if k in conv:
# 					temp.append(conv[k])
# 				else:
# 					temp.append(k)
# 			gramA[conv[i]].append(temp)

# 	for i in range(c-1,0,-1):
# 		ai="A"+str(i)
# 		for j in range(0,i):
# 			aj=gramA[ai][0][0]
# 			if ai!=aj:
# 				if aj in gramA and checkForIndirect(gramA,ai,aj):
# 					gramA=rep(gramA,ai)

# 	for i in range(1 , c):
# 		ai = "A"+str(i)
# 		for j in gramA[ai]:
# 			if(ai == j[0]):
# 				gramA = removeDirectLR(gramA , ai)
# 				break
# 	op = {}
# 	for i in gramA:
# 		a = str(i)
# 		for j in conv:
# 			a = a.replace(conv[j] , j)
# 		reconv[i] = a

# 	for i in gramA:
# 		I = []
# 		for j in gramA[i]:
# 			k = []
# 			for m in j :
# 				if m in reconv:
# 					k.append(m.replace(m , reconv[m]))
# 				else:
# 					k.append(m)
# 			I.append(k)
# 		op[reconv[i]] = I

# 	return op

# result = rem(gram)

# def first(gram , term):
# 	a = []
# 	if term not in gram:
# 		return [term]
# 	for i in gram[term]:
# 		if i[0] not in gram:
# 			a.append(i[0])
# 		elif i[0] in gram :
# 			a += first(gram , i[0])
# 	return a

# firsts = {}
# for i in result:
# 	firsts[i] = first(result , i)
# 	print(f'First({i}): ' , firsts[i])

# def follow(gram , term):
# 	a=[]
# 	for rule in gram:
# 		for i in gram[rule]:
# 			if term in i:
# 				temp = i
# 				indx = i.index(term)
# 				if indx+1!=len(i):
# 					if i[-1] in firsts:
# 						a+=firsts[i[-1]]
# 					else:
# 						a+=[i[-1]]
# 				else:
# 					a+=["e"]
# 					if rule!= term and "e" in a:
# 						a+= follow(gram,rule)
# 	return a


# follows={}
# for i in result:
# 	follows[i] = list(set(follow(result,i)))
# 	if "e" in follows[i]:
# 		follows[i].pop(follows[i].index("e"))
# 	follows[i]+=["$"]
# 	print(f'Follow({i}):',follows[i])



