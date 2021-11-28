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
global_content=""
global_lang=""
global_title=""
global_user_input=""


def home(request):
    context = {
        'codes': Code.objects.all()
    }
    return render(request, 'codes/home.html', context)

def output(request):
    global global_user_input
    global_user_input = request.POST['userin']
    print_output = get_output()
    con={
        'global_user_input' : global_user_input ,
        'global_content' : global_content ,
        'global_lang' : global_lang ,
        'global_title' : global_title ,
        'print_output' : print_output
    }
    return render(request,'codes/output.html',con)

def class_name(content):
    words2 = content.split('{')
    words = words2[0].split(" ")
    name = words[-1]
    if name[-1]=='{':
        name = name[0:-2]
    return name

def get_output():
    # code = code_written.content 
    # lang = code_written.lang
    # title = code_written.title
    code=global_content
    lang=global_lang
    title=global_lang
    output=""
    cmd2=""
    f6=open("in.txt","w")
    f6.write(global_user_input)
    f6.close()
    if lang == "PYTHON":
        if len(code)>0:
            f2 = open("pyt.py", "w")
            f2.write(code)
            f2.close()
            
            os.system("echo kurama | sudo -S ls")
            os.system("sudo docker create --name OCDE -t --net=host -v \"$HOME\" -e DISPLAY=\"$DISPLAY\" --volume=\"$HOME/.Xauthority:/root/.Xauthority:rw\" --cap-add=SYS_PTRACE --security-opt seccomp=unconfined cs251aut2021")
            os.system("sudo docker start OCDE")
            os.system("sudo docker cp ./pyt.py OCDE:/home")
            os.system("sudo docker cp ./in.txt OCDE:/home")
            output = subprocess.check_output("(echo \"python3 pyt.py < in.txt; exit 0 \") | sudo docker exec -i OCDE /bin/bash", shell=True).decode('utf-8')
            os.system("echo kurama | sudo -S docker stop OCDE")
            os.system("echo kurama | sudo -S docker container rm OCDE")
            # output = subprocess.check_output("python3 pyt.py < in.txt; exit 0", shell=True).decode('utf-8')
            os.remove("pyt.py")

    elif lang == 'C++':
        if len(code)>0:
            f1 = open("cpy.cpp", "w")
            f1.write(code)
            f1.close()
            cmd = "cpy.cpp"
            p1=subprocess.run(["g++", cmd])
            if p1.returncode==0:
                # output = subprocess.check_output("./a.out < in.txt", shell=True).decode('utf-8')
                # os.remove("./a.out")
                os.system("echo kurama | sudo -S ls")
                os.system("sudo docker create --name OCDE -t --net=host -v \"$HOME\" -e DISPLAY=\"$DISPLAY\" --volume=\"$HOME/.Xauthority:/root/.Xauthority:rw\" --cap-add=SYS_PTRACE --security-opt seccomp=unconfined cs251aut2021")
                os.system("sudo docker start OCDE")
                os.system("sudo docker cp ./a.out OCDE:/home")
                os.system("sudo docker cp ./in.txt OCDE:/home")
                output = subprocess.check_output("(echo \"./a.out < in.txt; exit 0 \") | sudo docker exec -i OCDE /bin/bash", shell=True).decode('utf-8')
                os.system("echo kurama | sudo -S docker stop OCDE")
                os.system("echo kurama | sudo -S docker container rm OCDE")
                os.remove("./a.out")
            else:
                output="compilation error"
            os.remove("cpy.cpp")
            
    
    elif lang == 'JAVA':
        if len(code)>0:
            class_name = global_title
            source = class_name + ".java"
            f3 = open(source , "w")
            f3.write(code)
            f3.close()
            p3 = subprocess.run(["javac", source])
            if p3.returncode==0:
                # output=subprocess.check_output("java \"+ source + \"; exit 0", shell=True).decode('utf-8')
                os.system("echo kurama | sudo -S ls")
                os.system("sudo docker create --name OCDE -t --net=host -v \"$HOME\" -e DISPLAY=\"$DISPLAY\" --volume=\"$HOME/.Xauthority:/root/.Xauthority:rw\" --cap-add=SYS_PTRACE --security-opt seccomp=unconfined cs251aut2021")
                os.system("sudo docker start OCDE")
                os.system("sudo docker cp ./" + class_name + ".class OCDE:/home")
                os.system("sudo docker cp ./in.txt OCDE:/home")
                output = subprocess.check_output("(echo \"java " + class_name + " < in.txt; exit 0 \") | sudo docker exec -i OCDE /bin/bash", shell=True).decode('utf-8')
                os.system("echo kurama | sudo -S docker stop OCDE")
                os.system("echo kurama | sudo -S docker container rm OCDE")
                os.system("rm *.class")
            else:
                output="compilation error"
            os.remove(source)
    os.remove("in.txt")
    output = output.replace("\n","<br>")
    output = output.split("<br>")
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
        global global_title
        global global_lang
        global global_content
        context = super().get_context_data(**kwargs)
        global_title=self.get_object().title
        global_lang=self.get_object().lang
        global_content=self.get_object().content
        #context['output'] = get_output(self.get_object())
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


