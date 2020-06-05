import random

def main():
    numero_dados = int(input("digite a quantidade de dados"))
    numero_de_lados = int(input("digite a quantidade de dados"))
    soma_das_jogadas = 0 
    for i in range(0,numero_dados):
        roll = random.randint(1,numero_de_lados)
        soma_das_jogadas += roll
        if roll == 1:
            print(f"sua jogada foi: {roll} Falha critica")
        elif roll == 6:
            print(f"sua jogada foi: {roll} Acerto Critico")
        else:
            print(f"sua jogada foi: {roll}")    
        
    print(f"o total das jogadas foi: {soma_das_jogadas}")
    

if __name__== "__main__":
  main()
