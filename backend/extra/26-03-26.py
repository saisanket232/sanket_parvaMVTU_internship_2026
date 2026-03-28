class Employee:
    id_counter=1000
    def __init__(self, name, dob, email, phone, education):
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.education = education

        self.skills = []   # list
        self.emp_id = None
        self.department = None
        self.work = None
        self.time_taken = None
        self.works = []
        self.times = []

    def register_employee(self ,department):
        self.emp_id = Employee.id_counter
        Employee.id_counter += 1
        self.department = department
        print(f"Employee {self.name} registered with ID: {self.emp_id} and Department: {self.department}")

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"Skill '{skill}' added to employee {self.name}")

    def assign_work(self, work):
    self.works.append(work)
    print(f"Work '{work}' assigned to employee {self.name}")

def complete_work(self, time_taken):
    self.times.append(time_taken)
    print(f"Work completed in {time_taken} hours")

    def display_details(self):
    print("\nEmployee Details")
    print("Name:", self.name)
    print("ID:", self.emp_id)
    print("Department:", self.department)
    print("Skills:", self.skills)

        print("Work History:")
        if not self.works:
            print("   No work assigned yet")
        else:
            for w, t in zip(self.works, self.times):
                print(f"   {w} → {t} hours")    

employees = []

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Assign Work")
    print("3. Search Employee")
    print("4. Display All")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("\nEnter details for Employee:")
        name = input("Name: ")
        dob = input("DOB: ")
        email = input("Email: ")
        phone = input("Phone: ")
        education = input("Education: ")

        emp = Employee(name, dob, email, phone, education)

        dept = input("Department: ")
        emp.register_employee(dept)

        skill_count = int(input("How many skills? "))
        for _ in range(skill_count):
            skill = input("Enter skill: ")
            emp.add_skill(skill)

        employees.append(emp)
        print("Employee added successfully!")

    elif choice == '2':
        try:
            emp_id = int(input("\nEnter Employee ID to assign work: "))
        except ValueError:
            print("Invalid ID format!")
            continue
            
        found = False
        for emp in employees:
            if emp.emp_id == emp_id:
                work = input(f"Assign work for {emp.name}: ")
                emp.assign_work(work)
                try:
                    time_taken = int(input("Time taken (hours): "))
                    emp.complete_work(time_taken)
                except ValueError:
                    print("Invalid time format!")
                found = True
                break
        if not found:
            print("Employee not found!")

    elif choice == '3':
        try:
            search_id = int(input("\nEnter ID to search: "))
        except ValueError:
            print("Invalid ID format!")
            continue
            
        found = False
        for emp in employees:
            if emp.emp_id == search_id:
                emp.display_details()
                found = True
                break
        if not found:
            print("Employee not found!")

    elif choice == '4':
        if not employees:
            print("\nNo employees to display.")
        else:
            print("\n--- All Employees ---")
            for emp in employees:
                emp.display_details()

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")