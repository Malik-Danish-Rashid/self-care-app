import tkinter as tk
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("Self-Care Application")
root.geometry("600x400")

current_date = datetime.now().strftime("%Y-%m-%d")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

physical_health_tasks = ["Morning Exercise", "Drink Water", "Eat Healthy", "Go for a Walk", "Get Enough Sleep"]
learning_skills_tasks = ["Read a Book", "Practice Coding", "Learn New Words", "Watch Educational Video", "Solve Puzzles"]
entertainment_tasks = ["Listen to Music", "Watch a Movie", "Play a Game", "Draw or Paint", "Spend Time with Friends"]
all_tasks = {
    "Physical Health": physical_health_tasks,
    "Learning Skills": learning_skills_tasks,
    "Entertainment": entertainment_tasks
}

task_vars = []

def update_progress():
    total_tasks = len(physical_health_tasks + learning_skills_tasks + entertainment_tasks)
    completed_tasks = sum(var.get() for var in task_vars)
    progress_percentage = (completed_tasks / total_tasks) * 100
    
    progress_label.config(text=f"Tasks Completed: {completed_tasks}/{total_tasks} ({progress_percentage:.0f}%)")
    if progress_percentage >= 70:
        progress_message.config(text="Perfect", fg="green")
    elif 40 <= progress_percentage < 70:
        progress_message.config(text="Good Job", fg="blue")
    else:
        progress_message.config(text="You can do it", fg="red")

def create_tab(title, tasks):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=title)
    
    tk.Label(frame, text=f"{title} Tasks", font=("Arial", 14)).pack(pady=10)
    tk.Label(frame, text=f"Date: {current_date}", font=("Arial", 12)).pack(pady=5)
    
    for task in tasks:
        var = tk.IntVar()
        checkbox = tk.Checkbutton(frame, text=task, variable=var, command=update_progress)
        checkbox.pack(anchor="w")
        task_vars.append(var)
    
   
    tk.Label(frame, text="Noa's Project", font=("Arial", 10), fg="gray").pack(side="bottom", anchor="e", padx=10, pady=10)
    return frame


create_tab("Physical Health", physical_health_tasks)
create_tab("Learning Skills", learning_skills_tasks)
create_tab("Entertainment", entertainment_tasks)


progress_tab = ttk.Frame(notebook)
notebook.add(progress_tab, text="Today's Progress")

tk.Label(progress_tab, text="Today's Progress", font=("Arial", 14)).pack(pady=10)
tk.Label(progress_tab, text=f"Date: {current_date}", font=("Arial", 12)).pack(pady=5)

progress_label = tk.Label(progress_tab, text="Tasks Completed: 0/15 (0%)", font=("Arial", 12))
progress_label.pack(pady=10)

progress_message = tk.Label(progress_tab, text="", font=("Arial", 16))
progress_message.pack(pady=10)

tk.Label(progress_tab, text="Noa's Project", font=("Arial", 10), fg="gray").pack(side="bottom", anchor="e", padx=10, pady=10)

update_progress()

root.mainloop()
