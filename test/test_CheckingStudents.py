# -*- coding: utf-8 -*-
from src.CheckingStudents import CheckingStudents
import pytest

RatingsType = dict[str, float]


class TestCheckingStudents:

    @pytest.fixture()
    def input_data(self) -> tuple[RatingsType, str]:
        data: RatingsType = {
            "Абрамов Петр Сергеевич": 100,
            "Петров Игорь Владимирович": 79
        }

        student: str = "Абрамов Петр Сергеевич"

        return data, student

    def test_init_checking_students(self, input_data: tuple[RatingsType, str])\
            -> None:

        checking_students = CheckingStudents(input_data[0])
        assert input_data[0] == checking_students.data

    def test_check(self, input_data: tuple[RatingsType, str]) -> None:

        stud = CheckingStudents(input_data[0]).check()
        assert pytest.approx(stud) == input_data[1]
