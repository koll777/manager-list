import tkinter as tk
from tkinter import ttk

tasks = []

def main():
    root = tk.Tk()
    root.title("Пример проекта на Python с Tkinter")
    root.geometry("400x400")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)

    label = ttk.Label(main_frame, text="Это пример интерфейса")
    label.pack(pady=10)

    task_entry = ttk.Entry(main_frame)
    task_entry.pack(pady=5)

    add_button = ttk.Button(main_frame, text="Добавить задачу",
                            command=lambda: add_task(task_entry))
    add_button.pack(pady=5)

    tasks_listbox = tk.Listbox(main_frame, height=10)
    tasks_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def update_task_list():
        tasks_listbox.delete(0, tk.END)
        for task in tasks:
            tasks_listbox.insert(tk.END, task)

    def add_task(entry_widget):
        task_text = entry_widget.get().strip()
        if task_text:
            tasks.append(task_text)
            update_task_list()
            entry_widget.delete(0, tk.END)

    root.mainloop()

def on_button_click(label):
    label.config(text="Кнопка нажата!")

if __name__ == "__main__":
    main()
