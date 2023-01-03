

# Car is a class
class Car:

    def __init__(self, car_model, car_color):
        self.model = car_model
        self.color = car_color

    def __str__(self):
        return f"[color: {self.color}, model: {self.model}]"

    # start is a Car method not a function
    def start(self):
        print(f"starting {self.model}")
    



class Student:

    def __init__(self, student_name, student_grade):
        self.name = student_name
        self.grade = student_grade

class Course:

    def __init__(self, course_title, course_student_list):
        self.title = course_title
        self.student_list = course_student_list

    def avg(self):
        total = 0
        count = 0
        for the_student in self.student_list:
            try:
                total = total + the_student.grade
                count = count + 1
            except AttributeError:
                pass
        if count != 0:
            return total / count
        else:
            return 0 


class Animal:
    
    def __init__(self, is_wild = False):
        self.wildness = is_wild
        pass

    def run(self):
        print("running...")

class Mamal(Animal):
    pass

class Dog(Mamal):
    pass

class Cat(Mamal):
    pass











