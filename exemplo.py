# Strings: representam uma sequência de caracteres

texto = "Exemplo de texto" # por ser uma sequência, eu posso acessar essa variável pelos indices que cada string tem
a = texto[0] # lembrando que, indice = posição
print(a)

# percorre uma string
for c in texto:
    print(c) 

# tamanho da string
print(len(texto))

if "x" in texto: # confiro se há, dentro da sequência, um determinado valor
    print("O caractere x está contido na string")

# lower
print(texto.lower())

# title, que coloca as iniciais de cada palavra
print(texto.title())

# capitalize (coloca em maiusculo)
print(texto.capitalize())

# strip (remove os espaços)
texto2 = " exemplo de texto "
print(texto.strip())

# count = conta a quantidade de caracteres a partir de um caractere especifico
print(texto.count("e")) # lembrando que maiuscula e minuscula são coisas diferentes!

# replace = substitui uma substring por outra
texto3 = "banana, laranja, melao"
texto4 = texto3.replace("laranja", "melancia") # tem que ser exatamente igual
print(texto4)


'''import random
lista = []
for i in range(10):
    lista.append(str(random.randint(1,300)))

texto = "banana, laranja, maça, melancia, melao"
texto = texto.replace(",", "" + lista[random.randint(0, len(lista))])
print(texto) '''

# split (divide uma string de acordo com um separador e joga o resultado numa lista)
texto = "banana, laranja, maça, melancia, melao"
frutas = texto.split(',')
print(frutas)