class Marks:
    college = "College Name"

    def __init__(self, m1, m2, m3):
        self.__m1 = m1  # private attribute
        self._m2 = m2  # protected attribute
        self.m3 = m3  # public attribute

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Creating class method decorators for define the class method
    @classmethod
    def college_name(cls):
        return cls.college

    # Creating static method decorators for define the static method
    @staticmethod
    def static():
        print("Inside the Static Method")

    @property
    def m2(self):
        return self._m2


# Creating Objects for Marks Class
student1 = Marks(55, 88, 65)
student2 = Marks(54, 56, 74)

# printing class and static methods
print(student1.college_name())
student1.static()

# printing access specifiers
print("Protected Attribute", student1.m2)
print("Public Attribute", student1.m3)

# printing Private attribute
try:
    print("Private Attribute", student1.__m1)

except AttributeError:
    print("**It is a Private Attribute**")
