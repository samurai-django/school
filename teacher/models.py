
from django.db import models
from account.models import Account
from classroom.models import Class

from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class TeacherFunction(models.Model):

    title = models.CharField(verbose_name='title', max_length=30)
    # pub_date = models.DateField(verbose_name='pub_date', blank=True, default=timezone.now)
    date = models.DateField(verbose_name='date', default=timezone.now)

    content = models.CharField(verbose_name='content', max_length=255)

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    #
    # def publish(self):
    #     self.pub_date = timezone.now()
    #     self.save()
    def __str__(self):
        return self.title


class Course(models.Model):

    # teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    # semester = models.CharField(choices=SEMESTER_CHOICES, max_length=20, default=False)
    abstract = models.CharField(verbose_name='abstract', max_length=100)
    # subjects = models.CharField(choices=SUBJECT_CHOICES, max_length=20, default=False)
    # grades = models.CharField(choices=GRADE_CHOICES, default=False, max_length=1)
    slug = models.SlugField()
    is_registered = models.BooleanField(default=False)

class TeacherModel(models.Model):

    teacher = models.OneToOneField(User, on_delete=models.CASCADE, default=False)
    add_course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.teacher.username



