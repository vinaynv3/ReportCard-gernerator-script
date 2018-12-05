import csv


def marks_csv():
    marks_list = []
    folder = '/home/vini/PycharmProjects/ReportCard/resources/backend-assessment/marks.csv'
    with open(folder, 'r') as file:
        read_csv = csv.reader(file, delimiter=',')
        next(read_csv,None)
        for row in read_csv:
            marks_list.append(row)
    return marks_list


print(marks_csv())

'''

folder = '/home/vini/PycharmProjects/ReportCard/resources/backend-assessment/courses.csv'
with open(folder, 'r') as file:
    readCSV = csv.reader(file, delimiter=',')
    for line in readCSV:
        print(line)

    print('\n')

folder = '/home/vini/PycharmProjects/ReportCard/resources/backend-assessment/students.csv'
with open(folder, 'r') as file:
    readCSV = csv.reader(file, delimiter=',')
    for line in readCSV:
        print(line)
    print('\n')

folder = '/home/vini/PycharmProjects/ReportCard/resources/backend-assessment/tests.csv'
with open(folder, 'r') as file:
    readCSV = csv.reader(file, delimiter=',')
    for line in readCSV:
        print(line)
    print('\n')

'''