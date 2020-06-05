import random

def main():
    numero_de_jogadores=int(input("Digite o numero de jogadores: "))
    numero_dados = int(input("digite a quantidade de dados"))
    numero_de_lados = int(input("digite a quantidade de lados"))
    soma_das_jogadas = 0
    jogadas=dict()

    for i in range(0,numero_de_jogadores):

        nome_do_usuario=str(input(f"digite o nome do jogador {i+1}: "))
        if nome_do_usuario not in jogadas:
            jogadas[nome_do_usuario]=0
        for j in range(0,numero_dados):

            roll = random.randint(1,numero_de_lados)
            soma_das_jogadas += roll    

            if roll == 1:
                print(f"sua jogada {j+1} foi: {roll} Falha critica")
            elif roll == numero_de_lados:
                print(f"sua jogada {j+1} foi: {roll} Acerto Critico")
            else:
                print(f"sua jogada {j+1} foi: {roll}")

        jogadas[nome_do_usuario]=jogadas[nome_do_usuario]+soma_das_jogadas            
        print(f"o total das jogadas foi: {jogadas[nome_do_usuario]}")







if __name__== "__main__":
  main()
