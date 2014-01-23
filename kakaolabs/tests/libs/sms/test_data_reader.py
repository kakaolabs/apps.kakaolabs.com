# -*- coding: utf-8 -*

import unittest

from libs.sms.data_reader import DataReader


class TestDataReader(unittest.TestCase):
    def test_parser_category(self):
        filepath = 'databases/sms/xin-loi'
        reader = DataReader(filepath)
        reader.parse()
        categories = [
            "SMS xin lỗi bạn bè, người yêu",
            "8 câu xin lỗi bạn trai hiệu quả nhất"
        ]

        self.assertEquals(
            sorted(categories),
            sorted(reader.contents.keys()))

    def test_parse_content(self):
        filepath = 'databases/sms/lam-quen'
        reader = DataReader(filepath)
        reader.parse()
        smscontents = [
            "Liệu cha của em có phải là một tay trộm hay không? Vì ông ấy đã lấy cắp những vì sao trên trời và đưa chúng vào mắt em.",
            "Khi ngã từ thiên đường xuống trần gian em có đau không?",
            "Hẳn là em đã mỏi nhừ, vì em chạy trong tâm trí anh suốt cả ngày.",
            "Xin lỗi tôi đã làm mất số điện thoại của mình. Tôi có thể mượn số của cô được không?",
            "Cô có tin vào tình yêu từ cái nhìn đầu tiên không, hay để tôi đi qua một lần nữa?",
            "Xin lỗi cô, cô có hôn người lạ không? Không à? Vậy thì hãy để tôi tự giới thiệu nhé.",
            "Chân em có đau khi chạy suốt đêm trong giấc mơ của anh không?",
            "Tôi mới tới thành phố này. Liệu em có thể chỉ dẫn cho tôi đến căn hộ của em được không?",
            "Xin hỏi cô có bản đồ không? Tôi cứ bị lạc hoài trong đôi mắt cô.",
            "Điều duy nhất đôi mắt em chưa nói cho anh biết là tên của em.",
        ]
        category_name = "Những tin nhắn làm quen, sms làm quen hài hước và lãng mạn"

        self.assertEquals(
            sorted(smscontents),
            sorted(reader.contents[category_name]))
