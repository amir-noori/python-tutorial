
from oop import *


def car_test():
    # peykan is an object
    peykan = Car("Peykan", "Gojeie")
    pride = Car("Pride", "zard")

    peykan.start()
    pride.start()

    print(peykan)

def avg(student_list):
    total = 0
    count = 0
    for the_student in student_list:
        try:
            total = total + the_student.grade
            count = count + 1
        except AttributeError:
            pass
    if count != 0:
        return total / count
    else:
        return 0

def student_test():
    jack = Student("Jack", 12)
    joe = Student("Joe", 16)
    jim = Student("Jim", 18.5)

    # print(avg([jack, joe, jim, Car("dummy", "dummy")]))
    math_course = Course("Math", [jack, joe, jim])
    average = math_course.avg()
    print(f"average -> {average}")

def animal_test():
    nikke = Cat()
    figo = Dog()

    nikke.run()


if __name__ == "__main__":
    # car_test()
    # student_test()
    animal_test()

