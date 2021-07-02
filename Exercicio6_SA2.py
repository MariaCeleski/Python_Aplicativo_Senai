#6 - Crie um programa que converta horas em segundos, conforme o valor que o usuário informar quando solicitado a ele.

horaSegundos = 3600
valor = input("Digite as horas para conversão: ")
calculo = int(valor) * horaSegundos
print(valor, "horas equivalem à ", round(calculo, 2), "segundos")
