import calendar
import numpy as np
import matplotlib.pyplot as plt

arq = open("poa_temps.txt")
arq.readline() # Pula o cabeçalho

minimas = np.zeros(12)
maximas = np.zeros(12)
totminimas = np.zeros(12)
totmaximas = np.zeros(12)

for linha in arq.readlines():
    dados = linha.split()
    data = dados[0]
    precip = dados[1]
    maxima = float(dados[2])
    minima = float(dados[3])

    diamesano = data.split("/")
    mes = int(diamesano[1])-1

    # Há máxima?
    if maxima != -1:
        #print(mes,"maxima:",maxima)
        maximas[mes] += maxima
        totmaximas[mes] += 1

    # Há mínima?
    if minima != -1:
        #print(mes,"minima:",maxima)
        minimas[mes] += minima
        totminimas[mes] += 1

arq.close()

mins = minimas/totminimas
print(mins)

maxs = maximas/totmaximas
print(maxs)

ampli = maxs - mins
print(ampli)

mesMenor = mins.argmin()
mesMenorValor = mins.min()
mesMaior = maxs.argmax()
mesMaiorValor = mins.max()

ampliMaior = ampli.argmax()
ampliMaiorValor = ampli.max()

print("Mês com menor média de temperatura mínima:",mesMenor+1,"(",mesMenorValor,")")
print("Mês com maior média de temperatura máxima:",mesMaior+1,"(",mesMaiorValor,")")
print("Mês com maior amplitude térmica:",ampliMaior+1,"(",ampliMaiorValor,")")

meses = np.linspace(1,12,12) # 1, 2, 3..., 12
plt.xlabel("Meses")
plt.ylabel("Médias")
plt.xticks(np.arange(13), calendar.month_abbr[0:13])
plt.bar(meses,mins,label="Mínimas")
plt.bar(meses,maxs,bottom=mins,label="Máximas")
plt.legend()
plt.show()


