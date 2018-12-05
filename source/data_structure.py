import csv


def marks_csv():
    mlist = []
    folder = '/home/vini/PycharmProjects/ReportCard/resources/marks.csv'
    with open(folder, 'r') as file:
        read_csv = csv.reader(file, delimiter=',')
        next(read_csv,None)
        for row in read_csv:
            mlist.append(row)

    return mlist


def marks(marks_list):

    # separating data according to test_id and course_id
    bio, hist, math = [], [], []
    for data in marks_list:
        if data[1] == '1':
           bio.append(data)
        elif data[1] == '2':
            hist.append(data)
        else:
            math.append(data)

    return bio, hist, math


if __name__ == '__main__':
    marks_list = marks_csv()
    result = marks(marks_list)
    print('\tStudent A\n\t--------')
    for data in result[0]:
        print(data)
    print('\n\tStudent B\n\t--------')
    for data in result[1]:
        print(data)
    print('\n\tStudent C\n\t--------')
    for data in result[2]:
        print(data)





