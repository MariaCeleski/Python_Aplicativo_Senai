#Resolução exercício 1 da SA2
#1 - Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista; b) maior valor da lista; c) menor valor da lista; d) soma de todos os elementos da lista;
# e) lista em ordem crescente; f) lista em ordem decrescente.


lista = [5, 7, 2, 9, 4, 1, 3]
lista_ordenada = []

#Exercício A
tam = len(lista)
print(f'O tamanho da lista é de: {tam} elementos')

#Exercício B
lista_max = max(lista)
print(f'O maior número da lista é: {lista_max}')

#Exercício C
lista_min = min(5, 7, 2, 9, 4, 1, 3)
print(f'O menor número da lista é: {lista_min}')

#Exercício D
lista_soma = sum(lista)
print(f'A soma dos números da lista é: {lista_soma}')

#Exercício E
for i in range(tam):
     menor = lista[0]
     for j in range(len(lista)):
         if lista[j] < menor:
             menor = lista[j]
             pos_menor = j
     lista_ordenada.append(menor)
     lista.remove(menor)

print(f'A lista em ordem crescente é: {lista_ordenada}')

#Exercício F
lista_dec = [5, 7, 2, 9, 4, 1, 3]
lista_dec.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista_dec}')

