class student:
    def __init__(self, name, roll_number, branch, college):
        self.name = name
        self.roll_number = roll_number
    #protected variables
        self.branch = branch
        self.college = college
    #private variables
        self.__subjects={}
        self.__total_marks=0
        self.__percentage=0
        self.__grade=None

    def add_subject_marks(self, subject, marks):
        if 0<=marks<=100:
            self.__subjects[subject] = marks
            print(f"Marks for {subject} added successfully!")
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")
        
    def calculate_total_marks(self):
        if not self.__subjects:
            print("No subjects added yet!")
            return
        self.__total_marks = sum(self.__subjects.values())
        self.__percentage = (self.__total_marks / (len(self.__subjects) * 100)) * 100
        self.__grade = self.__calculate_grade()

    def __calculate_grade(self):
        if self.__percentage >= 90:
            return "'A'-Excellent"
        elif self.__percentage >= 80:
            return "'B'-Good"
        elif self.__percentage >= 70:
            return "'C'-Average"
        elif self.__percentage >= 60:
            return "'D'-Below Average"
        else:
            return "'F'-Fail"
    def display_result(self):
        if self.__grade is None:
            print("Please calculate total marks and grade first!")
            return
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")
        print(f"College: {self.college}")
        print(f"Total Marks: {self.__total_marks}")
        print(f"Percentage: {self.__percentage:.2f}%")
        print(f"Grade: {self.__grade}")

        for subject, marks in self.__subjects.items():
            print(f"{subject}: {marks} marks")
        print(f"Overall Grade: {self.__grade}")
        print(f"Percentage: {self.__percentage:.2f}%")


std1 = student("Sanket", "12345", "Computer Science", "XYZ College")
std2 = student("Anjali", "67890", "Mechanical Engineering", "ABC College")
std1.add_subject_marks("Mathematics", 95)
std1.add_subject_marks("Physics", 88)
std1.add_subject_marks("Chemistry", 92)
std1.calculate_total_marks()
std1.display_result()
print("\n")
std2.add_subject_marks("Mathematics", 88)
std2.add_subject_marks("Physics", 88)
std2.add_subject_marks("Chemistry", 92)
std2.calculate_total_marks()
std2.display_result()
