# -*- coding: utf-8 -*

import sqlite3

from django.core.management.base import BaseCommand

from sms.models import Category, SMSContent


CATEGORIES = [
    "Tình yêu",
    "Chúc mừng sinh nhật",
    "Chào buổi sáng",
    "Chúc ngủ ngon",
    "Chúc mừng năm mới",
    "Valentine",
    "Chúc mừng 8-3",
    "Mùa thi",
    "Chúc mừng 20-10",
    "Giáng sinh",
    "Hình cute",
    None,
    "Khác"
]


class Command(BaseCommand):
    help = "insert data from sms cute"

    def insert_categories_if_needed(self):
        self.categories = {}
        for item in CATEGORIES:
            if not item:
                continue

            if not Category.objects.filter(name=item, type=Category.CATEGORY).count():
                print "create subcategory %s" % item
                category = Category.objects.create(
                    name=item, type=Category.SUBCATEGORY)
            else:
                print "create subcategory Khác for %s" % item
                parent = Category.objects.get(name=item, type=Category.CATEGORY)
                category = Category.objects.create(
                    name="Khác", type=Category.SUBCATEGORY, parent=parent)
            self.categories[item] = category

    def insert_data(self):
        conn = sqlite3.connect("databases/kutesms.sqlite")
        c = conn.cursor()
        c.execute("SELECT catId, content FROM sms")

        for row in c:
            category_index = row[0]
            category = self.categories[CATEGORIES[category_index]]
            content = row[1]
            SMSContent.objects.create(content=content, category=category)


    def handle(self, *args, **options):
        self.insert_categories_if_needed()
        self.insert_data()
