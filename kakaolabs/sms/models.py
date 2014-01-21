from django.db import models


class Category(models.Model):

    CATEGORY, SUBCATEGORY = xrange(0, 2)
    CATEGORY_TYPE_CHOICES = (
        (CATEGORY, 'category'),
        (SUBCATEGORY, 'subcategory'),
    )

    name = models.CharField(max_length=200, db_index=True)
    type = models.SmallIntegerField(choices=CATEGORY_TYPE_CHOICES, default=SUBCATEGORY, db_index=True)
    parent = models.ForeignKey('Category', null=True, blank=True, related_name='children')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    @property
    def data(self):
        return self.children

    def __unicode__(self):
        return self.name


class SMSContent(models.Model):
    category = models.ForeignKey('Category', related_name='sms')
    content = models.TextField()
    votes = models.IntegerField(default=0, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
