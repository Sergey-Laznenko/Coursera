"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
"""


text = open('input.txt', 'r', encoding='utf8')
separation = []
output_list = []
couple = dict()
for j in text:
    j = j.split()
    for p in range(len(j)):
        separation.append(j[p])
for i in separation:
    if i not in couple:
        couple[i] = 0
        output_list.append(couple[i])
    else:
        couple[i] += 1
        output_list.append(couple[i])
print(*output_list)
