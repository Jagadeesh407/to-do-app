import tkinter as tk
from tkinter import messagebox, filedialog

tasks = []

# Functions
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task first!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def save_tasks():
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    global tasks
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        update_listbox()

# GUI Setup
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=25, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

del_btn = tk.Button(root, text="Delete Selected", command=delete_task, bg="red", fg="white")
del_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save Tasks", command=save_tasks)
save_btn.pack(pady=2)

load_btn = tk.Button(root, text="Load Tasks", command=load_tasks)
load_btn.pack(pady=2)

root.mainloop()