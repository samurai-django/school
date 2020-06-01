from django.db import models
from account.models import Account
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.core.validators import FileExtensionValidator

User = get_user_model()

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

class Class(models.Model):

    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=20, default=False)
    abstract = models.CharField(verbose_name='abstract', max_length=100)
    subjects = models.CharField(choices=SUBJECT_CHOICES, max_length=20, default=False)
    grades = models.CharField(choices=GRADE_CHOICES, default=False, max_length=100)
    slug = models.SlugField()
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.teacher.username, self.abstract)

    def get_absolute_url(self):
        return reverse("classroom:detail_class", kwargs={
            'slug': self.slug
        })

class ClassDetail(models.Model):
    name = models.CharField(choices=SEMESTER_CHOICES, max_length=20, default=False)
    is_class = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    pdf_file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['pdf', ])],
       )

    def __str__(self):
        # return str(self.pdf_file)
        return '{0} - {1}'.format(self.name, str(self.pdf_file))


class Register(models.Model):

    students = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    register = models.ManyToManyField(Class)
    is_date = models.DateField(auto_now_add=True)
    is_registered = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.students.email, self.is_registered)


# intermidiate
class Relationship(models.Model):
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, default=False)
    register = models.ForeignKey(Register, on_delete=models.CASCADE, default=False)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.classes.teacher.username, self.register.students.username)

class Relationship2(models.Model):
    students = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, default=False)
    is_registered = models.BooleanField(default=False)
    is_date = models.DateField(auto_now_add=True)

    slug = models.SlugField

    def __str__(self):
        return reverse('classroom:student_detail', kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return '{0} - {1}'.format(self.classes.teacher.username, self.students.username)











#
# class Course(models.Model):
#     course_name = models.CharField(max_length=50, null=False, blank=False)
#     name = models.ForeignKey(User, models.CASCADE, default=False)
#     semester = models.CharField(choices=SEMESTER_CHOICES, max_length=20, default=False)
#     abstract = models.CharField(verbose_name='abstract', max_length=100)
#     subjects = models.CharField(choices=SUBJECT_CHOICES, max_length=20, default=False)
#     grades = models.CharField(choices=GRADE_CHOICES, default=False, max_length=1)
#     slug = models.SlugField()
#     is_registered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return '{0} - {1}'.format(str(self.course_name), str(self.name.name))
#
#
# class CourseDetail(models.Model):
#     course = models.ForeignKey(Course, models.CASCADE, default=False)
#     number = models.IntegerField()
#     pdf_file = models.FileField(
#         upload_to='uploads/%Y/%m/%d/',
#         verbose_name='添付ファイル',
#         validators=[FileExtensionValidator(['pdf', ])],
#         blank=True,
#         null=True,
#        )
#
#     def __str__(self):
#         return '{0} - {1} - {2}'.format(str(self.course.name.name), str(self.course.course_name), str(self.number))
#
# class Test(models.Model):
#     test_name = models.CharField(max_length=50, null=False, blank=False)
#     test_course = models.OneToOneField(CourseDetail, models.CASCADE, default=False)
#     test_file = models.FileField(
#         upload_to='uploads/%Y/%m/%d/',
#         verbose_name='テストファイル',
#         validators=[FileExtensionValidator(['pdf', ])],
#         blank=True,
#         null=True,
#        )
#     def __str__(self):
#         return '{0} - {1}'.format(str(self.test_name), str(self.test_course.course.course_name))
#
#
# class SectionTest(models.Model):
#     section_test_name = models.CharField(max_length=50, null=False, blank=False)
#     section_test_course = models.OneToOneField(Course, models.CASCADE, default=False)
#     test_file = models.FileField(
#         upload_to='uploads/%Y/%m/%d/',
#         verbose_name='章末テストファイル',
#         validators=[FileExtensionValidator(['pdf', ])],
#         blank=True,
#         null=True,
#     )
#
#
# class FinalTest(models.Model):
#     final_test_name = models.CharField(max_length=50, null=False, blank=False)
#     final_test_course = models.OneToOneField(Course, models.CASCADE, default=False)
#     test_file = models.FileField(
#         upload_to='uploads/%Y/%m/%d/',
#         verbose_name='修了テストファイル',
#         validators=[FileExtensionValidator(['pdf', ])],
#         blank=True,
#         null=True,
#     )
#
#
#
# class MyCourse(models.Model):
#     name = models.ForeignKey(User, models.CASCADE, default=False)
#     course = models.ManyToManyField(Course)
#     is_add = models.DateTimeField(auto_now_add=True)
#     is_course_registered = models.BooleanField(default=False)
#
#
#     def __str__(self):
#         return '{0} - {1}'.format(str(self.name.name.email), str(self.is_add))
#
#
#
# class MidMyCourse(models.Model):
#     course = models.ForeignKey(Course, models.CASCADE, default=False)
#     my_course = models.ForeignKey(MyCourse, models.CASCADE, default=False)
#
#
#
# class Result(models.Model):
#     student = models.ForeignKey(User, models.CASCADE, default=False)
#     course = models.ForeignKey(Test, models.CASCADE, default=False)
#     is_score = models.PositiveIntegerField(default=False)
#     result_file = models.FileField(
#         upload_to='uploads/%Y/%m/%d/',
#         verbose_name='テスト結果',
#         validators=[FileExtensionValidator(['pdf', ])],
#         null=False,
#         blank=False,
#         default=False,
#        )
#
#     def __str__(self):
#         return str(self.is_score)
#
