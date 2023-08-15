# LISTAS: estrutura de dados e uma sequência de itens
# delimitada por colchetes

lista = [1, 2, 3, 4]

# listas são heterogêneas (no Python), ou seja, podem ter strings, inteiros, floats e afins -> NÃO SÃO TODAS AS LINGUAGENS!
exemplo = [3, 2, "abc", 4, 5, "aaaaaaaaaa"]

# indices negativos começam sempre do -1
lista = [3,4,5,6]
print(lista[-1])

# len 
print(len(lista))

# append para adicionar
lista.append(300)
print(lista)

# insert(indice, item) -> adiciona um item em determinada posição
lista.insert(1, 99)
print(lista)

# pop remove o ultimo elemento da lista
lista1 = [3,2,4,5]
lista1.pop()
print(lista)

# pop(indice) remove o item da lista em especifico
lista3 = [1, 3, 5, 7]
lista3.pop(1)
print(lista3)

# remove -> remove o primeiro valor IGUAL ao parametro passado (remove somente o primeiro)
exemplo2 = [3, 5, 6, 7, 8, 5, 9]
exemplo2.remove(5)
print(exemplo2)

lista10 = [1,2,3,4,5,6,7,8]
if 8 in lista10:
    lista10.remove(8)
print(lista10)

# count - quantas vezes um item aparece na lista
lista4 = [3,4,5,6,7, 5, 5]
print(lista4.count(5))

print(lista4.index(5)) # index - em qual indice está o PRIMEIRO elemento que aparece

# sort -> ordena de forma crescente uma lista
lista4.sort()
print(lista4)

# de forma decrescente
lista4.sort(reverse=True)
print(lista4)

# com strings
nomes = ["Maria", "Carol", "Socorro", "Aegis"]
nomes.sort()
print(nomes)

# max - maior elemento da lista
print(max(nomes))

# min - menor elemento da lista
print(min(nomes))

# sum -> somar todos os elementos da lista NUMERICA
print(sum(lista4))

# média de uma lista
media = sum(lista4) / len(lista4)
print(media)

# usuario preenchendo uma lista
numeros = []
for i in range(5):
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)
print(numeros)

# percorrer itens da lista
lista = [2, 4, 6, 8, 9, 10, 11, 12, 14, 15]
cont = 0
for item in lista:
    if item % 2 == 0:
        cont += 1
print(f"Quantidade de pares: {cont}")

# caso queira alterar indices da lista
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)

# concatenação (juntar listas)
lista1 = [3, 4, 5]
lista2 = ["Titan", "Robs", "Guigo", "Dynquedo"]
lista3 = lista1 + lista2 #coloca na ordem colocada e pode ir indo coloando mais listas pra concatenar
print(lista3)