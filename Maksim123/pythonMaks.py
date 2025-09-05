1import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from pathlib import Path

class FileManagerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Manager")
        self.geometry("800x600")
        
        # Главное окно делится на две панели
        left_frame = ttk.Frame(self)
        right_frame = ttk.Frame(self)
        left_frame.pack(side="left", fill="both", expand=True)
        right_frame.pack(side="right", fill="both", expand=True)
        
        # Дерево директорий слева
        self.treeview = ttk.Treeview(left_frame)
        self.treeview.pack(fill="both", expand=True)
        self.treeview.heading("#0", text="Древо директорий")
        self.populate_treeview('/')
        
        # Списки файлов справа
        self.file_listbox = tk.Listbox(right_frame)
        self.file_listbox.pack(fill="both", expand=True)
        
        # Кнопки для навигации и поиска
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)
        
        select_button = ttk.Button(button_frame, text="Открыть выбранную директорию",
                                  command=self.open_selected_directory)
        select_button.pack(side="left", padx=5)
        
        search_button = ttk.Button(button_frame, text="Искать файлы...",
                                  command=self.search_files_dialog)
        search_button.pack(side="left", padx=5)
        
        exit_button = ttk.Button(button_frame, text="Выход", command=self.quit)
        exit_button.pack(side="left", padx=5)
    
    def populate_treeview(self, path):
        """Заполняет древовидный вид всеми папками"""
        self.treeview.delete(*self.treeview.get_children())
        parent_node = self.treeview.insert('', 'end', text=Path(path).anchor)
        self.recursive_populate(parent_node, path)
    
    def recursive_populate(self, parent, path):
        """Рекурсивно добавляет элементы дерева"""
        try:
            children = next(os.walk(path))[1]
            for child in children:
                full_child_path = os.path.join(path, child)
                node_id = self.treeview.insert(parent, 'end', text=child)
                self.recursive_populate(node_id, full_child_path)
        except PermissionError:
            pass
    
    def open_selected_directory(self):
        selected_item = self.treeview.focus()
        if selected_item:
            path = self.treeview.item(selected_item)['text']
            if os.path.exists(path):
                self.current_directory = path
                self.update_file_list()
    
    def update_file_list(self):
        """Обновляет список файлов справа"""
        self.file_listbox.delete(0, tk.END)
        files = os.listdir(self.current_directory)
        for file in files:
            self.file_listbox.insert(tk.END, file)
    
    def search_files_dialog(self):
        """Диалог поиска файлов"""
        pattern = filedialog.askstring("Поиск файлов", "Введите маску поиска (например, *.txt)")
        if pattern:
            results = []
            for root, _, files in os.walk(self.current_directory):
                for file in files:
                    if fnmatch.fnmatch(file, pattern):
                        results.append(os.path.join(root, file))
            if results:
                self.file_listbox.delete(0, tk.END)
                for res in results:
                    self.file_listbox.insert(tk.END, res)
            else:
                self.file_listbox.insert(tk.END, "Файлы не найдены.")

if __name__ == "__main__":
    app = FileManagerGUI()
    app.mainloop()