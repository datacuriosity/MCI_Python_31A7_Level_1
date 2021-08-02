from abstract_student import AbstractStudent


class Student(AbstractStudent):

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_list = {'student_id': student_id, 'student_name': student_name}

    def get_student_name(self): # Overwrite
        """
        Get student name

        :return: str - student name
        """
        return self.student_name

    def get_student_id(self): # Overwrite
        return self.student_id

    def get_student_info(self):
        return self.student_list


if __name__ == '__main__':
    student_1 = Student(1, 'Truong')
    student_2 = Student(2, 'Trung')
    student_3 = Student(3, 'Anh')
