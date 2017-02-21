import matplotlib.pyplot as plt
import numpy as np

total = 800
Pop = 100000
iniciais = 1
sadias = Pop - iniciais
mortas = 0
imunizadas = 0
contaminadas = iniciais

contagio = 0.02
mortalidade = 0.05

listaSadias = np.zeros(total)
listaMortas = np.zeros(total)
listaImuniz = np.zeros(total)

for it in range(total):
    
    if it % 100 == 0:
        print("Sadias:",sadias,"Mortas:",mortas,"Imunizadas:",imunizadas,"Total:",(iniciais+sadias+mortas+imunizadas))
    
    adoecem = contagio * sadias * contaminadas / Pop
    contaminadas = contaminadas + (1 - mortalidade) * adoecem
    mortas = mortas + mortalidade * adoecem
    imunizadas = imunizadas + (1 - mortalidade) * adoecem
    sadias = sadias - adoecem

    listaSadias[it] = sadias
    listaMortas[it] = mortas
    listaImuniz[it] = imunizadas

its = np.linspace(1,total,total) # 1, 2, 3..., total
plt.xlabel("Iteração")
plt.plot(its,listaSadias,label="Sadias")
plt.plot(its,listaMortas,label="Mortas")
plt.plot(its,listaImuniz,label="Imunizadas")
plt.legend()
plt.show()
