from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from .forms import ReverseForm
from .models import servis, logo, barber, work


def home(request):
    data = {
        'servis': servis.objects.all(),
        'logo': logo.objects.all(),
    }
    return render(request, 'home/home.html', data)


class WorkView(DetailView):
    model = barber
    template_name = 'home/work.html'
    context_object_name = 'work'


class details(DetailView):
    model = servis
    template_name = 'home/details.html'
    context_object_name = 'servis'


class reverse(LoginRequiredMixin, DetailView, FormMixin):
    model = barber
    template_name = 'home/reverse.html'
    context_object_name = 'reverse'
    form_class = ReverseForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('reverse', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return redirect(request, 'reg/login.html')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.barber = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
