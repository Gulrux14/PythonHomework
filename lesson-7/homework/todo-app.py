import json
import csv
import os

class Task:
    def init(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def str(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class TaskManager:
    JSON_FILE = "tasks.json"
    CSV_FILE = "tasks.csv"

    def init(self):
        if not os.path.exists(self.JSON_FILE):
            with open(self.JSON_FILE, 'w') as file:
                json.dump([], file)

    def add_task(self, task):
        tasks = self.load_tasks()
        tasks.append(task.dict)
        with open(self.JSON_FILE, "w") as file:
            json.dump(tasks, file, indent=4)

    def load_tasks(self):
        with open(self.JSON_FILE, "r") as file:
            return json.load(file)

    def view_tasks(self):
        tasks = self.load_tasks()
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                print(Task(**task))

    def delete_task(self, task_id):
        tasks = self.load_tasks()
        tasks = [t for t in tasks if t["task_id"] != task_id]
        with open(self.JSON_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
        print("Task deleted successfully.")