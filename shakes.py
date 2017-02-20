import string, re

arq = open("shakespeare2.txt")
trans = str.maketrans(dict.fromkeys(string.punctuation))
dic = {}

for line in arq.readlines():
    line = line.strip()
    if line and not line.isdigit():
        line = line.translate(trans)
        for word in line.lower().split(' '):
            if len(word) == 0:
                continue
            if word in dic:
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1

arq.close()

s = [(k, dic[k]) for k in sorted(dic, key=dic.get, reverse=True)]

print("Palavras distintas:",len(s))
for k,v in s:
    print(k,'->',v)
