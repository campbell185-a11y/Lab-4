#Adrien Campbell Python Lab 4 dictionary
names = ['Joe', 'Tom', 'Barb', 'Sue', 'Sally"']
scores = [10,23,13,18,12]
scoreDict = {}
def makeDictionary(name, score):
    

    for i in range(len(name)):

        scoreDict[name[i]] = score[i]
    return scoreDict

print(makeDictionary(names,scores))

print(scoreDict.get('Barb'))

scoreDict['John'] = 19

print(scoreDict)

scoreList = list(scoreDict.values())

scoreList.sort()

print(scoreList)

def mean(aList):
    return sum(aList) / len(aList)

averageScore = mean(scoreList)

print(averageScore)

scoreDict['Sally'] = 13

print(scoreDict)

del scoreDict['Tom']

print(scoreDict)