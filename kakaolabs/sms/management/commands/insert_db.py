# -*- coding: utf-8 -*

from django.core.management.base import BaseCommand

from libs import language
from libs.sms.data_reader import DataReader
from sms.models import Category, SMSContent


class Command(BaseCommand):
    help = "insert data to sms"

    def clear_data(self):
        Category.objects.all().delete()
        SMSContent.objects.all().delete()

    def insert_data_to_category(self, category):
        eng_name = language.convert_vietnamese_to_english(category.name)
        normalize_name = eng_name.replace(" ", "-")
        name = "%s%s" % (normalize_name[0].lower(), normalize_name[1:])
        filepath = "databases/sms/%s" % name
        print filepath
        reader = DataReader(filepath)
        reader.parse()
        for name, data in reader.contents.iteritems():
            sub_category = Category.objects.create(
                    parent=category, name=name, type=Category.SUBCATEGORY)
            for item in data:
                SMSContent.objects.create(category=sub_category, content=item)


    def insert_data(self):
        CATEGORIES = [
            "bạn bè", "buổi sáng", "chọc phá", "chúc mừng 20-10",
            "chúc mừng 8-3", "chúc mừng năm mới",
            "chúc mừng sinh nhật", "chúc ngủ ngon", "doạ ma",
            "giáng sinh", "hài hước", "làm quen", "tình yêu",
            "tỏ tình", "trung thu", "valentine", "xin lỗi"]

        for item in CATEGORIES:
            category_name = "%s%s" % (item[0].upper(), item[1:])
            category = Category.objects.create(name=category_name, type=Category.CATEGORY)
            self.insert_data_to_category(category)

    def handle(self, *args, **options):
        self.clear_data()
        self.insert_data()
