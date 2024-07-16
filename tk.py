import tkinter as tk

root = tk.Tk()
root.title("Pack Layout")
root.geometry("400x300")

label1 = tk.Label(root, text="Top", bg="red", fg="white")
label1.pack(fill='x')

label2 = tk.Label(root, text="Center", bg="green", fg="white")
label2.pack(fill='x')

label3 = tk.Label(root, text="Bottom", bg="blue", fg="white")
label3.pack(fill='x')

root.mainloop()
