
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, ID, salary):
        super().__init__(name, age)  
        self.salary = salary
        self.ID = ID

    def show_details(self):
        super().show_details()
        print(f"Employee created with name:{name}, {age}, ID:{ID}, and salary:{salary}")


class Manager(Employee):
    def __init__(self, name, age, ID, salary, department):
        super().__init__(name, age, ID, salary)  
        self.department = department


    def show_details(self):
        super().show_details()  
        print(f"Manger created with name:{name}, {age}, ID:{ID}, salary:{salary}Department: {self.department}")



person = ''
employee = ''
manager = ''

while True:
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Compare Salaries")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            person = Person(name, age)
            print(f"Person created with name: {name} and {age}.")
    elif choice == 2:
            if person is '':
                print("Please create a person first!")
                continue
            name = person.name
            age = person.age
            ID = int(input("enter the ID of employee:"))
            salary = float(input("Enter salary: "))
            employee = Employee(name, age, ID, salary)
            print(f"Employee created with name:{name}, age:{age}, ID:{ID}, and salary:{salary}.")

    elif choice == 3:
            if employee is '':
                print("Please create an employee first!")
                continue
            department = input("Enter department: ")
            manager = Manager(employee.name, employee.age, employee.ID, employee.salary, department)
            print(f"Manager created with name:{name}, age:{age}, ID:{ID}, and salary:{salary}, and department{department}.")
            
            break
    else:
        print("Invalid choice, please try again.")
            


