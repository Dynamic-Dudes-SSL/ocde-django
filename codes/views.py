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
    fields = ['lang', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def output(self,form):
        code = self.get_object()
        pycode=" "
        pyoutput=""
        pycode=code.content
        if len(pycode)>0:
            f2 = open("pyt.py", "w")
            f2.write(pycode)
            f2.close()
            cmd = "pyt.py"
            p3=subprocess.run(["python", cmd], stdout=PIPE, stderr=PIPE)
            if p3.returncode==0:
                pyoutput=p3.stdout.decode()
            else:
                pyoutput="error"
            os.remove("pyt.py")
        form.instance.output = pyoutput

        cppcode="get lost"
        cppoutput="no output"
            # cppcode=request.POST['cpp','']
            # if len(cppcode)>0:
            #     f = open("cpy.cpp", "w")
            #     f.write(cppcode)
            #     f.close()
            #     cmd = "cpy.cpp"
            #     p2=subprocess.run(["g++", cmd])
            #     if p2.returncode==0:
            #         p1=subprocess.run("./a.out", stdout=PIPE, stderr=PIPE)
            #         if p1.returncode==0:
            #             cppoutput=p1.stdout.decode()
            #         else:
            #             cppoutput="runti

        return super().form_valid(form)


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


class CodeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Code
    success_url = '/code'

    def test_func(self):
        code = self.get_object()
        if self.request.user == code.author:
            return True
        return False


