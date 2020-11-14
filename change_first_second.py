#szotarfile = open("szótár.txt", "r", encoding='utf-8')

#with open(hibagyujto, "w", encoding='utf-8') as ujraIras:
#    ujraIras.writelines(lista)

file = open("change.txt", "r", encoding='utf-8')
f = file.readlines()

words = []
for line in f:
    words.append(line.strip())

first = []
second = []

for e in words:
    first.append(e.split("#")[0])
    second.append(e.split("#")[1])

wordsChange = []

e = 0

while e < len(first):
    wordsChange.append(second[e] + "#" + first[e] + "\n")
    e += 1
    
    #for i in first:
    #    wordsChange.append(i + "\n")

with open("new.txt", "w", encoding='utf-8') as ujraIras:
    ujraIras.writelines(wordsChange)


print(wordsChange)