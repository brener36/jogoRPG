import random
import time

# ======================
# PERSONAGEM
# ======================
jogador = {
    "nome": "",
    "classe": "",
    "vida": 100,
    "vida_max": 100,
    "ataque": 10,
    "ouro": 50,
    "inventario": [],
    "vitorias": 0  # ADICIONADO
}

# ======================
# INIMIGOS
# ======================
inimigos = [
    {"nome": "Goblin", "vida": 30, "ataque": 5, "ouro": 20},
    {"nome": "Orc", "vida": 50, "ataque": 8, "ouro": 50},
    {"nome": "Lobisonmen", "vida": 100, "ataque": 20, "ouro": 100},
    {"nome": "Presidente Lula", "vida": 150, "ataque": 9, "ouro": 1000},
]

# ======================
# BOSS
# ======================
boss = {
    "nome": "Lich King",
    "vida": 500,
    "ataque": 85,
    "ouro": 10000
}

# ======================
# VISUAL
# ======================
def barra_vida(atual, maximo):
    tamanho = 20
    proporcao = atual / maximo
    cheio = int(proporcao * tamanho)
    return "█" * cheio + "-" * (tamanho - cheio)

def limpar():
    print("\n" * 3)

# ======================
# CRIAÇÃO DE PERSONAGEM
# ======================
def criar_personagem():
    jogador["nome"] = input("Nome do herói: ")

    print("\nEscolha sua classe:")
    print("1 - Guerreiro (mais vida)")
    print("2 - Mago (mais ataque)")
    print("3 - Arqueiro (equilibrado)")

    escolha = input("Escolha: ")

    if escolha == "1":
        jogador["classe"] = "Guerreiro"
        jogador["vida"] = 120
        jogador["vida_max"] = 120
        jogador["ataque"] = 8

    elif escolha == "2":
        jogador["classe"] = "Mago"
        jogador["vida"] = 80
        jogador["vida_max"] = 80
        jogador["ataque"] = 15

    else:
        jogador["classe"] = "Arqueiro"
        jogador["vida"] = 100
        jogador["vida_max"] = 100
        jogador["ataque"] = 10

    print(f"\n🧙 {jogador['nome']} o {jogador['classe']} entrou na aventura!")
    time.sleep(1)

# ======================
# STATUS
# ======================
def mostrar_status():
    print("\n=== STATUS ===")
    print(f"Nome: {jogador['nome']} ({jogador['classe']})")
    print(f"Vida: [{barra_vida(jogador['vida'], jogador['vida_max'])}] {jogador['vida']}")
    print(f"Ataque: {jogador['ataque']}")
    print(f"Ouro: {jogador['ouro']}")
    print(f"Vitórias: {jogador['vitorias']}")
    print("Inventário:", jogador["inventario"])
    input("\nENTER para continuar")

# ======================
# USAR ITEM EM COMBATE
# ======================
def usar_item_combate(inimigo):
    if not jogador["inventario"]:
        print("\n❌ Inventário vazio!")
        time.sleep(1)
        return False

    print("\n🎒 Inventário:")
    for i, item in enumerate(jogador["inventario"]):
        print(f"{i+1} - {item}")

    try:
        escolha = int(input("Escolha item: ")) - 1
    except:
        return False

    if escolha < 0 or escolha >= len(jogador["inventario"]):
        print("Escolha inválida!")
        return False

    item = jogador["inventario"][escolha]

    if item == "poção":
        jogador["vida"] += 30
        if jogador["vida"] > jogador["vida_max"]:
            jogador["vida"] = jogador["vida_max"]
        print("\n🧪 Você se curou!")

    elif item == "bomba":
        inimigo["vida"] -= 20
        print("\n💣 Bomba causou 20 de dano!")

    jogador["inventario"].remove(item)
    time.sleep(1)
    return True

