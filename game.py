import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("450x450")  # Adjusted window size to fit smaller buttons
        self.player_turn = True  # True for Player 1 (X), False for Player 2 (O)
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Arial", 28), width=5, height=2,  # Reduced font size and button dimensions
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=8, pady=8)  # Adjusted padding for better spacing

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            if self.player_turn:
                self.buttons[row][col]["text"] = "X"
            else:
                self.buttons[row][col]["text"] = "O"

            self.board[row][col] = "X" if self.player_turn else "O"
            self.player_turn = not self.player_turn

            if self.check_winner():
                winner = "Player 1 (X)" if not self.player_turn else "Player 2 (O)"
                messagebox.showinfo("Game Over", f"{winner} has won!")
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if None in row:
                return False
        return True

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
