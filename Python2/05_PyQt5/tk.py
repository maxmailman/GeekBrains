import tkinter

# Создали окно
root = tkinter.Tk()

t = tkinter.Text()

# Обработка событий - просто функция
def hello():
    print("Привет!")
    t.insert("0.0", "Какой то текст!\n")


# Рисуем компоненты
b = tkinter.Button(text="Нажми меня!", command=hello)

# Размещение элемента
b.grid(row=1, column=1)


t.grid(row=2, column=2)

root.mainloop()

print("Конец")
