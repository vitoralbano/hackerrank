#!/user/bin/python
# -*- coding: utf-8 -*-

import math


def gradingStudents(grades):
    for index in range(len(grades)):
        grade = grades[index]
        if grade > 40:
            rem = grade % 5
            print(rem)
            if rem < 3:
                grade = math.ceil(grade / 5) * 5
                print(grade)
                grades[index] = grade
    
    print(grades)


gradingStudents([73, 67, 38, 33])
