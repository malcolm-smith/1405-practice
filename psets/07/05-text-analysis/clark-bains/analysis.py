wordList = []
followingWordFrequency = {}
wordFrequency = {}
def load(filename):
    global wordList, wordFrequency, followingWordFrequency
    wordList = []
    followingWordFrequency = {}
    wordFrequency = {}
    f = open (filename, 'r')
    for line in f:
        wordList += line.split (' ')
    f.close()
    tot = 0
    for wordIdex in range(len(wordList)):
        word = wordList[wordIdex]
        nextWord = wordList[wordIdex + 1] if (wordIdex < len(wordList)-1) else None
        if word not in followingWordFrequency:
            followingWordFrequency[word] = {}
        if nextWord not in followingWordFrequency[word]:
            followingWordFrequency[word][nextWord] = 0
        if word not in wordFrequency:
            wordFrequency[word] = 0
        wordFrequency[word] += 1
        followingWordFrequency[word][nextWord] += 1
    print (followingWordFrequency,tot)
    
def commonword(l1):
    for tstword in l1:
        if tstword not in wordFrequency:
            return None
    if len(l1) == 0:
        return None
    mostFrequentKey = wordFrequency[l1[0]]
    mostFrequentVal = 0
    for i in l1:
        if wordFrequency[i] > mostFrequentVal:
            mostFrequentVal = wordFrequency[i]
            mostFrequentKey = i
    return mostFrequentKey

def commonpair(s1):
    mostFrequentKey = None
    mostFrequentVal = 0
    if (s1 not in followingWordFrequency):
        return None
    for followingWord in followingWordFrequency[s1].keys():
        if followingWordFrequency[s1][followingWord] > mostFrequentVal:
            mostFrequentVal = followingWordFrequency[s1][followingWord] 
            mostFrequentKey = followingWord
    return mostFrequentKey
def countall():
    return len(wordList)
def countunique():
    return len(followingWordFrequency)