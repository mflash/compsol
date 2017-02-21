import string, re

arq = open("shakespeare2.txt")
dic = {}

for line in arq.readlines():
    line = line.strip()
    if line:
        for word in line.split(' '):
            if len(word) == 0:
                continue
            if word in dic:
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1

arq.close()

s = [(k, dic[k]) for k in sorted(dic, key=dic.get, reverse=True)]

print("Palavras distintas:",len(s))
for k,v in s[:20]:
    print(k,'->',v)
