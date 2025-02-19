import tkinter as tk
from tkinter import messagebox
import csv

file_name = "tasks.csv"

tasks = []

# Load tasks from tasks.csv file
def load_tasks():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for task in reader:
                tasks.append(task[0])
    except FileNotFoundError:
        pass

def show_tasks():
    tasks_listbox.delete(0, tk.END)
    
    for index, task in enumerate(tasks):
        if index % 2 == 0:
            bg_color = "#00ffff"  # Light Gray for even rows
        else:
            bg_color = "#33ccff"  # White for odd rows
        
        tasks_listbox.insert(tk.END, task)
        tasks_listbox.itemconfig(index, {'bg': bg_color})


def save_tasks():
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])
    messagebox.showinfo("Tasks", "Tasks saved")


# Add task to the listbox and tasks list (CSV file)
def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showerror("Error", "Task cannot be empty")
        return
    if task in tasks:
        messagebox.showwarning("Warning", "Task already exists!")
        return

    tasks.append(task)
    tasks_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    save_tasks()

# Mark task as done
def mark_task():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks[index]

        if task.startswith("✓ "):  # Prevent multiple ✓ marks
            messagebox.showwarning("Warning", "Task is already marked as done!")
            return

        task = f"✓ {task}"
        tasks[index] = task
        tasks_listbox.delete(index)
        tasks_listbox.insert(index, task)
        save_tasks()

    except IndexError:
        messagebox.showerror("Error", "No task selected")

# Double-click to edit task
def on_double_click(event):
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks[index]

        # Remove checkmark if task is marked completed
        if task.startswith("✓ "):
            task = task[2:]

        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)

        # Bind Enter key to update_task with arguments
        task_entry.bind("<Return>", lambda event: update_task(index))
    except IndexError:
        pass

def update_task(index):
    new_task = task_entry.get().strip()

    if not new_task:
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    # Prevent duplicate task entries
    if new_task in tasks and new_task != tasks[index]:
        messagebox.showwarning("Warning", "Task already exists!")
        return

    # Preserve completion status
    completed_status = "✓ " if tasks[index].startswith("✓ ") else ""
    tasks[index] = f"{completed_status}{new_task}"

    # Update listbox
    tasks_listbox.delete(index)
    tasks_listbox.insert(index, tasks[index])

    # Clear input field
    task_entry.delete(0, tk.END)

    # Save updated tasks to CSV
    save_tasks()


def delete_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks.pop(index)
        tasks_listbox.delete(index)
        save_tasks()
    except IndexError:
        messagebox.showerror("Error", "No task selected")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry("%dx%d+%d+%d" % (width, height, x, y))

#add a placeholder to the entry widget
def add_placeholder(entery, placeholderTxt):
    def focus_in(event):
        if entery.get() == placeholderTxt:
            entery.delete(0, tk.END)
            entery.config(fg='black')
    
    def focus_out(event):
        if entery.get():
            entery.delete(0, tk.END)
            entery.config(fg='grey')

    entery.insert(0, placeholderTxt)
    entery.config(fg='grey')

    entery.bind('<FocusIn>', focus_in)
    entery.bind('<FocusOut>', focus_out)



def main():
    global tasks_listbox, task_entry
    root = tk.Tk()
    root.geometry("500x1500")
    root.resizable(False, False)
    root.configure(bg="blue", padx=10, pady=10)
    root.title("To-Do List")

    # Center the window on the screen
    center_window(root, 500, 570)

    nameLabel = tk.Label(root, text="Developed By : Prof. Hezzy", bg="blue", fg="white", font=("Arial", 12))
    nameLabel.pack()

    taskFrame = tk.Frame(root, bg="blue", padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
    taskFrame.pack()

    tasks_listbox = tk.Listbox(taskFrame, width=80, height=20, bg="#99ccff", font=("Arial", 12))
    tasks_listbox.pack(pady=10)
    tasks_listbox.bind("<Double-1>", on_double_click)

    task_entry = tk.Entry(taskFrame, width=80, bg="white", font=("Arial", 12))
    task_entry.pack(side=tk.LEFT, padx=5, ipady=10)

    add_placeholder(task_entry, "Enter your task here...")

    BtnFrame = tk.Frame(root, bg="blue")
    BtnFrame.pack(ipadx=10, ipady=10)

    addBtn = tk.Button(BtnFrame, text="Add Task", bg="green", fg="white", command=add_task, width=10)
    addBtn.grid(row = 0, column = 1, padx=5, ipady=10, ipadx=10)

    delBtn = tk.Button(BtnFrame, text="Delete Task", bg="red", fg="white", command=delete_task, width=10)
    delBtn.grid(row=0, column=2, padx=5, pady=10, ipadx=10, ipady=8)

    #updtBtn = tk.Button(BtnFrame, text="Update Task", bg="orange", fg="white", command=lambda: update_task(tasks_listbox.curselection()[0] if tasks_listbox.curselection() else None))
    #updtBtn.grid(row=0, column=2, padx=5)

    mrkBtn = tk.Button(BtnFrame, text="Mark Task", bg="purple", fg="white", command=mark_task, width=10)
    mrkBtn.grid(row=0, column=3, padx=5, pady=10, ipadx=10, ipady=8)

    exitBtn = tk.Button(BtnFrame, text="Exit", bg="black", fg="white", command=root.quit, width=10)
    exitBtn.grid(row=0, column=4, padx=5, ipadx=10, ipady=8)

    

    #showBtn = tk.Button(BtnFrame, text="Show Tasks", bg="black", fg="white", command=show_tasks)
    #showBtn.grid(row=0, column=4, padx=5, ipadx=10, ipady=8)

    #saveBtn = tk.Button(BtnFrame, text="Save Tasks", bg="black", fg="white", command=save_tasks)
    #saveBtn.grid(row=0, column=4, padx=5)

    load_tasks()
    for task in tasks:
        tasks_listbox.insert(tk.END, task)
    tasks_listbox.bind("<Double-1>", on_double_click)

    show_tasks()

    root.mainloop()


if __name__ == "__main__":
    main()
