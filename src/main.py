# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from CheckingStudents import CheckingStudents
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    if 'xml' in path:
        reader = XmlDataReader()
    else:
        reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()

    print('\nПроверка студентов, имеющих 100 баллов по всем дисциплинам:')
    if CheckingStudents(rating).check():
        print('   Студент ' + CheckingStudents(rating).check() +
              ' имеет 100 баллов по всем дисциплинам')
    else:
        print('   Студенты, имеющие 100 баллов по всем дисциплинам '
              'отсутствуют')


if __name__ == "__main__":
    main()
