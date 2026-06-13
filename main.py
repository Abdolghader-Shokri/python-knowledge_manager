# main.py
import tkinter as tk
from ui.app import KnowledgeApp

if __name__ == "__main__":
    root = tk.Tk()
    app = KnowledgeApp(root)
    root.mainloop()
