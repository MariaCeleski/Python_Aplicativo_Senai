# 2 - Faça um programa que leia 4 valores, calcule a média e imprima positivo ou negativo
# (para ser positivo a média deve ser acima de 1).

valores = []

for c in range(1, 5):
        valores.append(int(input(f'Digite um valor até 10 para cada posição = {c}:')))

soma_valores = sum(valores)

media_valores = soma_valores / 4
print('_'*50)
print(f'A média das notas é: {media_valores}')

if media_valores >=7:
    print('Essa média é positiva = Aprovado')
else:
    print('Média negativa = Reprovado')