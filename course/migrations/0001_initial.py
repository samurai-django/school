# Generated by Django 3.0.5 on 2020-05-26 10:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4'), ('summer vacation', 'summer vacation'), ('winter vacation', 'winter vacation')], default=False, max_length=20)),
                ('abstract', models.CharField(max_length=100, verbose_name='abstract')),
                ('subjects', models.CharField(choices=[('Math', 'Math'), ('English', 'English'), ('Science', 'Science'), ('PE', 'PE'), ('Geography', 'Geography'), ('physics', 'Physics')], default=False, max_length=20)),
                ('grades', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default=False, max_length=1)),
                ('slug', models.SlugField()),
                ('is_registered', models.BooleanField(default=False)),
                ('name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='添付ファイル')),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('test_file', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='テストファイル')),
                ('test_course', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='course.CourseDetail')),
            ],
        ),
        migrations.CreateModel(
            name='SectionTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_test_name', models.CharField(max_length=50)),
                ('test_file', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='章末テストファイル')),
                ('section_test_course', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_score', models.PositiveIntegerField(default=False)),
                ('result_file', models.FileField(default=False, upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='テスト結果')),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='course.Test')),
                ('student', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_add', models.DateTimeField(auto_now_add=True)),
                ('is_course_registered', models.BooleanField(default=False)),
                ('course', models.ManyToManyField(to='course.Course')),
                ('name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MidMyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('my_course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='course.MyCourse')),
            ],
        ),
        migrations.CreateModel(
            name='FinalTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_test_name', models.CharField(max_length=50)),
                ('test_file', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='修了テストファイル')),
                ('final_test_course', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
    ]
