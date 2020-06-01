import calendar
from collections import deque
import datetime
import itertools
from django import forms
...
...
class MonthWithFormsMixin(MonthCalendarMixin):
    """スケジュール付きの、月間カレンダーを提供するMixin"""

    def get_month_forms(self, start, end, days):
        """それぞれの日と紐づくフォームを作成する"""
        lookup = {
            # '例えば、date__range: (1日, 31日)'を動的に作る
            '{}__range'.format(self.date_field): (start, end)
        }
        # 例えば、Schedule.objects.filter(date__range=(1日, 31日)) になる
        queryset = self.model.objects.filter(**lookup)
        days_count = sum(len(week) for week in days)
        FormClass = forms.modelformset_factory(self.model, self.form_class, extra=days_count)
        if self.request.method == 'POST':
            formset = self.month_formset = FormClass(self.request.POST, queryset=queryset)
        else:
            formset = self.month_formset = FormClass(queryset=queryset)

        # {1日のdatetime: 1日に関連するフォーム, 2日のdatetime: 2日のフォーム...}のような辞書を作る
        day_forms = {day: [] for week in days for day in week}

        # 各日に、新規作成用フォームを1つずつ配置
        for empty_form, (date, empty_list) in zip(formset.extra_forms, day_forms.items()):
            empty_form.initial = {self.date_field: date}
            empty_list.append(empty_form)

        # スケジュールがある各日に、そのスケジュールの更新用フォームを配置
        for bound_form in formset.initial_forms:
            instance = bound_form.instance
            date = getattr(instance, self.date_field)
            day_forms[date].append(bound_form)

        # day_forms辞書を、周毎に分割する。[{1日: 1日のフォーム...}, {8日: 8日のフォーム...}, ...]
        # 7個ずつ取り出して分割しています。
        return [{key: day_forms[key] for key in itertools.islice(day_forms, i, i+7)} for i in range(0, days_count, 7)]

    def get_month_calendar(self):
        calendar_context = super().get_month_calendar()
        month_days = calendar_context['month_days']
        month_first = month_days[0][0]
        month_last = month_days[-1][-1]
        calendar_context['month_day_forms'] = self.get_month_forms(
            month_first,
            month_last,
            month_days
        )
        calendar_context['month_formset'] = self.month_formset
        return calendar_context