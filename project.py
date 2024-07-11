import tkinter as tk
from tkinter import simpledialog, messagebox
import time

class NQueensVisualizer:
    def __init__(self, n):
        self.n = n
        self.iterations = 0
        self.solutions = 0
        self.col = set()
        self.posdiag = set()
        self.negdiag = set()
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.res = []
        self.start_time = None

        self.root = tk.Tk()
        self.root.title("N-Queens Visualizer")

        self.canvas = tk.Canvas(self.root, width=n*40, height=n*40)
        self.canvas.pack()

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.status_label.pack()

        self.root.after(1000, self.start_backtracking)
        self.root.mainloop()

    def start_backtracking(self):
        self.start_time = time.time()
        self.print_board()
        self.backtrack(0)
        self.display_summary()

    def print_board(self):
        self.canvas.delete("all")
        for r in range(self.n):
            for c in range(self.n):
                color = "white" if self.board[r][c] == '.' else "black"
                self.canvas.create_rectangle(c*40, r*40, (c+1)*40, (r+1)*40, fill=color)
                if color == "black":
                    self.canvas.create_text(c*40 + 20, r*40 + 20, text='Q', fill='red')
        self.canvas.update()
        time.sleep(0.0001)

    def backtrack(self, r):
        if r == self.n:
            self.res.append(["".join(row) for row in self.board])
            self.solutions += 1
            return

        for c in range(self.n):
            if c in self.col or (r + c) in self.posdiag or (r - c) in self.negdiag:
                continue

            self.iterations += 1
            self.col.add(c)
            self.posdiag.add(r + c)
            self.negdiag.add(r - c)
            self.board[r][c] = 'Q'
            self.print_board()
            self.backtrack(r + 1)
            self.col.remove(c)
            self.posdiag.remove(r + c)
            self.negdiag.remove(r - c)
            self.board[r][c] = '.'
            self.print_board()

    def display_summary(self):
        end_time = time.time()
        time_taken = end_time - self.start_time

        summary_text = f"Solutions: {self.solutions}\nIterations: {self.iterations}\n"
        summary_text += f"Time taken: {time_taken:.2f} seconds\n\n"
        summary_text += "Solutions:\n"
        for solution in self.res:
            for row in solution:
                summary_text += row + "\n"
            summary_text += "\n"

        self.status_label.config(text=f"Solutions: {self.solutions}\nIterations: {self.iterations}\nTime taken: {time_taken:.2f} seconds")
        self.canvas.update()

        result_window = tk.Toplevel(self.root)
        result_window.title("N-Queens Solutions")

        text_box = tk.Text(result_window, wrap="word")
        text_box.insert("1.0", summary_text)
        text_box.pack(expand=True, fill='both')

        # Display the last solution on the grid
        self.board = [list(row) for row in self.res[-1]]
        self.print_board()

def main():
    root = tk.Tk()
    root.withdraw()
    n = simpledialog.askinteger("Input", "Enter the number of queens:")
    root.destroy()
    if n:
        NQueensVisualizer(n)

if __name__ == "__main__":
    main()
