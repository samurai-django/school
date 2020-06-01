from django.contrib import admin

from account.models import Account, MessageToStudent

from django.contrib.auth.admin import UserAdmin
admin.site.register(MessageToStudent)


class AccountAdmin(UserAdmin):

    queryset = Account.objects.filter(is_active=True)

    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active', 'is_teacher', 'is_student',)
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)

