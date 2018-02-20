from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from apps.kindergarten.models import (
    Kindergarten,
    Group,
    Queue, QueueChildRelation)
from apps.user_profile.forms import RegisterChild


class KinderDetailView(DetailView):
    template_name = 'kindergarten/show_kindergarten.html'
    model = Kindergarten

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        context['groups'] = Group.objects.filter(kindergarten=self.object)

        return context


class KindergartenListView(ListView):
    model = Kindergarten
    template_name = 'kindergarten/kindergarten_page.html'
    context_object_name = 'kinder_list'
    queryset = Kindergarten.objects.select_related('district').all()


class RegisterKidView(View):

    def post(self, request):
        form = RegisterChild(request.POST)
        if form.is_valid():
            q = Queue.objects.filter(
                kindergarten=form.cleaned_data['kindergarten']
            ).last()

            q_c = QueueChildRelation(
                child=form.cleaned_data['child'],
                queue=q
            )
            q_c.save()

        return HttpResponseRedirect(reverse('main'))
