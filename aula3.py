resposta = ""
sair = False

while not sair:
    resposta = input("Digite sair para encerrar o loop: " )
    sair = resposta == "sair"
    if not sair:
        print("Você digitou:", resposta)