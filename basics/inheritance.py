class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls,origin,friend_name,salary):
        return cls(friend_name, origin.school, salary)


##

class WorkingStudent(Student):
    def __init__(self,name, school, salary):
        super().__init__(name,school)
        self.salary = salary


anna = WorkingStudent("Anna","Oxford", 20.00)
print(anna.salary)

friend = WorkingStudent.friend(anna, "Greg", 17.50)
