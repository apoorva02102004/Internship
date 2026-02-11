class Student:
    
    # Class Variable (Shared by all students)
    college_name = "ABC College"
    
    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("------------------------")
    
    # Class Method (Updates class variable)
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name
    
    # Static Method (Helper function)
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"


# Creating 2 Student Objects
student1 = Student("Rahul", 101)
student2 = Student("Priya", 102)

# Printing Student Details (Before Changing College)
print("Before Changing College:")
student1.display()
student2.display()

# Changing College Name using Classmethod
Student.change_college("XYZ College")

# Printing Student Details (After Changing College)
print("After Changing College:")
student1.display()
student2.display()

# Using Staticmethod to Check Pass/Fail
print("Result of Rahul (Marks: 80):", Student.is_pass(80))
print("Result of Priya (Marks: 30):", Student.is_pass(30))
