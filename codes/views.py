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
from subprocess import PIPE
import subprocess
import os

def home(request):
    context = {
        'codes': Code.objects.all()
    }
    return render(request, 'codes/home.html', context)

def class_name(content):
    words2 = content.split('{')
    words = words2[0].split(" ")
    name = words[-1]
    if name[-1]=='{':
        name = name[0:-2]
    return name

def get_output(code_written):
    code = code_written.content 
    lang = code_written.lang
    title = code_written.title
    output="abc"
    cmd2=""
    if lang == "PYTHON":
        if len(code)>0:
            f2 = open("pyt.py", "w")
            f2.write(code)
            f2.close()
            cmd = "pyt.py"
            p2=subprocess.run(["python3", cmd], stdout=PIPE, stderr=PIPE)
            if p2.returncode==0:
                output=p2.stdout.decode()
            else:
                output="error"
                os.remove("pyt.py")

    elif lang == 'C++':
        if len(code)>0:
            f1 = open("cpy.cpp", "w")
            f1.write(code)
            f1.close()
            cmd = "cpy.cpp"
            p1=subprocess.run(["g++", cmd])
            if p1.returncode==0:
                p1=subprocess.run("./a.out", stdout=PIPE, stderr=PIPE)
                if p1.returncode==0:
                    output=p1.stdout.decode()
                else:
                    output="runtime error"
            else:
                output="compilation error"
            os.remove("cpy.cpp")
            os.remove("./a.out")

    elif lang == 'JAVA':
        if len(code)>0:
            cmd2=class_name(code)
            cmd =cmd2+ ".java"
            f3 = open(cmd, "w")
            f3.write(code)
            f3.close()
            p3=subprocess.run(["javac", cmd])
            if p3.returncode==0:
                p3=subprocess.run(["java",cmd2], stdout=PIPE, stderr=PIPE)
                if p3.returncode==0:
                    output=p3.stdout.decode()
                else:
                    output="runtime error"
            else:
                output="compilation error"
            os.remove(cmd)
            #os.remove(cmd2+".class")
            
    return output

def submissions(user):
    codes = Code.objects.all()
    subm = 0
    for code in codes:
        if code.author==user:
            subm += 1
    return subm

def sumbit(user, mycode):
    codes = Code.objects.all()
    subm = 0
    for code in codes:
        if code.author==user:
            subm += 1
            if(code==mycode):
                return subm
    return subm

class CodeListView(ListView):
    model = Code
    template_name = 'codes/home.html' 
    context_object_name = 'codes'
    ordering = ['-date_posted']


class CodeDetailView(DetailView):
    model = Code

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['output'] = get_output(self.get_object())
        return context

class CodeCreateView(LoginRequiredMixin, CreateView):
    model = Code
    fields = ['lang', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submissions'] = submissions(self.request.user)+1
        return context

class CodeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Code
    fields = ['lang', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        code = self.get_object()
        if self.request.user == code.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submissions'] = sumbit(self.request.user,self.get_object())
        return context


class CodeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Code
    success_url = '/code'

    def test_func(self):
        code = self.get_object()
        if self.request.user == code.author:
            return True
        return False


