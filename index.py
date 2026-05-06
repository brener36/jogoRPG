import random
import time


jogador = {
    "nome": "",
    "classe": "",
    "vida": 100,
    "vida_max": 100,
    "ataque": 10,
    "ouro": 50,
    "inventario": [],
    "vitorias": 0    
}

|#inimigos

inimigos = [
    {"nome": "zumbi", "vida": 50, "ataque": 5, "ouro": 20},
    {"nome": "vamp", "vida": 60, "ataque": 10, "ouro": 350},
    {"nome": "lobo", "vida": 10, "ataque": 3, "ouro": 150},
]

#boss

boss = {
    "nome": "the king",
    "vida": 500,
    "ataque": 50,
    "ouro": 100000
}

#visual

def barra_vida(atual, maxima):
    tamanho = 20
    proporcao = atual / maxima
    cheio = int(proporcao * tamanho)
    return "█" * cheio + "-" * (tamanho - cheio)

def limpar():
    print("\n" * 3)
    
#criacao do personagem

def criar_personagem():
    jogador["nome"] = input("nome do heroi: ")
   
    print("\nescolha uma classe: ")
    print("1 - guerreiro (mais vida)")
    print("2 - mago (mais dano)")
    print("3 - arqueiro (mais trouxa)")
    
    escolha = input("escolha: ")
    
    if escolha = "1":
        jogador["classe"] = "guerreiro"
        jogador["vida"] = 120
        jogador["vida_max"] = 120
        jogador["ataque"] = 10
    
    elif escolha == "2":
        jogador["classe"] = "mago"
        jogador["vida"] = 100
        jogador["vida_max"] = 100
        jogador["ataque"] = 30
    else:
        jogador["classe"] = "arqueiro"
        jogador["vida"] = 100
        jogador["vida_max"] = 100
        jogador["ataque"] = 10