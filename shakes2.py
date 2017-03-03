import string, re
import numpy as np
import matplotlib.pyplot as plt

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

print(s[:20])
print("Palavras distintas:",len(s))
for k,v in s[:20]:
    print(k,'->',v)

nums = np.linspace(1,20,20) # 1, 2, 3..., 20
plt.xlabel("Palavras")
plt.ylabel("Frequência")
#plt.xticks(np.arange(13), calendar.month_abbr[0:13])
dados1,dados2 = zip(*s[:20])
print(dados1)
print(dados2)
plt.bar(nums,dados2)
plt.xticks(nums,dados1)
plt.show()

