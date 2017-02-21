arq = open("poa_temps.txt")
arq.readline() # Pula o cabeçalho

minimas = [0] * 12
maximas = [0] * 12
totminimas = [0] * 12
totmaximas = [0] * 12

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

mins = [k[0]/k[1] for k in zip(minimas,totminimas)]
#print(mins)

maxs = [k[0]/k[1] for k in zip(maximas,totmaximas)]
#print(maxs)

ampli = [k[0]-k[1] for k in zip(maxs,mins)]
#print(ampli)

mes_menor_ind, mes_menor_temp = min(enumerate(mins), key=lambda t: t[1])
mes_maior_ind, mes_maior_temp = max(enumerate(maxs), key=lambda t: t[1])
ampli_ind, ampli_val = max(enumerate(ampli), key=lambda t: t[1])

print("Mês com menor média de temperatura mínima:",mes_menor_ind+1,"(",mes_menor_temp,")")
print("Mês com maior média de temperatura máxima:",mes_maior_ind+1,"(",mes_maior_temp,")")
print("Mês com maior amplitude térmica:",ampli_ind+1,"(",ampli_val,")")

