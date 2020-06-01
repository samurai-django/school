from django.db import models
from account.models import Account
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.core.validators import FileExtensionValidator


SUBJECT_CHOICES = (
    ('Math', 'Math'),
    ('English', 'English'),
    ('Science', 'Science'),
    ('PE', 'PE'),
    ('Geography', 'Geography'),
    ('physics', 'Physics'),

)

GRADE_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),

)
SEMESTER_CHOICES = (
    ('Q1', 'Q1'),
    ('Q2', 'Q2'),
    ('Q3', 'Q3'),
    ('Q4', 'Q4'),
    ('summer vacation', 'summer vacation'),
    ('winter vacation', 'winter vacation'),

)

class Course(models.Model):
    course_name = models.CharField(max_length=50, null=False, blank=False, unique=True, error_messages={'unique':"This course_name has been used, please use other course_name"})
    name = models.ForeignKey(Account, models.CASCADE, default=False)
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=20, default=False)
    abstract = models.CharField(verbose_name='abstract', max_length=100)
    subjects = models.CharField(choices=SUBJECT_CHOICES, max_length=20, default=False)
    grades = models.CharField(choices=GRADE_CHOICES, default=False, max_length=1)
    slug = models.SlugField()
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1}'.format(str(self.course_name), str(self.name.username))




class CourseDetail(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, default=False)
    number = models.IntegerField()

    pdf_file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['pdf', ])],
        blank=True,
        null=True,
       )
    # number = models.IntegerField(unique=True, error_messages={'unique':"You have already created , please use other number of this course"})

    def __str__(self):
        return '{0} - {1} - {2}'.format(str(self.course.name.username), str(self.course.course_name), str(self.number))

class Test(models.Model):
    test_name = models.CharField(max_length=50, null=False, blank=False)
    test_course = models.OneToOneField(CourseDetail, models.CASCADE, default=False)
    test_file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='テストファイル',
        validators=[FileExtensionValidator(['pdf', ])],
        blank=True,
        null=True,
       )
    def __str__(self):
        return '{0} - {1}'.format(str(self.test_name), str(self.test_course.course.course_name))


class SectionTest(models.Model):
    section_test_name = models.CharField(max_length=50, null=False, blank=False)
    section_test_course = models.OneToOneField(Course, models.CASCADE, default=False)
    test_file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='章末テストファイル',
        validators=[FileExtensionValidator(['pdf', ])],
        blank=True,
        null=True,
    )


class FinalTest(models.Model):
    final_test_name = models.CharField(max_length=50, null=False, blank=False)
    final_test_course = models.OneToOneField(Course, models.CASCADE, default=False)
    test_file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='修了テストファイル',
        validators=[FileExtensionValidator(['pdf', ])],
        blank=True,
        null=True,
    )

class RegisterCourse(models.Model):
    student_name = models.ForeignKey(Account, models.CASCADE, default=False)
    complete = models.BooleanField(default=False)

class MyCourse(models.Model):
    name = models.ForeignKey(RegisterCourse, models.CASCADE, default=False)
    course = models.ForeignKey(Course, models.CASCADE, default=False)
    is_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} - {1}'.format(str(self.name.student_name.username), str(self.is_add))

class MidMyCourse(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, default=False)
    my_course = models.ForeignKey(MyCourse, models.CASCADE, default=False)


class Result(models.Model):
    student = models.ForeignKey(Account, models.CASCADE, default=False)
    course = models.ForeignKey(Test, models.CASCADE, default=False)
    is_score = models.PositiveIntegerField(default=False)
    result_file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='テスト結果',
        validators=[FileExtensionValidator(['pdf', ])],
        null=False,
        blank=False,
        default=False,
       )

    def __str__(self):
        return str(self.is_score)