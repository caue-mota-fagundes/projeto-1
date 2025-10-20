salario = float(input("Qual é  seu salário mensal? "))
hora = int(input("Você trabalha quantas horas por mês? "))
valor_hora = salario / hora
print(f"Seu salário mensal é: R${salario:.2f}")
print(f"Você trabalha {hora} horas por mês" )
print(f"Seu salário por hora é: R${valor_hora:.2f} ")
#O .2f fotmata o valor para duas casas decimais(adiciona dois zeros)
