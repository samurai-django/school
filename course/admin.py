from django.contrib import admin

from .models import Course, CourseDetail, RegisterCourse
from .models import MyCourse, Test, SectionTest, FinalTest, Result


admin.site.register(Course)
admin.site.register(CourseDetail)
admin.site.register(RegisterCourse)


admin.site.register(MyCourse)
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(SectionTest)

admin.site.register(FinalTest)


