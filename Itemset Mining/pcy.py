data = [[1, 2, 3], [2, 3, 6], [1, 3, 4], [3, 4, 6],
        [1, 5, 6], [2, 4, 6], [1, 2, 5], [2, 4, 5],
        [1, 3, 5], [2, 3, 4], [4, 5, 6], [3, 5, 6]]

bucket = 13
minsup = 4


def PCYpass(data, bucket, minsup):
    candidatelist1 = []
    finallist1 = []
    support_finallist1 = []
    # ----------load all data into list------------#
    for i in range(len(data)):
        for e in data[i]:
            if e not in candidatelist1:
                candidatelist1.append(e)
    # ----------Delete duplicate words-------------#
    sorted(candidatelist1)
    # ----------Filter out < minsup----------------#
    temp = 0
    for e in candidatelist1:
        for basket in data:
            for item in basket:
                if e == item:
                    temp += 1
        if temp >= minsup:
            support_finallist1.append(temp)
            finallist1.append(e)
        temp = 0
    finallist1 = sorted(finallist1)
    print("(a) By any method, compute the support for each item and each pair of items.")
    for i in range(len(finallist1)):
        print(" # of support for [%s] : %d " % (finallist1[i], support_finallist1[i]))
    PCYpass2(data, bucket, minsup, finallist1)


def PCYpass2(data, bucket, minsup, finallist1):
    bitmap, countofbit, pairs = [0] * bucket, [0] * bucket, []
    # starts to combine all possible combination via given data
    # bucket : (x * y) % 11
    for index in range(len(data)):
        for i in range(len(data[index]) - 1):
            for j in range(i + 1, len(data[index])):
                countofbit[(data[index][i] * data[index][j]) % 11] += 1
                if [data[index][i], data[index][j]] not in pairs:
                    pairs.append([data[index][i], data[index][j]])
    for i in range(len(countofbit)):
        if countofbit[i] >= minsup:
            bitmap[i] = 1
        else:
            bitmap[i] = 0
    # Extra step for homework : compute the support for each pair
    temp = 0
    support_pairs = []
    for i in range(len(pairs)):
        for j in range(len(data)):
            if set(pairs[i]).issubset(set(data[j])):
                temp += 1
    support_pairs.append(temp)
    temp = 0
    # prunning 1 : all each item in pairs are in finallist
    pairs_prun_1 = []
    for i in range(len(pairs)):
        for j in range(len(pairs[i]) - 1):
            if pairs[i][j] in finallist1 and pairs[i][j + 1] in finallist1:
                pairs_prun_1.append(pairs[i])
    # prunning 2(essence) : check if correspondding bitmap is 1
    pairs_prun_2 = []
    for i in range(len(pairs_prun_1)):
        for j in range(len(pairs_prun_1[i]) - 1):
            if bitmap[(pairs_prun_1[i][j] * pairs_prun_1[i][j + 1]) % 11] == 1:
                pairs_prun_2.append(pairs_prun_1[i])
    # add qualify paris to new finalist
    finallist2 = []
    support_finallist2 = []
    temp = 0
    for i in range(len(pairs_prun_2)):
        for j in range(len(data)):
            if set(pairs_prun_2[i]).issubset(set(data[j])):
                temp += 1
    if temp >= minsup:
        support_finallist2.append(temp)
    finallist2.append(pairs_prun_2[i])
    temp = 0
    finallist2 = sorted(finallist2)
    for i in range(len(pairs)):
        print(" # of support for %s : %d " % (pairs[i], support_pairs[i]))
    print("(b) Which pairs hash to which buckets?")
    for i in range(len(pairs)):
        print(" %s hash to bucket : %s " % (pairs[i], (pairs[i][0] * pairs[i][1]) % 11))
    frequencybucket = []
    for i in range(len(bitmap)):
        if bitmap[i] == 1:
            frequencybucket.append(i)
    print("(c) Which buckets are frequent?")
    print(" Frequency buckets are : %s " % frequencybucket)
    print("(d) Which pairs are counted on the second pass of the PCY Algorithm?")
    print(" %s" % finallist2)


PCYpass(data, bucket, minsup)
