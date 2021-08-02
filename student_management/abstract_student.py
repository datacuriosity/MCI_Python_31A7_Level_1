from abc import ABC, abstractmethod  # Abstract- Based Class

# Class: frame for many instance
# Instance: specific object for a Class


class AbstractStudent(ABC):
    """
    Abstract class could not initiate constructor. No any data
    """

    # def __init__(self, student_id, student_name):  # Constructor
    #     self.student_id = student_id
    #     self.student_name = student_name

    @abstractmethod
    def get_student_name(self):
        pass

    @abstractmethod
    def get_student_id(self):
        pass


# if __name__ == '__main__':

    # student_1 = AbstractStudent(1, 'Nguyen Truong')
    # student_2 = AbstractStudent(1, 'Anh')
    # student_3 = AbstractStudent(3, 'Chuong')
    # student_4 = AbstractStudent(4, 'Trung')
    #
    # print(student_1)

    # Compile-time error
    # Run-time error
