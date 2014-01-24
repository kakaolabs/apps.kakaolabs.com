# -*- coding: utf-8 -*

import sqlite3

from django.core.management.base import BaseCommand

from sms.models import Category, SMSContent


class Command(BaseCommand):
    help = "insert data from sms cute"

    def insert_categories_if_needed(self):
        pass

    def insert_data(self):
        pass

    def handle(self, *args, **options):
        self.insert_categories_if_needed()
        self.insert_data()
