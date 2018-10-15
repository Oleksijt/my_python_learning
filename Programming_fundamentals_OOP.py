# class Message:
#     def greeting(self, name):
#         return 'Hello {}.'.format(name)
#
# message = Message()
# message.greeting('Pavlo')
# print(message.greeting('Pavlo'))


# class Message:
#     class_var = 2
#
#     def __init__(self):
#         self.instance_var = 4
#
#
# message = Message()
# new_message = Message()
# print(message.instance_var)
# message.instance_var = 6
# print(message.instance_var)
# print(new_message.instance_var)
# print(message.class_var)
# print(new_message.class_var)
# Message.class_var = 6
# print(message.class_var)
# print(new_message.class_var)


# """Classwork
# Create a class Student
# Student has `name` attribute
# It should be able to add a student to collection.
# It should be able to show a list of added students.
# Expected behaviour:
# student = Student()
# student.add(“Pavlo”)
# student.add(“Ivan”)
# student.show_students()  # “Pavlo”, “Ivan”
# """
# class Student:
#     def __init__(self):
#         self.students = []
#         pass
#
#     def add(self, name):
#         self.students.append(name)
#
#     def show_students(self):
#         return self.students
#
#
# student = Student()
# student.add('Pavlo')
# student.add('Ivan')
#
# print(student.show_students())


#
# class Human:
#     def __init__(self):
#         self.__deposit_sum = 15000
#     def increase_deposit(self, value):
#         self.__deposit_sum += value
#     def show_deposit(self):
#         return self.__deposit_sum
# h = Human()
# print(h.show_deposit())
# h.increase_deposit(1500)
# print(h.show_deposit())


# class Human:
#     def get_location(self):
#         return 'Your location is Ukraine.'
#
#
# class Student(Human):
#     def get_scholarship(self):
#         return 'Your scholarship is 1000.'
#
#     def get_subjects(self):
#         return 'Your favourite subjects are mathematics and informatics.'
#
# student = Student()
# print(student.get_scholarship())
# print(student.get_subjects())
# print(student.get_location())




# import math
#
# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#     def get_area(self):
#         return self.width * self.length
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return math.pi * self.radius **2
#
#
# figures = [Rectangle(10, 20), Circle(15), Rectangle(15, 40), Circle(20), Rectangle(50, 100)]
# for figure in figures:
#     print(figure.get_area())




"""OOP. Classwork (try to do it)
Create class `Human` with name, age, email, sex(None by default)
`email` should be a private attribute.
Add an ability to change a email.
Create a child class `Male`.
`Male` defines `sex` as a `male`.
male = Male()
male.get_sex()  # Returns male
male.change_email(“new_email@example.com”)
male.show_email()
"""


class Human:
    def __init__(self, name, age, email='', sex=None):
        self.name = name
        self.age = age
        self.email = email
        self.sex = sex

    def change_email(self, new_email):
        self.email = new_email

    def show_email(self):
        return self.email

    def get_sex(self):
        return self.sex

class Male(Human):
    def __init__(self):
        self.sex = 'male'




male = Male()
print(male.get_sex())
print(male.show_email())
male.change_email('new_email@example.com')
print(male.show_email())



# class Test:
#     __private_var = 42
#
#
# test = Test()
# print(test._Test__private_var)