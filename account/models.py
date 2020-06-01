from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import datetime


# [2]
class MyAccountManager(BaseUserManager):


    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an email username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# [1]

class Account(AbstractBaseUser):

    # {% email, username, date_joined, ... , is_superuser  ここに何かを付け加えることはできるがここまでは記述しなければならない%　}

    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Multiple User
    is_superuser = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    # first_name      =models.CharField(max_length=30) 付け加えてもよい

    # Image
    image = models.ImageField(upload_to='profile_pic', default='default.jpg')

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
# REQUIRED_FIELDS = ['username', 'first_name', ] 付け加えた場合
# [3] MyAccountManager　呼び
# [4] settings.py へ行き
# AUTH_USER_MODELを設定 'account.Account
# ディスプレイしたもの

    def __str_(self):
        return self.email

# ここから先はコピーすればよい

    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True


    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_is_teacher_count(self):
        return Account.objects.filter(is_teacher=True).count()

    def get_is_student_count(self):
        return Account.objects.filter(is_student=True).count()


class MessageToStudent(models.Model):
    title = models.CharField(verbose_name='title', max_length=30)
    date = models.DateField(verbose_name='date', auto_now_add=True)
    content = models.CharField(verbose_name='content', max_length=255)

    # message = models.ForeignKey(to=Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




