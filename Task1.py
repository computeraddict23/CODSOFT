import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application📝")
        self.root.geometry("500x450")
        self.root.configure(bg="#fef6f6")  # pastel background

        self.setup_styles()
        self.create_widgets()
        self.bind_keys()

    # Setup pastel colors and fonts
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=("Helvetica", 9), padding=6, background="#d0e1f9", foreground="#333")
        style.map("TButton", background=[("active", "#b8d8f9")])
        style.configure("Treeview", font=("Helvetica", 10), rowheight=24)
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#f7d9e3", foreground="#333")

    # Create all GUI widgets
    def create_widgets(self):
        # Header label
        header = ttk.Label(
            self.root, text="To-Do List📝", 
            font=("Helvetica", 16, "bold"), foreground="#856c8b", background="#fef6f6"
        )
        header.pack(pady=10)

        # Input section
        entry_frame = ttk.Frame(self.root)
        entry_frame.pack(fill=tk.X, padx=10)
        self.task_entry = ttk.Entry(entry_frame, font=("Helvetica", 11))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        ttk.Button(entry_frame, text="Add", command=self.add_task).pack(side=tk.RIGHT)

        # Task list section
        self.tree = ttk.Treeview(
            self.root, columns=("status", "task", "added"),
            show="headings", selectmode="browse"
        )
        self.tree.heading("status", text="✓")
        self.tree.heading("task", text="Task")
        self.tree.heading("added", text="Added On")
        self.tree.column("status", width=30, anchor=tk.CENTER)
        self.tree.column("task", width=250)
        self.tree.column("added", width=140)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree.tag_configure("completed", foreground="#999999")

        # Buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        ttk.Button(btn_frame, text="Complete ✓", command=self.toggle_complete).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete 🗑", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear All🧹", command=self.clear_all).pack(side=tk.LEFT, padx=5)

    # Bind Enter key to add task
    def bind_keys(self):
        self.root.bind("<Return>", lambda e: self.add_task())

    # Add a task to the list
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            added_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.tree.insert("", tk.END, values=("○", task, added_time))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Enter a task to add.")

    # Mark a task as complete/incomplete
    def toggle_complete(self):
        sel = self.tree.selection()
        if sel:
            item = self.tree.item(sel[0])
            status = "✓" if item['values'][0] == "○" else "○"
            new_tags = ("completed",) if status == "✓" else ()
            self.tree.item(sel[0], values=(status, item['values'][1], item['values'][2]), tags=new_tags)
        else:
            messagebox.showwarning("No Selection", "Select a task to mark complete.")

    # Delete selected task
    def delete_task(self):
        sel = self.tree.selection()
        if sel:
            task_text = self.tree.item(sel[0])['values'][1]
            if messagebox.askyesno("Delete Task", f"Delete: {task_text}?"):
                self.tree.delete(sel[0])
        else:
            messagebox.showwarning("No Selection", "Select a task to delete.")

    # Clear all tasks from the list
    def clear_all(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            for item in self.tree.get_children():
                self.tree.delete(item)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()