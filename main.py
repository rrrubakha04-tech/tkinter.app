import tkinter as tk

root = tk.Tk()
root.title("Тест Tkinter")
root.geometry("300x200")

label = tk.Label(root, text="Работает в GitHub!", font=("Arial", 14))
label.pack(pady=50)

root.mainloop()
