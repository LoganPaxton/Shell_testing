#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

# File to store the to-do list
TODO_FILE = "todo.txt"

# Create the main application window
root = tk.Tk()
root.title("Todo List")

# Function to add a task to the to-do list
def add_task():
    task = entry.get()
    if task:
        with open(TODO_FILE, "a") as file:
            file.write(task + "\n")
        entry.delete(0, tk.END)
        messagebox.showinfo("Task added", "Task added: {task}")
    else:
        messagebox.showwarning("Empty task", "Please enter a task.")

# Function to view the to-do list
def view_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            tasks = file.read().strip()
        if tasks:
            messagebox.showinfo("Todo List", tasks)
        else:
            messagebox.showinfo("Todo List", "No tasks found.")
    except FileNotFoundError:
        messagebox.showinfo("Todo List", "No tasks found.")

# Function to delete a task from the to-do list
def delete_task():
    try:
        task_num = int(entry.get())
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            with open(TODO_FILE, "w") as file:
                file.writelines(tasks)
            entry.delete(0, tk.END)
            messagebox.showinfo("Task deleted", "Task deleted: {task_num}")
        else:
            messagebox.showwarning("Invalid task number", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Invalid task number", "Invalid task number.")
    except FileNotFoundError:
        messagebox.showinfo("Todo List", "No tasks found.")

# Create and configure UI elements
label = tk.Label(root, text="Enter task:")
label.pack()
entry = tk.Entry(root)
entry.pack()
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
view_button = tk.Button(root, text="View Tasks", command=view_tasks)
view_button.pack()
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Start the main event loop
root.mainloop()
