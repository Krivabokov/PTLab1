# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XmlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()
        i = 0
        for elem in root:
            self.key = elem.attrib.get('name')
            self.students[self.key] = []
            for j in range(len(root[i])):
                subj = root[i][j].tag
                score = root[i][j].text
                self.students[self.key].append((subj, int(score)))
            i += 1
        return self.students
