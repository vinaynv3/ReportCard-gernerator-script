# modules
import csv
import os


# os module initializes file path folders from root directory to access csv files data
path = os.path.abspath('.')

# condition checks OS eg: Linux, OSX
if path[0] == '/':
    path = path + os.path.join('/csv_files/')

# Windows OS
else:
    path = path + os.path.join('\\csv_files\\')

# total csv_files
csv_files = ['courses.csv', 'tests.csv', 'marks.csv', 'students.csv']

# initialized variables names holds data from associated csv file
students = {}
courses = {}
course_teachers = {}
marks_data = []
tests_data = []

# loop collect data and assigns it to above associated csv file variable
for file in csv_files:

    with open(path + file, 'r') as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        # skipping header in csv file
        next(read_csv, None)

        # condition assigns data to courses and course_teacher dictionary
        if file == csv_files[0]:
            for data in read_csv:
                courses[data[0]] = data[1]
                course_teachers[data[1]] = data[2]

        # condition assigns data to students dictionary
        elif file == csv_files[3]:
            for data in read_csv:
                students[data[0]] = data[1]

        # condition assigns data to marks_data list
        elif file == csv_files[2]:
            for data in read_csv:
                marks_data.append(data)

        # condition assigns data to tests_data list
        elif file == csv_files[1]:
            for data in read_csv:
                tests_data.append(data)


text_file = open('report_card.txt', 'r+')
text_file.truncate(0)

# report card script starts
# loop calculate each student grades and their average dynamically
for name_id, name in students.items():

    # initialized variables names holds individual student details
    marks = {}
    total_percentage = 0
    total_courses = 0
    final_grade = []

    # collecting individual student marks
    for index in marks_data:
        if name_id == index[1]:
            marks[index[0]] = index[2]

    # collecting individual student course marks
    course_id = list(courses.keys())
    for course_name in course_id:

        # verify course weights
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

    # statements writes students report card final grades into text document

    text_file = open('report_card.txt', 'a')
    text_file.write('\n')
    text_file.write(("Student_Id:%s" % name_id) + " \tName:%s" % name)
    text_file.write('\n')
    text_file.write("Total Average:%s" % round(total_percentage, 2) + '%')
    text_file.write('\n\n')

    # statement block writes course grades and tests taken course names into text document
    grade = 0
    for c_id, c_teacher in course_teachers.items():
        # condition evaluates null values
        if final_grade[grade] != 0:
            text_file.write(("\t\t Course:%s" % c_id) + "\tTeacher:%s" % c_teacher)
            text_file.write('\n')
            text_file.write('\t\t Final Grade:\t%s' % final_grade[grade] + '%')
            text_file.write('\n\n')
        grade += 1

    # text_file.write('---------------------------------------------------------------')
    text_file.close()

# open report card text file

abs_path = os.path.abspath('.') + '/report_card.txt'
report_card = open(str(abs_path))
report = report_card.read()
print(report)

# opening final report card text document
# Linux
if abs_path[0] == '/':
    osCommandString = "gedit report_card.txt"
    os.system(osCommandString)
# Windows
else:
    osCommandString = "notepad.exe report_card.txt"
    os.system(osCommandString)
# THE END OF PYTHON SCRIPT

