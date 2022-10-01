class Students:
    def __init__(self, name, student_ID):
        self.name = name
        self.student_ID = student_ID

    def learning(self):
        return "Student should learn Python!"

class Freshman_student(Students):
    def __init__(self, name, student_ID, graduation_year):
        super().__init__(name, student_ID)
        self.__graduation_year = graduation_year

    def get_graduation_year(self):
        return f'My graduation year is {self.__graduation_year}'

    def set_graduation_year(self, year):
        self.__graduation_year = year

    def welcome(self):
        return "Congratulations! Welcome to the college!"

class Sophomore_student(Freshman_student):
    def __init__(self, name, student_ID, graduation_year, score):
        super().__init__(name, student_ID, graduation_year)
        self.score = score



student1 = Students('Alex',  20234451)
print("Name: ", student1.name, "ID:", student1.student_ID)
print(student1.learning())

newStudent = Freshman_student('Anna', 33347563, 2021)
print("Name: ", newStudent.name, "ID: ", newStudent.student_ID)
print(newStudent.welcome())

# second_Year_Student = Sophomore_student('Mary', 40455623, 3.7)
# print(second_Year_Student.graduation_year)

student2 = Sophomore_student('Garry', 3938264, 2020, 3.7)
# student2.set_graduation_year(2020)
print(student2.get_graduation_year())