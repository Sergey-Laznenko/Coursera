"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько,
выведите то, которое меньше в лексикографическом порядке.
"""


file = open('input.txt')
myDict = {}
for word in file.read().split():
    myDict[word] = myDict.get(word, 0) + 1
myList = sorted(myDict.items())
myList.sort(key=lambda x: x[1], reverse=True)
print(myList[0][0])
