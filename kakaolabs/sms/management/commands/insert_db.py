# -*- coding: utf-8 -*

from django.core.management.base import BaseCommand

from libs import language
from sms.models import Category, SMSContent


class Command(BaseCommand):
    help = "insert data to sms"

    def clear_data(self):
        Category.objects.all().delete()
        SMSContent.objects.all().delete()

    def insert_data_to_category(self, name):
        eng_name = language.convert_vietnamese_to_english(name)
        normalize_name = eng_name.replace(" ", "-")
        filepath = "databases/sms/%s" % normalize_name
        print filepath

    def insert_data(self):
        CATEGORIES = [
            "bạn bè", "buổi sáng", "chọc phá", "chúc mừng 20-10",
            "chúc mừng 8-3", "chúc mừng năm mới",
            "chúc mừng sinh nhât", "chúc ngủ ngon", "doạ ma",
            "giáng sinh", "hài hước", "làm quen", "tình yêu",
            "tỏ tình", "trung thu", "valentine", "xin lỗi"]

        for item in CATEGORIES:
            category_name = "%s%s" % (item[0].upper(), item[1:])
            Category.objects.create(name=category_name, type=Category.CATEGORY)
            self.insert_data_to_category(item)

    def handle(self, *args, **options):
        self.clear_data()
        self.insert_data()
