import csv
import os


path = os.path.join('/home', 'vini', 'PycharmProjects', 'ReportCard', 'resources/')
csv_files = ['courses.csv', 'tests.csv', 'marks.csv', 'students.csv']

students = {}
courses = {}
course_teachers = {}
marks_data = []  # marks csv data is assigned
tests_data = []  # tests csv data is assigned


for file in csv_files:

    with open(path + file, 'r') as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')

        # skipping header in csv file
        next(read_csv, None)

        # loop assigns key course_id and value course_name to course_details dictionary
        if file == csv_files[0]:
            for data in read_csv:
                courses[data[0]] = data[1]
                course_teachers[data[1]] = data[2]
        elif file == csv_files[3]:
            for data in read_csv:
                students[data[0]] = data[1]
        elif file == csv_files[2]:
            for data in read_csv:
                marks_data.append(data)
        elif file == csv_files[1]:
            for data in read_csv:
                tests_data.append(data)


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
    course_id = list(courses.keys())
    for course_name in course_id:

        course_weights = {}
        for course_test_id in tests_data:
            if course_name == course_test_id[1]:
                course_weights[course_test_id[0]] = course_test_id[2]

        course_total = 0
        # course average calculation
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

    # calculating student total percentage of marks
    total_percentage = total_percentage / float(total_courses)

    '''
    # Debugging 
    print(round(total_percentage, 2))
    print(final_grade, '\n')
    print("-----------------------------------------------------------------------")
    '''
    # statements writes students report card final grades into test document
    text_file = open('report_card.txt', 'a')
    text_file.write('\n')
    text_file.write(("Student_Id:%s" % name_id) + " Name:%s" % name)
    text_file.write('\n')
    text_file.write("Total Average:%s" % round(total_percentage, 2) + '%')
    text_file.write('\n\n')

    # statement block writes course grades and tests taken course names into text document
    grade = 0
    for c_id, c_teacher in course_teachers.items():
        # condition evaluates null values
        if final_grade[grade] != 0:
            text_file.write(("\t\t course:%s" % c_id) + "\tTeacher:%s" % c_teacher)
            text_file.write('\n')
            text_file.write('\t\t Final Grade:\t%s' % final_grade[grade] + '%')
            text_file.write('\n\n')
        grade += 1

    text_file.write('---------------------------------------------------------------')

# THE END OF PYTHON SCRIPT

