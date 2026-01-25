import tkinter as tk
from tkinter import messagebox
import random

# --- LOGICA DEL GIOCO (Dal codice del tuo amico) ---ss
personaggio = {"nome": "Eroe", "livello": 1, "hp": 100, "attacco": 10}
inventario = []
lista_mostri = [
    {"nome": "Goblin", "hp": 30, "attacco": 5},
    {"nome": "Orco", "hp": 50, "attacco": 10},
    {"nome": "Drago", "hp": 100, "attacco": 20},
    {"nome": "Scemo", "hp": 1, "attacco": 0},
    {"nome": "Windows Updete", "hp": 250, "attacco": 2},
    {"nome": "doc", "hp": 0, "attacco": 2},
]
oggetti_possibili = [{"nome": "Pozione"}, {"nome": "Spada Arrugginita"}, {"nome": "Scudo"}, {"nome": "PC"}, {"nome": "Orologio"}, ]

# --- FUNZIONI DELL'INTERFACCIA ---
def aggiorna_stato():
    lbl_stats.config(text=f"HP: {personaggio['hp']} | Livello: {personaggio['livello']} | Attacco: {personaggio['attacco']}")
    lbl_inv.config(text=f"Oggetti nello zaino: {len(inventario)}")

def esplora():
    oggetto = random.choice(oggetti_possibili)
    inventario.append(oggetto)
    txt_log.insert(tk.END, f"-> Hai trovato: {oggetto['nome']}\n")
    txt_log.see(tk.END)
    aggiorna_stato()

def combatti():
    mostro = random.choice(lista_mostri).copy()
    txt_log.insert(tk.END, f"\n⚠️ Un {mostro['nome']} appare!\n")
    
    # Combattimento veloce
    mostro['hp'] -= personaggio['attacco']
    personaggio['hp'] -= mostro['attacco']
    
    if personaggio['hp'] <= 0:
        messagebox.showerror("Game Over", "Sei morto!")
        root.destroy()
    elif mostro['hp'] <= 0:
        personaggio['livello'] += 1
        txt_log.insert(tk.END, f"✅ Hai sconfitto il {mostro['nome']}! +1 Livello\n")
    else:
        txt_log.insert(tk.END, f"⚔️ Scambio di colpi! Ti restano {personaggio['hp']} HP\n")
    
    txt_log.see(tk.END)
    aggiorna_stato()

# --- CREAZIONE FINESTRA ---
root = tk.Tk()
root.title("RPG Graphical Edition - Saffdds & diegozampini ")
root.geometry("400x500")

# Header con statistiche
lbl_stats = tk.Label(root, text="", font=("Arial", 10, "bold"))
lbl_stats.pack(pady=10)

lbl_inv = tk.Label(root, text="")
lbl_inv.pack()

# Area di testo (Log degli eventi)
txt_log = tk.Text(root, height=15, width=45)
txt_log.pack(pady=10)

# Pulsanti di azione
btn_esplora = tk.Button(root, text="🔍 Esplora", width=20, command=esplora, bg="#e1f5fe")
btn_esplora.pack(pady=5)

btn_combatti = tk.Button(root, text="⚔️ Combatti", width=20, command=combatti, bg="#ffebee")
btn_combatti.pack(pady=5)

btn_esci = tk.Button(root, text="🚪 Esci", width=20, command=root.destroy)
btn_esci.pack(pady=5)

# Inizio gioco
aggiorna_stato()
txt_log.insert(tk.END, "Benvenuto nell'avventura grafica!\n")
root.mainloop()
