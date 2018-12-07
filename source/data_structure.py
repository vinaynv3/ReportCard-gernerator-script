import csv

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
teachers = {}   # teachers csv data is assigned

# statement reads csv course data
with open(folder, 'r') as file:

    read_csv_course = csv.reader(file, delimiter=',')
    next(read_csv_course, None)

    # loop assigns key course_id and value course_name to course_details dictionary
    for data in read_csv_course:
        courses[data[0]] = data[1]
        teachers[data[0]] = data[2]
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

# breaking dictionary values into list
student_id = list(students.keys())
course_id = list(courses.keys())

# logic script starts
# loop calculate each student grades and their average dynamically
for name_id in student_id:

    marks = {}
    total_percentage = 0
    total_courses = 0

    # collecting individual student marks
    for index in marks_data:
        if name_id == index[1]:
            marks[index[0]] = index[2]

    print('STUDENT', name_id)

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
        print(course_total)

        # adding each test averages
        total_percentage += course_total

        # counting total tests taken each student
        if course_total != 0:
            total_courses += 1

    # finally calculating student total percentage of marks
    total_percentage = total_percentage / float(total_courses)
    print(total_percentage)
    print("-----------------------------------------------------------------------")









