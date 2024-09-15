# class: class is a blueprint of object
# object: Object is a instance of class

class student():
    def student_detail(self):
        roll_no = 10
        print(roll_no)

    def student_name(self, name):
        print(name)


object = student()
object.student_detail()
object.student_name("ashjash as dasd ")