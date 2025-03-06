import django_filters
from django.db.models import Q
from users.models import User


class StudentFilter(django_filters.FilterSet):
    search_student = django_filters.CharFilter(method='filter_full_name_or_username')

    class Meta:
        model = User
        fields = ['search_student']

    def filter_full_name_or_username(self, queryset, name, value):
        words = value.strip().split()

        username_results = queryset.filter(username__icontains=value)

        if len(words) == 2:
            name_results = queryset.filter(Q(first_name__icontains=words[0]) & Q(last_name__icontains=words[1]))
        else:
            name_results = queryset.filter(
                Q(first_name__icontains=value) |
                Q(last_name__icontains=value)
            )

        return username_results | name_results
