import unittest

from libs.sms.data_reader import DataReader


class TestDataReader(unittest.TestCase):
    def test_parser(self):
        filepath = 'database/sms/hai-huoc'
        parser = DataReader(filepath)
