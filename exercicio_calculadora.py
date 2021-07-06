#Exercício da SA3
#Algoritimo de uma calculadora para calcular troco em python.

print('=' * 30)
print('{:^30}'.format('CALCULE O TROCO'))
print('=' * 30) #printa linhas
print('=' * 60)
print('{:^30}'.format('DIGITE O VALOR DAS SUAS COMPRAS E APÓS, O VALOR EM DINHEIRO'))
print('=' * 60)

# use pontos para casas decimais
compras = float(input('Qual foi o valor das compras?'))
dinheiro = float(input('Qual o valor em dinheiro?'))
print('=' * 50)
valor = round((dinheiro - compras), 2) #limita duas casa após a vírgula quando necessário
print(f'Seu troco é de R$ {valor} em notas de:') #identação com variavel dentro de {chaves}
total = valor
print('=' * 100)
notas = 100
totalnotas = 0
while True:
    if total >= notas:
        total -= notas
        totalnotas += 1
    else:
        if compras == dinheiro:
            print("NÃO TEM TROCO")
        if totalnotas > 0:
            print(f'{totalnotas} cédulas de R${notas}') #para mostrar somente quando houver as determinadas notas
        if notas == 100:
            notas = 50
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 5
        elif notas == 5:
            notas = 2
        elif notas == 2:
            notas = 1
        elif notas == 1:
            notas = 0.5
        elif notas == 0.5:
            notas = 0.05
        elif notas == 0.05:
            notas = 0.01
        elif notas == 0.01:
            notas = 1
        totalnotas = 0
        if total == 0:
            break  #encerra o loop