# ======================
# COMBATE NORMAL
# ======================
def batalha():
    inimigo = random.choice(inimigos).copy()
    vida_max_inimigo = inimigo["vida"]

    print(f"\n⚔️ Um {inimigo['nome']} apareceu!")
    time.sleep(1)

    while inimigo["vida"] > 0 and jogador["vida"] > 0:
        limpar()

        print("="*30)
        print(f"🧙 {jogador['nome']}")
        print(f"[{barra_vida(jogador['vida'], jogador['vida_max'])}] {jogador['vida']}")

        print(f"\n👹 {inimigo['nome']}")
        print(f"[{barra_vida(inimigo['vida'], vida_max_inimigo)}] {inimigo['vida']}")
        print("="*30)

        print("\n1 - Atacar")
        print("2 - Usar item")
        print("3 - Fugir")

        escolha = input("Escolha: ")

        # TURNO DO JOGADOR
        if escolha == "1":
            print("\n⚔️ Você atacou!")
            inimigo["vida"] -= jogador["ataque"]
            print(f"💥 Dano causado: {jogador['ataque']}")
            time.sleep(1)

        elif escolha == "2":
            usou = usar_item_combate(inimigo)
            if not usou:
                continue

        elif escolha == "3":
            print("\n🏃 Você fugiu!")
            time.sleep(1)
            return False

        # SE INIMIGO MORREU
        if inimigo["vida"] <= 0:
            break

        # TURNO DO INIMIGO
        print("\n👹 O inimigo atacou!")
        jogador["vida"] -= inimigo["ataque"]
        print(f"⚠️ Você recebeu {inimigo['ataque']} de dano!")
        time.sleep(1)

    # RESULTADO
    if jogador["vida"] > 0:
        ganho = inimigo["ouro"]
        jogador["ouro"] += ganho
        jogador["vitorias"] += 1
        print(f"\n🏆 Vitória!")
        print(f"💰 Você ganhou {ganho} de ouro!")
    else:
        print("\n💀 Você morreu...")
        exit()

    time.sleep(2)
# ======================
# BATALHA BOSS
# ======================
def batalha_boss():
    inimigo = boss.copy()
    vida_max = inimigo["vida"]

    print(f"\n👑 O {inimigo['nome']} apareceu!")
    time.sleep(1)

    while inimigo["vida"] > 0 and jogador["vida"] > 0:
        limpar()

        print("="*30)
        print(f"🧙 {jogador['nome']}")
        print(f"[{barra_vida(jogador['vida'], jogador['vida_max'])}] {jogador['vida']}")

        print(f"\n👑 {inimigo['nome']}")
        print(f"[{barra_vida(inimigo['vida'], vida_max)}] {inimigo['vida']}")
        print("="*30)

        print("\n1 - Atacar")
        print("2 - Usar item")

        op = input("Escolha: ")

        # TURNO DO JOGADOR
        if op == "1":
            print("\n⚔️ Você atacou!")
            inimigo["vida"] -= jogador["ataque"]
            print(f"💥 Dano causado: {jogador['ataque']}")
            time.sleep(1)

        elif op == "2":
            usou = usar_item_combate(inimigo)
            if not usou:
                continue

        # SE BOSS MORREU
        if inimigo["vida"] <= 0:
            break

        # TURNO DO BOSS
        print("\n👑 O boss atacou!")
        jogador["vida"] -= inimigo["ataque"]
        print(f"⚠️ Você recebeu {inimigo['ataque']} de dano!")
        time.sleep(1)

    # RESULTADO CORRETO
    if jogador["vida"] > 0:
        print("\n🏆 Você derrotou o Lich King!")
        print("🎉 ZEROU O JOGO!")
    else:
        print("\n💀 Você morreu para o boss...")

    exit()
# ======================
# LOJA
# ======================
def loja():
    while True:
        limpar()
        print("\n🛒 LOJA")
        print(f"💰 Ouro: {jogador['ouro']}")
        print("1 - Poção (20)")
        print("2 - Bomba (25)")

        print("\n=== Equipamentos ===")

        if jogador["classe"] == "Guerreiro":
            print("4 - Machado (+5 atk) (50)")
            print("5 - Armadura (+20 vida) (50)")
        elif jogador["classe"] == "Mago":
            print("4 - Cajado (+5 atk) (50)")
            print("5 - Amuleto (+20 vida) (50)")
        else:
            print("4 - Flechas (+5 atk) (50)")
            print("5 - Armadura couro (+20 vida) (50)")

        print("3 - Sair")

        op = input()

        if op == "1" and jogador["ouro"] >= 20:
            jogador["ouro"] -= 20
            jogador["inventario"].append("poção")

        elif op == "2" and jogador["ouro"] >= 25:
            jogador["ouro"] -= 25
            jogador["inventario"].append("bomba")

        elif op == "4" and jogador["ouro"] >= 50:
            jogador["ouro"] -= 50
            jogador["ataque"] += 5

        elif op == "5" and jogador["ouro"] >= 50:
            jogador["ouro"] -= 50
            jogador["vida_max"] += 20
            jogador["vida"] += 20

        elif op == "3":
            break

        time.sleep(1)

# ======================
# LOOP PRINCIPAL
# ======================
criar_personagem()

while True:
    limpar()
    print("\n=== MENU ===")
    print("1 - Batalhar")
    print("2 - Loja")
    print("3 - Status")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        if jogador["vitorias"] >= 3:
            batalha_boss()
        else:
            batalha()

    elif op == "2":
        loja()

    elif op == "3":
        mostrar_status()

    elif op == "4":
        break