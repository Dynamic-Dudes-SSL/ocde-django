from django.shortcuts import render
from .models import Code
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'codes': Code.objects.all()
    }
    return render(request, 'codes/home.html', context)

class CodeListView(ListView):
    model = Code
    template_name = 'codes/home.html' 
    context_object_name = 'codes'
    ordering = ['-date_posted']


class CodeDetailView(DetailView):
    model = Code


class CodeCreateView(LoginRequiredMixin, CreateView):
    model = Code
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CodeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Code
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        code = self.get_object()
        if self.request.user == code.author:
            return True
        return False


class CodeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Code
    success_url = '/'

    def test_func(self):
        code = self.get_object()
        if self.request.user == code.author:
            return True
        return False


