"""
Author: Alex Alvarado
Program: basic_IO.py
Date: 10-11-20
Desctiption: The program opens a text file and adds student information based on what the user inputs.
"""


FILE_NAME = 'student_info.txt'
MAX = 50

MIN = 1

IOERROR_MES = "Cannot open file on file system"

def write_to_file(*args):

    """
    :param args: accepts a tuple as an argument
    :returns : has no return because it writes to a text document
    """
    try:
        with open(FILE_NAME, 'a') as f:
            f.write('{}, {}:\t'.format(args[1], args[0]))
            for i in args[2]:
                f.write('{}\t'.format(i))
            f.write('\n')
    except IOError:
        print('Cannot open file on file system')


def get_student_info(**kwargs):
    """
    :param kwargs: accepts a tuple as an argument
    :return: returns nothing because it formats the string for the file
    """

    print("Welcome, {} {}!".format(kwargs['first_name'], kwargs['last_name']))
    scores = []
    num = 0
    while num != -1:
        try:
            num = float(input("Enter a score between {} and {}, (-1 to exit)".format(MIN, MAX)))
            if num == -1:
                break
            elif num < MIN or num > MAX:
                raise ValueError("Score must be between {} and {}".format(MIN, MAX))
            else:
                scores.append(num)
        except ValueError as err:
            print (err)
    all_scores = kwargs['first_name'], kwargs['last_name'], scores
    print(all_scores)
    write_to_file(kwargs['first_name'], kwargs['last_name'], scores)


    # num = float(input("Enter a score between {} and {}, (-1 to exit)".format(MIN, MAX))
def read_from_file():
    """
    :return: returns nothing because it reads the lines of the test file
    """
    try:
        with open(FILE_NAME, 'r') as f:
            read_line = f.read()
            print(read_line)
    except IOError:
        print(IOERROR_MES)




if __name__ == '__main__':
    get_student_info(first_name = 'Morgan', last_name='McCarley')
    get_student_info(first_name = 'Marco', last_name = 'Polo')
    input("hold.....")
    read_from_file()
    input('Press any key to end')
