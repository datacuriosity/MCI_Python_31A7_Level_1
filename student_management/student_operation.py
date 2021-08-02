from student import Student


class StudentOps:
    def __init__(self):
        self.student_li = []

    def add_one_student(self, student):
        if isinstance(student, Student):
            self.student_li.append(student)
        else:
            raise Exception('Please input an instance of class Student')

    def add_student_list(self, li):

        for student in li:
            self.add_one_student(student)

    def drop_student(self, student_id):
        index = 0
        for student in self.student_li:
            if student_id == student.student_id:
                self.student_li.pop(index)
            index += 1

    def edit_student_info(self, student_id, student_name=None):
        is_exist = False
        index = 0
        for student in self.student_li:
            if student_id == student.student_id:
                student.student_name = student_name
                is_exist = True
            index += 1

        if not is_exist:
            self.add_one_student(Student(student_id, student_name))

    def print_student_li_info(self):
        for student in self.student_li:
            print(f"Student ID: {student.student_id} with name: {student.student_name}")


if __name__ == '__main__':
    student_ops = StudentOps()
    student_li = [Student(1, 'Hong Anh'), Student(2, 'Loi Nguyen'), Student(3, 'Trung'), Student(4, 'Vu Dao'),
                  Student(5, 'Hau Pham'), Student(6, 'Hue Thieu'), Student(7, 'Hang Nguyen'), Student(8, 'Anh Duong')]
    student_ops.add_student_list(student_li)
    print('-'*50, 'BEFORE DROP', '-'*50)
    student_ops.print_student_li_info()

    print('-'*50, 'AFTER DROP', '-'*50)
    student_ops.drop_student(10)
    student_ops.print_student_li_info()

    print('-'*50, 'EDIT INFORMATION', '-'*50)
    student_ops.edit_student_info(10, student_name='Chuong Tran')
    student_ops.print_student_li_info()
