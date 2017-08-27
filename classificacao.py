from sklearn.naive_bayes import MultinomialNB

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

marcacoes = [1,1,1,-1,-1,-1]

modelo = MultinomialNB() # cria um modelo 
modelo.fit(dados, marcacoes) # modelo usa a funcao fit para treinar os dados com base nas marcacoes

misterioso1 = [1,0,1]
misterioso2 = [1,1,0]
misterioso3 = [0,0,1]

teste = [misterioso1, misterioso2, misterioso3]

marcacao_teste = [-1,1,-1]

resultado = modelo.predict(teste)

diferencas = resultado - marcacao_teste


total_de_acertos = 0
for d in diferencas:
	if d == 0:
		total_de_acertos = total_de_acertos + 1

total_de_elementos = len(teste)

taxa_de_acerto = total_de_acertos/total_de_elementos*100.0

print(resultado, diferencas, taxa_de_acerto)
# (array([-1,  1, -1]), array([0, 0, 0]), 100.0)