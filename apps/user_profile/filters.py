import django_filters

from apps.kindergarten.models import Kindergarten


class KinderFilter(django_filters.FilterSet):
    class Meta:
        model = Kindergarten
        fields = ['name']
