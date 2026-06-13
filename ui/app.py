# ui/app.py
import tkinter as tk
from tkinter import ttk, messagebox
from services import storage_service
from models.note import Note


class KnowledgeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Knowledge Manager Pro")
        self.root.geometry("600x400")

        self.notes = storage_service.load_notes()

        self.setup_ui()
        self.refresh_listbox()

    def setup_ui(self):
        # Layout
        self.left_frame = ttk.Frame(self.root, width=200)
        self.left_frame.pack(side="left", fill="y", padx=5, pady=5)

        self.right_frame = ttk.Frame(self.root)
        self.right_frame.pack(side="right", expand=True, fill="both", padx=5, pady=5)

        # Listbox
        self.listbox = tk.Listbox(self.left_frame)
        self.listbox.pack(fill="both", expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.load_selected_note)

        # Editors
        ttk.Label(self.right_frame, text="Title:").pack(anchor="w")
        self.title_entry = ttk.Entry(self.right_frame)
        self.title_entry.pack(fill="x")

        ttk.Label(self.right_frame, text="Content:").pack(anchor="w")
        self.content_text = tk.Text(self.right_frame, height=10)
        self.content_text.pack(fill="both", expand=True)

        # Buttons
        btn_frame = ttk.Frame(self.right_frame)
        btn_frame.pack(fill="x", pady=5)

        ttk.Button(btn_frame, text="Save", command=self.save_note).pack(side="left")
        ttk.Button(btn_frame, text="New", command=self.clear_fields).pack(side="left")
        ttk.Button(btn_frame, text="Delete", command=self.delete_note).pack(side="left")

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for note in self.notes:
            self.listbox.insert(tk.END, note['title'])

    def load_selected_note(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            note = self.notes[index]
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, note['title'])
            self.content_text.delete("1.0", tk.END)
            self.content_text.insert("1.0", note['content'])

    def save_note(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END).strip()

        if not title:
            messagebox.showwarning("Warning", "Title is required!")
            return

        new_note = Note(title, content)
        self.notes.append(new_note.to_dict())
        storage_service.save_notes(self.notes)
        self.refresh_listbox()
        self.clear_fields()

    def delete_note(self):
        selection = self.listbox.curselection()
        if selection:
            del self.notes[selection[0]]
            storage_service.save_notes(self.notes)
            self.refresh_listbox()
            self.clear_fields()

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
