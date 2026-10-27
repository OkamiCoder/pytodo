import sys
import tkinter as tk
#from tkinter import ttk, messagebox, simpledialog
import json
import os
import uuid

DATA_FILE = "tasks.json"

BANNER = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⢶⣲⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⢀⣤⢶⡿⣽⢳⣏⣯⣽⣛⣞⡷⣤⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡭⢉⠛⢽⣳⣻⢞⣻⣼⣳⠾⣝⡾⣽⣹⢯⣛⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣾⢶⣯⡶⣥⣽⣻⣣⣷⢯⡿⣽⣷⣯⢷⣯⢿⡼⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢻⣭⢿⣿⣽⣳⣯⡷⣯⣛⣿⣿⠿⠿⢿⡿⣞⡋⠷⠛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢸⣯⢿⣾⡷⣿⣿⣻⡵⣿⣿⠃⠀⠀⣾⣿⡽⣟⣿⣳⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠈⣿⣿⣿⣿⣽⣿⡇⡏⢰⣶⣤⣿⣿⣿⣽⣾⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣨⣟⣿⣾⡉⠙⠟⠇⠡⠈⡟⣿⣿⣧⡿⣞⣷⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣟⣾⣿⣷⠂⠈⡀⠀⠀⠐⠙⣡⣿⣿⣻⠿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⢾⣿⠋⡿⢿⣦⣟⣿⣢⡴⣿⣿⣿⣵⠿⣛⣙⣦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⢯⠁⢀⢹⣌⢿⣿⣧⣮⣷⣿⣿⡿⡓⠝⠁⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢠⠂⢸⠈⡽⢮⣳⣷⣯⠿⣽⢏⠌⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠷⠃⠀⠁⠂⣿⣏⡠⠔⠋⡢⡀⠤⠀⠀⢄⢠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣷⠤⣠⠔⠃⡞⠀⠀⢰⠿⢶⡶⣤⣄⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠬⠿⠞⣀⠄⠯⣑⠆⡾⡷⢷⡶⣬⡛⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⡕⠔⠈⡡⠈⠉⡸⠵⢇⡾⠛⠫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠀⣳⡠⠎⠁⠀⡰⠀⠀⢰⠁⠀⣦⣑⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⠀⢹⣦⡀⠀⡰⠀⠀⢠⠃⣀⣤⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⡴⣶⣼⠀⠀⢸⣿⣟⡗⠀⠀⣀⣾⡿⣿⣽⡟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡠⠄⠚⢿⢮⣗⠿⣶⢻⠀⠀⣸⣿⡿⠁⠀⣰⣾⣻⡽⣷⢯⡿⣽⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠠⠘⠀⠀⠀⠀⢸⡿⣼⣿⠿⣿⠀⠀⢸⣧⠇⠀⣠⣿⢿⣇⣿⣟⡿⣿⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⠄⠈⠀⠀⠀⠀⠀⠄⠂⠀⠛⠛⢹⡿⣽⠀⠀⣾⠃⣀⣴⢿⣏⡷⣾⣽⣻⢾⡷⣏⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠰⡁⠀⠀⠠⠀⠂⠈⠀⢀⠠⠀⠀⠀⠀⢿⣽⠀⠀⣇⠰⠋⠉⠓⠚⠻⣽⣯⢷⣻⡿⣽⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠑⢄⠀⠀⣀⣀⡤⢤⡤⣤⠶⣲⣾⢻⡉⠀⡀⡔⠃⠀⠀⣀⢀⣀⣀⣈⣻⡾⣽⣿⢃⣀⣠⠀⠀⠀⡶⢿⣿⣿⣿⣷⣤⣄⡀⠀⠀
⠀⠀⠀⠉⠉⠉⠉⠈⠉⠁⠀⠀⠀⠛⠱⠴⡶⠏⢠⠴⠊⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡄⠀⢸⢰⣾⣿⣿⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢎⠀⠀⠀⠀⠀⠀⠐⠀⠈⠀⢀⣀⡄⠤⠠⠔⠒⠻⠁⠒⠚⠊⠛⠛⠻⢿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠀⠠⠤⠐⠓⠂⠉⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀
"""


def show_banner() -> None:
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    print(BANNER)
    print("  Pure Python ToDo List · Notes · Checklists · Local JSON storage")
    print("  " + "-" * 64)
    print("  Tip: double-click a checklist item to toggle its status.")
    print("  " + "-" * 64)
    print()


class TodoApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Pure Python ToDo List with Notes & Checklists")
        self.root.geometry("900x600")

        self.tasks = []
        self.current_task_id = None

        self._setup_ui()
        self._load_tasks()

    def _setup_ui(self) -> None:
        main_pane = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_pane.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        left_frame = ttk.Frame(main_pane, width=350)
        main_pane.add(left_frame, weight=1)

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill=tk.X, pady=(0, 5))

        ttk.Button(btn_frame, text="Add Task", command=self._add_task).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Delete Task", command=self._delete_task).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Toggle Done", command=self._toggle_task_done).pack(side=tk.LEFT, padx=2)

        columns = ("done", "title")
        self.tree = ttk.Treeview(left_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("done", text="✓")
        self.tree.heading("title", text="Task")
        self.tree.column("done", width=30, anchor="center")
        self.tree.column("title", width=250)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self._on_task_select)

        right_frame = ttk.Frame(main_pane)
        main_pane.add(right_frame, weight=3)

        title_frame = ttk.Frame(right_frame)
        title_frame.pack(fill=tk.X, pady=(0, 5))
        ttk.Label(title_frame, text="Title:").pack(side=tk.LEFT)
        self.title_var = tk.StringVar()
        self.title_entry = ttk.Entry(title_frame, textvariable=self.title_var)
        self.title_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Button(title_frame, text="Update Title", command=self._update_title).pack(side=tk.LEFT)

        notes_frame = ttk.LabelFrame(right_frame, text="Notes")
        notes_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        self.notes_text = tk.Text(notes_frame, height=8, wrap=tk.WORD)
        self.notes_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        ttk.Button(notes_frame, text="Save Notes", command=self._save_notes).pack(pady=2)

        checklist_frame = ttk.LabelFrame(right_frame, text="Checklist")
        checklist_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        add_item_frame = ttk.Frame(checklist_frame)
        add_item_frame.pack(fill=tk.X, padx=5, pady=2)
        self.new_item_entry = ttk.Entry(add_item_frame)
        self.new_item_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.new_item_entry.bind("<Return>", lambda e: self._add_checklist_item())
        ttk.Button(add_item_frame, text="Add Item", command=self._add_checklist_item).pack(side=tk.LEFT, padx=2)

        self.checklist_listbox = tk.Listbox(checklist_frame, selectmode=tk.SINGLE)
        self.checklist_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        self.checklist_listbox.bind("<Double-Button-1>", self._toggle_checklist_item)

        remove_item_btn = ttk.Button(checklist_frame, text="Remove Selected Item", command=self._remove_checklist_item)
        remove_item_btn.pack(pady=2)

        self.status_var = tk.StringVar()
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def _load_tasks(self) -> None:
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except (json.JSONDecodeError, OSError) as e:
                messagebox.showerror("Load Error", f"Could not load tasks: {e}")
                self.tasks = []
        self._refresh_task_list()

    def _save_tasks(self) -> None:
        try:
            tmp_file = DATA_FILE + ".tmp"
            with open(tmp_file, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, indent=2, ensure_ascii=False)
            os.replace(tmp_file, DATA_FILE)
            self.status_var.set("Tasks saved.")
        except OSError as e:
            messagebox.showerror("Save Error", f"Could not save tasks: {e}")

    def _refresh_task_list(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)

        for task in self.tasks:
            done_mark = "✓" if task.get("completed", False) else ""
            self.tree.insert("", tk.END, iid=task["id"], values=(done_mark, task["title"]))

    def _on_task_select(self, event=None) -> None:
        selection = self.tree.selection()
        if not selection:
            self.current_task_id = None
            return
        task_id = selection[0]
        self.current_task_id = task_id
        task = self._get_task_by_id(task_id)
        if task:
            self.title_var.set(task["title"])
            self.notes_text.delete("1.0", tk.END)
            self.notes_text.insert("1.0", task.get("notes", ""))
            self._refresh_checklist(task)

    def _get_task_by_id(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def _add_task(self) -> None:
        title = simpledialog.askstring("New Task", "Enter task title:")
        if title:
            new_task = {
                "id": str(uuid.uuid4()),
                "title": title.strip(),
                "notes": "",
                "checklist": [],
                "completed": False,
            }
            self.tasks.append(new_task)
            self._refresh_task_list()
            self._save_tasks()
            self.tree.selection_set(new_task["id"])
            self._on_task_select()

    def _delete_task(self) -> None:
        if not self.current_task_id:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return
        if messagebox.askyesno("Confirm Delete", "Delete this task?"):
            self.tasks = [t for t in self.tasks if t["id"] != self.current_task_id]
            self.current_task_id = None
            self._refresh_task_list()
            self._clear_details()
            self._save_tasks()

    def _toggle_task_done(self) -> None:
        if not self.current_task_id:
            return
        task = self._get_task_by_id(self.current_task_id)
        if task:
            task["completed"] = not task.get("completed", False)
            self._refresh_task_list()
            self._save_tasks()
            self.tree.selection_set(self.current_task_id)

    def _update_title(self) -> None:
        if not self.current_task_id:
            return
        task = self._get_task_by_id(self.current_task_id)
        if task:
            task["title"] = self.title_var.get().strip()
            self._refresh_task_list()
            self._save_tasks()

    def _save_notes(self) -> None:
        if not self.current_task_id:
            return
        task = self._get_task_by_id(self.current_task_id)
        if task:
            task["notes"] = self.notes_text.get("1.0", tk.END).strip()
            self._save_tasks()

    def _refresh_checklist(self, task) -> None:
        self.checklist_listbox.delete(0, tk.END)
        for item in task.get("checklist", []):
            prefix = "✓ " if item.get("done", False) else "☐ "
            self.checklist_listbox.insert(tk.END, prefix + item["text"])

    def _add_checklist_item(self) -> None:
        if not self.current_task_id:
            return
        text = self.new_item_entry.get().strip()
        if not text:
            return
        task = self._get_task_by_id(self.current_task_id)
        if task:
            task.setdefault("checklist", []).append({"text": text, "done": False})
            self._refresh_checklist(task)
            self.new_item_entry.delete(0, tk.END)
            self._save_tasks()

    def _toggle_checklist_item(self, event=None) -> None:
        if not self.current_task_id:
            return
        selection = self.checklist_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        task = self._get_task_by_id(self.current_task_id)
        if task and 0 <= index < len(task.get("checklist", [])):
            item = task["checklist"][index]
            item["done"] = not item.get("done", False)
            self._refresh_checklist(task)
            self._save_tasks()

    def _remove_checklist_item(self) -> None:
        if not self.current_task_id:
            return
        selection = self.checklist_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        task = self._get_task_by_id(self.current_task_id)
        if task and 0 <= index < len(task.get("checklist", [])):
            del task["checklist"][index]
            self._refresh_checklist(task)
            self._save_tasks()

    def _clear_details(self) -> None:
        self.title_var.set("")
        self.notes_text.delete("1.0", tk.END)
        self.checklist_listbox.delete(0, tk.END)


if __name__ == "__main__":
    show_banner()


    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
