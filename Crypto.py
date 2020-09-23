import sys
import time

start = time.time()

# phrase = "fndfkn gtxygkkp anjna xd anqngato idmgugpq gq angkkp lyqx"
# FE WDPSHFYKNID UPSKIH FI KY NPBI PS IHVRPKTYS MY MNI GIXK FI YVK YC MRNYYO
# phrase = "qznqtz uzlxoz onmx"





phrase = ""
# if len(sys.argv) > 1:
#     for i in range(1,len(sys.argv)):
#         if i != len(sys.argv)-1:
#             phrase += sys.argv[i] + " "
#         else:
#             phrase += sys.argv[i]
# else:
#     phrase = sys.argv[1]

phrase = "Z BLKIIHB OV WQIXKI KC XUH SKCSLHXH DWKKL QCB ZX GQN UQLB"
# phrase = "jru fifr jpe str upi fpomh yfpsu ,u gtormf od trs;;u dovl smf o gr;; jptton;r gpt dsuomh yjsy yp upi"
phrase = phrase.lower()
allWords = phrase.split(" ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
for j in range(0,len(allWords)):
    each = allWords[j]
    each = list(each)
    # for i in range(0,len(each)):
    #     if each[i] not in alphabet:
    #         each[i] = ""
    each = "".join(each)
    allWords[j] = each
phrase = " ".join(allWords)

wordsDoc = open("enable.txt", "r")
words = wordsDoc.readlines()

# Create Patters for every word in the dictionary
patterns = {}
for word in words:
    s = ""
    letDict = {}
    count = 0
    check = 1
    for letter in word[0:-1]:
        if letter not in letDict:
            letDict[letter] = str(count)
            count += 1
        if check == len(word)-1:
            s += letDict[letter]
        else:
            s += letDict[letter] + ","
        check += 1
    if s not in patterns:
        patterns[s] = set()
    patterns[s].add(word[0:-1])

patterns['0'] = ['a','i']



dictionary = []
for word in words:
    dictionary.append(word[0:-1])
dictionary.append('i')
dictionary.append('a')

letterFreq = "etaoinsrhldcumfpgwybvkxjqz"
biFreq = {"t": "h", "h": "e", "i": "n","e": "r",
"a": "n","r": "e","o": "n","a": "t",
"e": "n","n": "d","t": "i","e": "s"
}
doubleFreq = "lseotfprmcn"

lettFreq = letterFreq.split()

def findFrequency(string):
    dictionary = {}
    for each in string:
        if each != " ":
            if each not in dictionary:
                dictionary[each] = 1
            elif each in dictionary:
                dictionary[each] += 1
    return dictionary

def createPattern(string):
    s = ""
    letDict = {}
    count = 0
    check = 1
    for letter in string:
        if letter not in letDict:
            letDict[letter] = str(count)
            count += 1
        if check == len(string):
            s += letDict[letter]
        else:
            s += letDict[letter] + ","
        check += 1
    return s


def recur(sentence,position,correct,sequence,ordered,match):
    # print(sentence)
    #This is base case. It checks if I'm done.
    bool = True
    for x in range(0,len(sentence)):
        each = sentence[x]
        each = list(each)
        for i in range(0,len(each)):
            if allWords[x][i] in correct:
                if correct[allWords[x][i]] != each[i]:
                    each[i] = correct[allWords[x][i]]
                    sentence[x] = "".join(each)
            else:
                break
    for each in sentence:
        if each not in dictionary:
            bool = False
    if bool == True:
        check = "".join(sentence)
        sequenceCheck = createPattern(noSpace)
        if sequenceCheck == sequence:
            return " ".join(sentence)

    possibilities = patterns[createPattern(ordered[position])]
    start = ordered[position]
    each = list(start[:])
    changed = set()
    for each2 in correct:
        for i in range(0,len(each)):
            if i not in changed:
                if each2 == each[i]:
                    each[i] = correct[each2]
                    changed.add(i)
                else:
                    newlist = list()
                    for k in correct.keys():
                        newlist.append(k)
                    if each2 == newlist[-1]:
                        each[i] = "."
    each = "".join(each)
    for some in possibilities:
        bool2 = True
        for i in range(0,len(some)):
            if each[i] != ".":
                if each[i] != some[i]:
                    bool2 = False
            else:
                if some[i] in correct.values():
                    bool2 = False
        if bool2 == True:
            newCorr = correct.copy()
            for i in range(0,len(some)):
                newCorr[start[i]] = some[i]
            sent = sentence[:]

            sent[match[position]] = some
            final = recur(sent, position+1,newCorr,sequence,ordered,match)
            if final != None:
                return final
        else:
            continue


noSpace = "".join(allWords)
sequence = createPattern(noSpace)

orderingStart = {}
for i in range(0,len(allWords)):
    orderingStart[allWords[i]] = len(patterns[createPattern(allWords[i])])
ordered = []
# for key, value in sorted(orderingStart.iteritems(), key=lambda (k,v): (v,k)):
#     ordered.append("%s" % (key))
#
ordered = sorted(orderingStart, key=orderingStart.get)
# #
#
# ordered = sorted(ordered, key=len)
# max = 0
# index = 0
# for i in range(0,len(ordered)):
#     if len(ordered[i]) > max:
#         max = len(ordered[i])
#         index = i
# changing = ordered[index]
# ordered.pop(index)
# ordered.insert(0,changing)
#

# ordered = sorted(orderingStart, key=len(orderingStart.keys()))


match = {}
for i in range(0, len(ordered)):
    for j in range(0, len(allWords)):
        if ordered[i] == allWords[j]:
            match[i] = j
print(match)
correct = {}

boolean = True
for each in allWords:
    if each not in dictionary:
        boolean = False
if boolean == True:
    print(phrase)
else:
    startPoss = patterns[createPattern(ordered[0])]
    sent = allWords[:]
    finalList = []
    print(sent, finalList)
    for each in startPoss:
        sent[match[0]] = each
        for i in range(0,len(ordered[0])):
            correct[ordered[0][i]] = each[i]
        final = recur(sent,1,correct,sequence,ordered,match)
        if final != None:
            print(final)
            break
print(time.time()-start)
