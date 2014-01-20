from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

from kakaolabs.libs import utils


class MemberManager(BaseUserManager):
    def create_member(self, username, email, password):

        # create new member
        member = self.get_query_set().create(
            username=username, password=make_password(password), email=email)

        return member


class Member(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    # app
    class Meta:
        app_label = 'core'

    # member manager
    objects = MemberManager()

    # fields for AbstractBaseUser
    username = models.CharField(max_length=200, unique=True, db_index=True, null=True)
    email = models.EmailField(max_length=254, unique=True, db_index=True, null=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_joined = models.DateTimeField(auto_now_add=True, db_index=True)
    api_key = models.CharField(max_length=60, default=utils.generate_uuid)
    api_secret = models.CharField(max_length=60, default=utils.generate_uuid)

    # methods for AbstractBaseUser
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin
