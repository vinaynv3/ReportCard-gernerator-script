
import csv

# ______________________________________________________________________________

# Course CSV file directory folder
folder = '/home/vini/PycharmProjects/ReportCard/resources/courses.csv'

# test CSV file directory folder
folder2 = '/home/vini/PycharmProjects/ReportCard/resources/tests.csv'

# students CSV file directory folder
folder3 = '/home/vini/PycharmProjects/ReportCard/resources/students.csv'

# marks CSV file directory folder
folder4 = '/home/vini/PycharmProjects/ReportCard/resources/marks.csv'

# ________________________________________________________________________________


# Report card class
class ReportCard:
    def __init__(self):
        self.course_details = {}
        self.test_details = {}
        self.course_id = None
        self.course_name = None
        self.students = {}

    # function return course_name and course_id
    def courses(self):

        # statement reads csv course data
        with open(folder, 'r') as file:
            read_csv = csv.reader(file, delimiter=',')

            # skipping header in csv file
            next(read_csv, None)

            # loop assigns key course_id and value course_name to course_details dictionary
            for data in read_csv:
                self.course_details[data[0]] = data[1]

        # creating lists for course_id and course_name
        self.course_id = list(self.course_details.keys())
        self.course_name = list(self.course_details.values())

        return self.course_details

    # function returns student_name and student_id
    def student_id(self):

        # statement reads csv course data
        with open(folder3, 'r') as file:
            read_csv = csv.reader(file, delimiter=',')

            # skipping header in csv file
            next(read_csv, None)

            # loop assigns key students_id and value students_name to students dictionary
            for data in read_csv:
                self.students[data[0]] = data[1]

        return self.students

    # function returns marks and test_id
    def marks(self):

        # statement reads csv course data
        with open(folder4, 'r') as file:
            read_csv = csv.reader(file, delimiter=',')

            # skipping header in csv file
            next(read_csv, None)

            for d in read_csv:
                print(d)

    # function returns course id and course weight
    def course_test_id_and_weight(self):

        bio, hist, math = {}, {}, {}

        with open(folder2, 'r') as file:
            read_csv = csv.reader(file, delimiter=',')
            next(read_csv, None)

            for id in self.course_id:
                print(id)
                for val in read_csv:
                    if id == val[1]:
                        bio[val[0]] = val[2]

            for id in self.course_id:
                print(id)
                if id == '2':
                    hist[val[0]] = val[2]

        print(bio, hist)


test = ReportCard()
print(test.courses())
# print(test.course_test_id_and_weight())
print(test.student_id())
