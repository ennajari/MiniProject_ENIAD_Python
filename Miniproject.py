#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import winsound

historique = []

def demarrer_minuteur(nb_cycles, secondes_exercice, secondes_repos, cycle=0):
    if cycle < nb_cycles:
        # Exercice
        etiquette_minuteur.config(text="Exercice", fg="blue")
        root.update()
        winsound.Beep(3500, 1000)
        for exercice in range(secondes_exercice, 0, -1):
            etiquette_minuteur.config(text="Exercice: {}s".format(exercice), fg="green")
            root.update()
            root.after(1000)
        winsound.Beep(3500, 500)

        historique.append(("Cycle {}".format(cycle + 1), secondes_exercice))

        # Repos
        if cycle < nb_cycles - 1:
            etiquette_minuteur.config(text="Repos", fg="red")
            root.update()
            winsound.Beep(3500, 1000)
            for repos in range(secondes_repos, 0, -1):
                etiquette_minuteur.config(text="Repos: {}s".format(repos), fg="red")
                root.update()
                root.after(1000)
            winsound.Beep(3500, 500)

            historique.append(("Repos", secondes_repos))

        # Prochain cycle
        demarrer_minuteur(nb_cycles, secondes_exercice, secondes_repos, cycle + 1)
    else:
        etiquette_minuteur.config(text="Minuteur terminé !", fg="purple")
        afficher_historique()

def afficher_historique():
    for i, (cycle, duree) in enumerate(historique):
        tree.insert("", "end", values=(cycle, duree))

def start_timer():
    try:
        nb_cycles = int(saisie_cycles.get())
        secondes_exercice = int(saisie_exercice.get())
        secondes_repos = int(saisie_repos.get())

        # Vérification des valeurs saisies
        if nb_cycles <= 0 or secondes_exercice <= 0 or secondes_repos <= 0:
            raise ValueError("Les valeurs doivent être positives et supérieures à zéro.")

        demarrer_minuteur(nb_cycles, secondes_exercice, secondes_repos)

    except ValueError as e:
        etiquette_minuteur.config(text=str(e), fg="red")

root = tk.Tk()
root.title("Minuteur d'Intervalles")
root.geometry("900x700")
root.configure(bg='black')

etiquette_titre = tk.Label(root, text="Minuteur d'Intervalles", font=("Helvetica", 24), fg="white", bg="black")
etiquette_titre.pack()

etiquette_instruction = tk.Label(root, text="Entrez les paramètres du minuteur:", font=("Helvetica", 20), fg="white", bg="black")
etiquette_instruction.pack()

etiquette_cycles = tk.Label(root, text="Nombre de cycles:", font=("Helvetica", 16), fg="white", bg="black")
etiquette_cycles.pack()
saisie_cycles = ttk.Entry(root, font=("Helvetica", 14))
saisie_cycles.pack(ipady=5, pady=5)

etiquette_exercice = tk.Label(root, text="Durée de l'exercice (en secondes):", font=("Helvetica", 16), fg="white", bg="black")
etiquette_exercice.pack()
saisie_exercice = ttk.Entry(root, font=("Helvetica", 14))
saisie_exercice.pack(ipady=5, pady=5)

etiquette_repos = tk.Label(root, text="Durée du repos (en secondes):", font=("Helvetica", 16), fg="white", bg="black")
etiquette_repos.pack()
saisie_repos = ttk.Entry(root, font=("Helvetica", 14))
saisie_repos.pack(ipady=5, pady=5)

espace = tk.Label(root, text="", bg="black")
espace.pack()

bouton_demarrer = tk.Button(root, text="Démarrer le Minuteur", command=start_timer, fg="white", bg="blue", font=("Helvetica", 16))
bouton_demarrer.pack()

etiquette_minuteur = tk.Label(root, text="", font=("Helvetica", 16), fg="white", bg="black")
etiquette_minuteur.pack()

tree = ttk.Treeview(root, columns=("Cycle", "Durée"), show="headings")
tree.heading("Cycle", text="Cycle", anchor=tk.CENTER)
tree.heading("Durée", text="Durée (s)", anchor=tk.CENTER)
tree.pack(pady=20)

root.mainloop()
