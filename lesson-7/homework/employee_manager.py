import os

class Employee:
    def init(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def str(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def init(self):
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, 'w').close()  # Create the file if it doesn't exist

    def add_employee(self, employee):
        with open(self.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")

    def view_employees(self):
        with open(self.FILE_NAME, "r") as file:
            employees = file.readlines()
            if not employees:
                print("No employees found.")
            else:
                for emp in employees:
                    print(emp.strip())

    def search_employee(self, employee_id):
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(str(employee_id)):
                    print("Employee Found:\n", line.strip())
                    return
        print("Employee not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated_lines = []
        found = False
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(", ")
                if data[0] == str(employee_id):
                    found = True
                    if name: data[1] = name
                    if position: data[2] = position
                    if salary: data[3] = str(salary)
                    updated_lines.append(", ".join(data) + "\n")
                else:
                    updated_lines.append(line)
        
        if found:
            with open(self.FILE_NAME, "w") as file:
                file.writelines(updated_lines)
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    def delete_employee(self, employee_id):
        lines = []
        deleted = False
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(str(employee_id)):
                    lines.append(line)
                else:
                    deleted = True
        
        with open(self.FILE_NAME, "w") as file:
            file.writelines(lines)

        print("Employee deleted successfully." if deleted else "Employee not found.")