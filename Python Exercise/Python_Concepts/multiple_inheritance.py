class Details:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no


class Sports:
    def __init__(self, sport):
        self.sport = sport


# Inherit the Details and Sports classes to the Student Class
class Student(Details, Sports):
    def __init__(self, name, age, roll_no, sport):
        Details.__init__(self, name, age, roll_no)
        Sports.__init__(self, sport)


# Creating objects for the Student class
student1 = Student("Arun", 12, 1151, "Cricket")
student2 = Student("Bala", 13, 1152, "Foot Ball")

print(f"Name: {student1.name}, Age: {student1.age}, RollNo: {student1.roll_no}, Sport{student1.sport}")
print(f"Name: {student2.name}, Age: {student2.age}, RollNo: {student2.roll_no}, Sport{student2.sport}")
