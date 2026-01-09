class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} I am a student with ID: {self.student_id}."
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} I teach {self.subject}."
    
# Example usage
if __name__ == "__main__":
    person = Person("Alice", 30)
    student = Student("Bob", 20, "S12345")
    teacher = Teacher("Charlie", 40, "Mathematics")

    print(person.introduce())
    print(student.introduce())
    print(teacher.introduce())