import tkinter as tk
root = tk.Tk()

root.geometry("500x500")
root.title("aemd")



label = tk.Label(root, text="Let`s make students life harder", font=('Calibri', 18))
label.pack()

button = tk.Button(root, text="Click me!", font=('Calibri', 16))
button.pack(padx=10, pady=10)

root.mainloop()