from django.views.generic import ListView

from apps.location.models import District


class LocationListView(ListView):
    model = District
    context_object_name = 'district_list'
    queryset = District.objects.all()
