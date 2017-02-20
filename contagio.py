Pop = 100000
iniciais = 1
sadias = Pop - iniciais
mortas = 0
imunizadas = 0
contaminadas = iniciais

contagio = 0.01
mortalidade = 0.05

for it in range(200):
    
    print("Sadias:",sadias,"Mortas:",mortas,"Imunizadas:",imunizadas,"Total:",(iniciais+sadias+mortas+imunizadas))
    
    adoecem = contagio * sadias * contaminadas / Pop
    contaminadas = contaminadas + (1 - mortalidade) * adoecem
    mortas = mortas + mortalidade * adoecem
    imunizadas = imunizadas + (1 - mortalidade) * adoecem
    sadias = sadias - adoecem
