import random

def main():
    numero_dados = 2
    soma_das_jogadas = 0 
    for i in range(0,numero_dados):
        roll = random.randint(1,6)
        soma_das_jogadas += roll
        print(f"sua jogada foi: {roll}")
    print(f"o total das jogadas foi: {soma_das_jogadas}")
    

if __name__== "__main__":
  main()
