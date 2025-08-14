import tkinter as tk
from tkinter import messagebox
import random

# --------- Initialisation de la fenêtre ---------
root = tk.Tk()
root.title("Tic-Tac-Toe Emotion - Dark Theme")
root.geometry("675x600")
root.configure(bg="#1e1e1e")  # fond sombre

current_player = "❌"  # Emoji X
board = [""] * 9
buttons = []
mode_bot = False  # False = Ami, True = Bot
thinking_label = None

# --------- Vérification du gagnant ---------
def check_winner():
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] != "":
            # Mettre en vert les cases gagnantes
            for idx in (a, b, c):
                buttons[idx]["bg"] = "#2ecc71"  # vert
                buttons[idx]["fg"] = "#ffffff"  # texte blanc

            msg = f"{board[a]} triomphe ! 🎉" if board[a]=="❌" else f"{board[a]} sourit timidement 😅"
            root.after(800, lambda: (messagebox.showinfo("Tic-Tac-Toe Emotion", msg), reset_board()))
            return True

    if "" not in board:
        root.after(800, lambda: (messagebox.showinfo("Tic-Tac-Toe Emotion", "Égalité… suspens intense 😮"), reset_board()))
        return True
    return False

# --------- Clic utilisateur ---------
def on_click(i):
    global current_player
    if board[i] == "":
        board[i] = current_player
        buttons[i]["text"] = current_player
        buttons[i]["fg"] = "#ff4c4c" if current_player=="❌" else "#4ccfff"
        buttons[i]["bg"] = "#2e2e2e"

        if not check_winner():
            current_player = "⭕" if current_player=="❌" else "❌"
            if mode_bot and current_player == "⭕":
                show_thinking()
                root.after(1000, bot_move)  # délai de 1s avant que le bot joue

# --------- Afficher "Thinking..." pour faire za3ma---------
def show_thinking():
    global thinking_label
    thinking_label = tk.Label(root, text="🤖 Thinking...", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="#ffaa00")
    thinking_label.grid(row=4, column=0, columnspan=3, pady=5)

def hide_thinking():
    global thinking_label
    if thinking_label:
        thinking_label.destroy()
        thinking_label = None

# --------- Tour du bot ---------
def bot_move():
    global current_player
    empty_indices = [i for i, val in enumerate(board) if val == ""]
    if empty_indices:
        choice = random.choice(empty_indices)
        on_click(choice)
    hide_thinking()

# --------- Réinitialiser ---------
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "❌"
    for btn in buttons:
        btn["text"] = ""
        btn["bg"] = "#2e2e2e"
        btn["fg"] = "#ffffff"

# --------- Fenêtre choix mode ---------
def ask_mode_start():
    win = tk.Toplevel(root)
    win.title("Choisir mode")
    win.geometry("300x150")
    win.configure(bg="#1e1e1e")
    win.grab_set()

    lbl = tk.Label(win, text="Voulez-vous jouer contre :", font=("Helvetica", 14, "bold"), bg="#1e1e1e", fg="#ffffff")
    lbl.pack(pady=10)

    def choose_ami():
        global mode_bot
        mode_bot = False
        win.destroy()

    def choose_bot():
        global mode_bot
        mode_bot = True
        win.destroy()

    tk.Button(win, text="Ami", font=("Helvetica", 14, "bold"),
              bg="#4ccfff", fg="#000000", width=8, command=choose_ami).pack(side="left", expand=True, padx=10)
    tk.Button(win, text="Bot", font=("Helvetica", 14, "bold"),
              bg="#ffaa00", fg="#000000", width=8, command=choose_bot).pack(side="right", expand=True, padx=10)

# --------- Construire interface ---------
def build_gui():
    for i in range(9):
        btn = tk.Button(root, text="", font=("Helvetica", 48, "bold"), width=5, height=2,
                        bg="#2e2e2e", fg="#ffffff",
                        activebackground="#3e3e3e",
                        activeforeground="#ffffff",
                        command=lambda i=i: on_click(i))
        btn.grid(row=i//3, column=i%3, padx=8, pady=8)
        buttons.append(btn)

    # Bouton Reset manuel
    reset_btn = tk.Button(root, text="Reset", font=("Helvetica", 16, "bold"),
                          bg="#3e3e3e", fg="#ffffff",
                          activebackground="#5e5e5e", activeforeground="#ffffff",
                          command=reset_board)
    reset_btn.grid(row=3, column=0, columnspan=3, sticky="we", padx=8, pady=12)

# Lancement
build_gui()
root.after(100, ask_mode_start)  # afficher la boîte ta3 bot wla ami au début
root.mainloop()
