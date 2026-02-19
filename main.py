import tkinter as tk
from tkinter import ttk, messagebox

def main():
    # Создаем главное окно
    root = tk.Tk()
    root.title("Список пользователей")
    root.geometry("400x350")

    # Создаем основной фрейм
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Создаем метку
    label = ttk.Label(main_frame, text="Введите имя пользователя:")
    label.pack(pady=5)

    # Поле ввода
    entry = ttk.Entry(main_frame)
    entry.pack(pady=5)

    # Список пользователей
    listbox = tk.Listbox(main_frame, height=8)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    # Кнопка добавления
    add_button = ttk.Button(
        main_frame,
        text="Добавить пользователя",
        command=lambda: add_user(entry, listbox)
    )
    add_button.pack(pady=5)

    # Кнопка удаления
    delete_button = ttk.Button(
        main_frame,
        text="Удалить выбранного",
        command=lambda: delete_user(listbox)
    )
    delete_button.pack(pady=5)

    # Запускаем главный цикл
    root.mainloop()

# Добавление пользователя
def add_user(entry, listbox):
    name = entry.get()

    if name.strip() == "":
        messagebox.showwarning("Ошибка", "Введите имя!")
        return

    listbox.insert(tk.END, name)
    entry.delete(0, tk.END)

# Удаление выбранного пользователя
def delete_user(listbox):
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Ошибка", "Выберите пользователя для удаления!")
        return

    listbox.delete(selected[0])

if __name__ == "__main__":
    main()