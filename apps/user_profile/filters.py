import django_filters

from apps.kindergarten.models import Kindergarten


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Kindergarten
        fields = ['name']
