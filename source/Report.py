
import csv

# Course CSV file directory folder
folder = '/home/vini/PycharmProjects/ReportCard/resources/courses.csv'

# Tests CSV file directory folder
folder2 = '/home/vini/PycharmProjects/ReportCard/resources/tests.csv'


# Report card class
class ReportCard:
    def __init__(self):
        self.course_details = {}
        self.test_details = {}
        self.course_id = None
        self.course_name = None

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

    # function returns course id and course weight
    def course_test_id_and_weight(self):

            with open(folder2, 'r') as file:
                read_csv = csv.reader(file, delimiter=',')
                next(read_csv, None)

                for val in read_csv:
                    print(val)

                    if self.course_id[0] == val[1]:
                        self.course_name[int(val[0])] = val[2]
                        print(self.course_name[0])

                '''
                    elif self.course_id[1] == id[1]:
                        history[id[0]] = id[2]

                    else:
                        maths[id[0]] = id[2]
        
                '''
        return self.course_name[0]


test = ReportCard()
print(test.courses())
print(test.course_test_id_and_weight())

