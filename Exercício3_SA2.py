
#3 - Escreva um programa que leia 20 valores inteiros e informe a média deles, o maior e o menor valor.
listanum = []
maiorn = 0
menorn = 0
for c in range(0, 20):
        listanum.append(int(input(f'Digite um valor para a Posição {c}:')))
        if c == 0:
            maiorn = menorn = listanum[c]
        else:
            if listanum[c] > maiorn:
                maiorn = listanum[c]
            if listanum[c] < menorn:
                menorn = listanum[c]

media = sum(listanum)/len(listanum)
print('=-' * 55)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi: {maiorn}')
print(f'O menor valor digitado foi: {menorn}')
print('=-' * 55)
print(f'A média dos valores digitados foi: {media}')