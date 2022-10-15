# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n" + \
               "<root>\n" + \
               "    <person name=\"Иванов Иван Иванович\">\n" + \
               "        <математика>67</математика>\n" + \
               "        <литература>100</литература>\n" + \
               "        <программирование>91</программирование>\n" + \
               "    </person>\n" + \
               "    <person name=\"Петров Петр Петрович\">\n" + \
               "        <математика>78</математика>\n" + \
               "        <химия>87</химия>\n" + \
               "        <социология>61</социология>\n" + \
               "    </person>\n" + \
               "</root>\n"

        data = {
            "Иванов Иван Иванович": [
                ("математика", 67), ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ('математика', 78), ('химия', 87), ('социология', 61)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
