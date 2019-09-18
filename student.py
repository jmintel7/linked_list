class Student:

    def __init__(self, rollno, name, gender, marks):
        self.rollno = int(rollno)
        self.name = name
        self.gender = gender
        self.marks = int(marks)

    def display(self):
        print('Roll no: ', self.rollno)
        print('Name: ', self.name)
        print('Gender: ', self.gender)
        print('Marks: ', self.marks)
