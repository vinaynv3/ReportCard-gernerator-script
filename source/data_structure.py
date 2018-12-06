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


students = {}

courses = {}

teachers = {}

# statement reads csv students data
with open(folder3, 'r') as file:
    read_csv = csv.reader(file, delimiter=',')

    # skipping header in csv file
    next(read_csv, None)

    # loop assigns key course_id and value course_name to course_details dictionary
    for data in read_csv:
        students[data[0]] = data[1]

# statement reads csv course data
with open(folder, 'r') as file:
    read_csv = csv.reader(file, delimiter=',')

    # skipping header in csv file
    next(read_csv, None)

    # loop assigns key course_id and value course_name to course_details dictionary
    for data in read_csv:
        courses[data[0]] = data[1]
        teachers[data[0]] = data[2]

# Debugging
# print(students, courses, teachers)

'''
Script: loops will iterate data to handle scalability issues in csv files
Approach: Dynamic
TODO: implement average and percentile calculation 

'''

student_id = list(students.keys())
course_id = list(courses.keys())
marks_data = []
tests_data = []

# statement reads csv marks data
with open(folder4, 'r') as file:
    read_csv_marks = csv.reader(file, delimiter=',')

    # skipping header in csv file
    next(read_csv_marks, None)

    for data in read_csv_marks:
        marks_data.append(data)

# Debugging

# statement reads csv tests data
with open(folder2, 'r') as file:
    read_csv_tests = csv.reader(file, delimiter=',')

    # skipping header in csv file
    next(read_csv_tests, None)

    # loop assigns key course_id and value course_name to course_details dictionary
    for data in read_csv_tests:
        tests_data.append(data)

# for i in tests_data:
#    print(i)


for name_id in student_id:
    marks = {}

    # collecting individual student marks
    for index in marks_data:
        if name_id == index[1]:
            marks[index[0]] = index[2]

    print('--------')
    # print(marks)
    # collecting individual student course marks
    for course_name in course_id:
        course_weights = {}
        for course_test_id in tests_data:
            if course_name == course_test_id[1]:
                course_weights[course_test_id[0]] = course_test_id[2]
        # print(course_weights)

        # single course average calculation
        total_percentage = 0
        count = 0
        course_total = 0
        for key, val in marks.items():

            for i, j in course_weights.items():

                if key == i:
                    total = int(val)*(int(j)*0.01)
                    course_total += total
                    count += 1
        print(course_total)











