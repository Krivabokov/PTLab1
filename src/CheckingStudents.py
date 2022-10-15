# -*- coding: utf-8 -*-
from Types import DataType
import random


class CheckingStudents:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.students: dict = []

    def check(self) -> str:
        number = 0
        for name in self.data:
            if self.data[name] == 100:
                self.students.insert(number, name)
        if len(self.students) == 0:
            return 0
        else:
            random_index = random.randint(0, len(self.students) - 1)
            return str(self.students[random_index])
