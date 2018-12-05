import csv

# Course CSV file directory folder
folder = '/home/vini/PycharmProjects/ReportCard/resources/courses.csv'

# Tests CSV file directory folder
folder2 = '/home/vini/PycharmProjects/ReportCard/resources/tests.csv'

# Total subjects
course = {}

# Test weight
tests = {}


with open(folder, 'r') as file:
    readCSV = csv.reader(file, delimiter=',')
    for line in readCSV:
        print(line)
    print('\n')


def courses():
    with open(folder, 'r') as file:
        read_csv = csv.reader(file, delimiter=',')
        next(read_csv,None)
        for id in read_csv:
            course[id[0]] = id[1]
        print(course)


# Course Function
courses()

# Structuring course id and test id dictionary values into List
test_id = list(course.keys())
test_course = list(course.values())

# Debugging
print(test_id)
print(test_course)



'''
Warning: Coded function is not scalable
TODO: work scalability and optimization

'''


def test_id_weight():

    biology = {}
    history = {}
    maths = {}

    with open(folder2, 'r') as file:
        read_csv = csv.reader(file, delimiter=',')
        next(read_csv,None)

        for id in read_csv:

            if test_id[0] == id[1]:
                biology[id[0]] = id[2]

            elif test_id[1] == id[1]:
                history[id[0]] = id[2]

            else:
                maths[id[0]] = id[2]

    print(biology, '\n', history, '\n', maths)


test_id_weight()


