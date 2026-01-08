# Utilizza il modulo random per scegliere oggetti casuali durante l'esplorazione (usando random.choice()) e per generare HP casuali dei mostri (usando random.randint(50, 100)).
# Inizia con il personaggio e inventario come sopra.
# Mostra un menu con opzioni numerate (usando un ciclo while per ripetere fino a scelta di uscita):
# 1: Esplora (aggiungi un oggetto casuale all'inventario da oggetti_possibili).
# 2: Combatti (scegli un oggetto dall'inventario per combattere un mostro casuale; se vinci, sali di livello; se perdi HP, potresti morire).
# 3: Inventario (visualizza tutti gli oggetti con nome, tipo, valore, usato).
# 4: Statistiche (mostra statistiche del personaggio e inventario: totale oggetti).
# 5: Esci.
# Gestisci input invalidi con messaggi di errore.
# Usa cicli for per iterare su liste e dizionari, ciclo while per il menu principale con continue per saltare iterazioni e break per uscire, condizioni if/elif/else per il menu e la logica, e metodi stringa se necessario.
# Esempio
# Menu:


# Esplora
# Combatti
# Inventario
# Statistiche
# Esci
# Scelta: 1
# Hai trovato: Spada (arma, valore: 20)


# Scelta: 3
# Inventario:


# Nome: Spada, Tipo: arma, Valore: 20, Usato: False
# Scelta: 4
# Nome: Eroe, Livello: 1, HP: 100, Attacco: 10
# Totale oggetti: 1


# Questo esercizio integra input/output per interazione, condizioni per validazione e menu, cicli per menu e iterazioni, liste per inventario, dizionari per personaggio e oggetti, stringhe per output, e il modulo random per casualità.


import random
import os


eroe = {"nome": "Eroe", "livello": 1, "hp": 100, "attacco": 15}
mago = {"nome": "Mago", "livello": 1, "hp": 90, "attacco": 20}
principessa = {"nome": "Principessa", "livello": 1, "hp": 30, "attacco": 50}
print("Benvenuto in questo viaggio epico!")
input("Premi Invio per cominciare...")
os.system("cls" if os.name == "nt" else "clear")

print("Il viaggio è cominciato!")
scelta = input("Che personaggio scegli? Eroe, Mago o Principessa: ").lower()
os.system("cls" if os.name == "nt" else "clear")
while True:
    if scelta in ["eroe", "mago", "principessa"]:
        print("Perfetto! Hai scelto il personaggio:", scelta.capitalize())
        break
    else:
        print("Scelta non valida. Scegli tra Eroe, Mago o Principessa.")
        scelta = input("Che personaggio scegli? Eroe, Mago o Principessa: ").lower()
        os.system("cls" if os.name == "nt" else "clear")

if scelta == "eroe":
    personaggio = eroe
    oggetti_possibili = [
        {"nome": "Spada", "tipo": "attacco", "valore": 20},
        {"nome": "Medicazione", "tipo": "hp", "valore": 30},
        {"nome": "Gatito Blade", "tipo": "attacco", "valore": 15},
        {"nome": "Scudo", "tipo": "hp", "valore": 10},
    ]
elif scelta == "mago":
    personaggio = mago
    oggetti_possibili = [
        {"nome": "Bacchetta", "tipo": "attacco", "valore": 20},
        {"nome": "Pozione", "tipo": "hp", "valore": 30},
        {"nome": "Arco", "tipo": "attacco", "valore": 15},
        {"nome": "Anello", "tipo": "hp", "valore": 25},
    ]
else:
    personaggio = principessa
    oggetti_possibili = [
        {"nome": "Arco triplo", "tipo": "attacco", "valore": 60},
        {"nome": "Collana", "tipo": "hp", "valore": 30},
        {"nome": "Specchio", "tipo": "hp", "valore": 15},
        {"nome": "Arco infuocato", "tipo": "attacco", "valore": 70},
    ]

inventario = []


lista_mostri = [
    {"nome": "Goblin", "hp": 50, "attacco": 10},
    {"nome": "Golem", "hp": 90, "attacco": 15},
    {"nome": "Orco", "hp": 80, "attacco": 12},
    {"nome": "Troll", "hp": 100, "attacco": 20},
]


while True:
    print("1) Trova oggetto")
    print("2) Combatti")
    print("3) Inventario")
    print("4) Stato personaggio")
    print("5) Esci")

    azione = int(input("Scegli un'azione (1-5): "))
    os.system("cls" if os.name == "nt" else "clear")

    if azione == 1:
        oggetto = random.choice(oggetti_possibili)
        inventario.append(oggetto)
        print(f"Bene! Hai trovato: {oggetto['nome']}")
        print(f"Il tuo inventario ora contiene: {len(inventario)} oggetti.")
        input("Se desideri continuare, premi Invio...")
        os.system("cls" if os.name == "nt" else "clear")

    
    elif azione == 2:
        mostro = random.choice(lista_mostri).copy()
        print(f"\nUn {mostro['nome']} appare!")

        while personaggio["hp"] > 0 and mostro["hp"] > 0:
            mostro["hp"] -= personaggio["attacco"]
            print(f"Colpisci il {mostro['nome']} (-{personaggio['attacco']} HP)")

            if mostro["hp"] <= 0:
                print(f"Hai sconfitto il {mostro['nome']}!")
                personaggio["livello"] += 1
                break

            personaggio["hp"] -= mostro["attacco"]
            print(f"Il {mostro['nome']} ti colpisce (-{mostro['attacco']} HP)")

            if personaggio["hp"] <= 0:
                print("Sei morto! Game Over.")
                exit()
        print("Bene! Il combattimento è finito.")
        input("Se desideri continuare, premi Invio...")
        os.system("cls" if os.name == "nt" else "clear")
    
    elif azione == 3:
        print (f"L'inventario contiene: {len(inventario)} oggetti")
        print (f"{inventario}")
        print("Questo è il tuo inventario:")
        input("Se desideri continuare, premi Invio...")
        os.system("cls" if os.name == "nt" else "clear")

    elif azione == 4:
        print(f"\nNome: {personaggio['nome']}")
        print(f"Livello: {personaggio['livello']}")
        print(f"HP: {personaggio['hp']}")
        print(f"Attacco: {personaggio['attacco']}")
        soddisfatto = input("Sei soddisfatto del tuo stato attuale?: (Si/No) ")
        if soddisfatto.lower() == "si":
            print("Ottimo! Continua così!")
            input("Se desideri continuare, premi Invio...")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("Non preoccuparti, migliorerai con il tempo!")
            input("Se desideri continuare, premi Invio...")
            os.system("cls" if os.name == "nt" else "clear")
    
    elif azione == 5:
        conferma = input("Sei sicuro di voler uscire? (Si/No): ").lower()

        if conferma == "si":
            print("Bene! Spero che ti sei divertito.")
            input("Premi Invio per uscire...")
            os.system("cls" if os.name == "nt" else "clear")
            print("Arrivederci! 👋")
            break

        elif conferma == "no":
            print("Perfetto! Il tuo viaggio continua....")
            input("Premi Invio per continuare...")
            os.system("cls" if os.name == "nt" else "clear")

        else:
            print("Risposta non valida. Scrivi Si o No.")

