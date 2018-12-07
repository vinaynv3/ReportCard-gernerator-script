import csv
from decimal import Decimal

# _________________________________________________________________________________________________________

# Course CSV file directory folder
folder = '/home/vini/PycharmProjects/ReportCard/resources/courses.csv'

# test CSV file directory folder
folder2 = '/home/vini/PycharmProjects/ReportCard/resources/tests.csv'

# students CSV file directory folder
folder3 = '/home/vini/PycharmProjects/ReportCard/resources/students.csv'

# marks CSV file directory folder
folder4 = '/home/vini/PycharmProjects/ReportCard/resources/marks.csv'
# __________________________________________________________________________________________________________

# ___________________________________________________________________________________________________________

students = {}   # students csv data is assigned

# statement reads csv students data
with open(folder3, 'r') as file:
    read_csv_students = csv.reader(file, delimiter=',')

    # skipping header in csv file
    next(read_csv_students, None)

    # loop assigns key course_id and value course_name to course_details dictionary
    for data in read_csv_students:
        students[data[0]] = data[1]
# ----------------------------------------------------------

courses = {}    # course csv data is assigned
course_teachers = {}   # teachers csv data is assigned

# statement reads csv course data
with open(folder, 'r') as file:

    read_csv_course = csv.reader(file, delimiter=',')
    next(read_csv_course, None)

    # loop assigns key course_id and value course_name to course_details dictionary
    for data in read_csv_course:
        courses[data[0]] = data[1]
        course_teachers[data[1]] = data[2]
# -------------------------------------------------------------
marks_data = []  # marks csv data is assigned
tests_data = []  # tests csv data is assigned

# statement reads csv marks data
with open(folder4, 'r') as file:

    read_csv_marks = csv.reader(file, delimiter=',')
    next(read_csv_marks, None)

    for data in read_csv_marks:
        marks_data.append(data)
# -------------------------------------------------

# statement reads csv tests data
with open(folder2, 'r') as file:

    read_csv_tests = csv.reader(file, delimiter=',')
    next(read_csv_tests, None)

    # loop assigns key course_id and value course_name to course_details dictionary
    for data in read_csv_tests:
        tests_data.append(data)
# __________________________________________________________________________________________________________





'''
# breaking dictionary values into list
student_id = list(students.keys())
course_id = list(courses.keys())

# logic script starts
# loop calculate each student grades and their average dynamically
for name_id, name in students.items():

    marks = {}
    total_percentage = 0
    total_courses = 0
    final_grade = []

    # collecting individual student marks
    for index in marks_data:
        if name_id == index[1]:
            marks[index[0]] = index[2]

    print('STUDENT', name_id, 'Name: ', name)

    # collecting individual student course marks
    for course_name in course_id:

        course_weights = {}
        for course_test_id in tests_data:
            if course_name == course_test_id[1]:
                course_weights[course_test_id[0]] = course_test_id[2]

        # course average calculation
        course_total = 0

        for test_id, mark in marks.items():
            for test_no, grade_weight in course_weights.items():

                if test_id == test_no:
                    total = int(mark)*(int(grade_weight)*0.01)
                    course_total += total

        # rounding up decimal point to 1
        final_grade.append(round(course_total, 1))

        # adding each test averages
        total_percentage += course_total

        # counting total tests taken each student
        if course_total != 0:
            total_courses += 1

    # finally calculating student total percentage of marks
    total_percentage = total_percentage / float(total_courses)
    print(round(total_percentage, 2))
    print(final_grade, '\n')
    print("-----------------------------------------------------------------------")

    text_file = open('report_card.txt', 'a')
    text_file.write('\n')
    text_file.write(("Student_Id:%s" % name_id) + " Name:%s" % name)
    text_file.write('\n')
    text_file.write("Total Average:%s" % round(total_percentage, 2) + '%')
    text_file.write('\n\n')

    grade = 0
    for c_id, c_teacher in course_teachers.items():
        if final_grade[grade] != 0:
            text_file.write(("\t\t course:%s" % c_id) + "\tTeacher:%s" % c_teacher)
            text_file.write('\n')
            text_file.write('\t\t Final Grade:\t%s' % final_grade[grade] + '%')
            text_file.write('\n\n')
        grade += 1

    text_file.write('---------------------------------------------------------------')


'''





