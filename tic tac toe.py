import tkinter as tk
from tkinter import messagebox

# --------- Initialisation de la fenêtre ---------
root = tk.Tk()
root.title("Tic-Tac-Toe By Rayan - Dark Theme")
root.geometry("675x550")
root.configure(bg="#1e1e1e")  # fond sombre

current_player = "❌"  # Emoji X
board = [""] * 9
buttons = []

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

# --------- Gestion du clic ---------
def on_click(i):
    global current_player
    if board[i] == "":
        board[i] = current_player
        buttons[i]["text"] = current_player
        buttons[i]["fg"] = "#ff4c4c" if current_player=="❌" else "#4ccfff"
        buttons[i]["bg"] = "#2e2e2e"  # léger contraste sur fond sombre
        if not check_winner():
            current_player = "⭕" if current_player=="❌" else "❌"

# --------- Réinitialisation du plateau ---------
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "❌"
    for btn in buttons:
        btn["text"] = ""
        btn["bg"] = "#2e2e2e"
        btn["fg"] = "#ffffff"

# --------- Création de l'interface ---------
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

build_gui()
root.mainloop()
