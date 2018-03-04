import tkinter as tk

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        for task in self.tasks:
            task.grid()
        self.task_create = tk.Text(self, height=3, bg="white", fg="black")
        self.task_create.pack()
        self.task_create.focus_set()
        self.bind("<Return>", self.add_task)
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()
        if len(task_text) > 0:
            self.tasks.append(tk.Label(self, text=task_text, pady=10).pack())
        self.task_create.delete(1.0, tk.END)
if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
