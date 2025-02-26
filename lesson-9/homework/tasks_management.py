import json
import csv

TASKS_JSON_FILE = "tasks.json"
TASKS_CSV_FILE = "tasks.csv"

# Function to load tasks
def load_tasks():
    with open(TASKS_JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Function to save tasks
def save_tasks(tasks):
    with open(TASKS_JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to {TASKS_JSON_FILE}.")

# Function to convert JSON to CSV
def convert_json_to_csv():
    tasks = load_tasks()
    with open(TASKS_CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"Tasks successfully converted to {TASKS_CSV_FILE}.")

# Function to display tasks
def display_tasks():
    tasks = load_tasks()
    print("\nTasks List:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

# Main execution
if __name__ == "__main__":
    display_tasks()
    convert_json_to_csv()