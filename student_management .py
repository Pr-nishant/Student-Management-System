import os

fli_p= r"C:\Users\USER\Desktop\StudentManagementSystem\Info.txt"

class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_students()
    
    def load_students(self):
        if not os.path.exists(fli_p):
            return
        
        with open(fli_p, "r") as f:
            for line in f:
                line  = line.strip()
                if line:
                    name, roll_no, course = line.split(",")
                    name = name.strip()
                    roll_no = roll_no.strip()
                    course = course.strip()
                    self.students.append(Student(name, roll_no,course)) 

    def sv_student(self):
        with open(fli_p, "w") as f:
            for student in self.students:
                f.write(f"{student.name},{student.roll_no},{student.course}\n")


    def add_student(self):
        name= input("Enter Name of the Student: ")
        roll_no = input("enter roll no: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Roll No already exists")
                return
            
        course = input("Enter Course: ")
        student = Student(name, roll_no, course)
        self.students.append(student)
        self.sv_student()
        print("Student Added Successfully!")


    def view_student(self):
        if not  self.students:
            print("No Record Found!")
            return
        for student in self.students:
            print("*" * 45)
            print(f"Name       : {student.name}")
            print(f"roll_no    : {student.roll_no}")
            print(f"course     : {student.course}")

    def search_student(self):
        roll_no = input("enter roll no: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent found!")
                print(f"Name         :{student.name}")
                print(f"roll_no      :{student.roll_no}")
                print(f"course       :{student.course}")
                return
        print ("Student Not Found!")


    def update_student(self):
        roll_no = input("enter roll no: ")

        for student in self.students:
            if student.roll_no == roll_no:
                print("\nCurrent Details")
                print(f"Name   : {student.name}")
                print(f"Course : {student.course}")


                student.name = input("Enter New name: ")
                student.course = input("Enter New Course: ")
                self.sv_student()
                print("Student Updated Successfully!")
                print("\nUPDATED DETAILS")
                print(f"Name   : {student.name}")
                print(f"Course : {student.course}")
                return
        print("Student Not found!")
            

    def delete_student(self):
        roll_no = input("Enter roll no of the student: ")
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                self.sv_student()
                print("Deletion Successful!")
                return
        print("Student not found!")




std = StudentManager()
while True:
    print("\n" + "=" * 40)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


    try:
        choice = input("Enter Choice : ")
    except ValueError:
        print("Invalid Value!")
        continue

    if choice == "1":
        std.add_student()

    elif choice == "2":
        std.view_student()

    elif choice == "3":
        std.search_student()
    
    elif choice == "4": 
        std.update_student()

    elif choice == "5" :
        std.delete_student()

    elif choice == "6":
        print("Thank You for Using!")
        break

    else:
        print("Invalid Choice")