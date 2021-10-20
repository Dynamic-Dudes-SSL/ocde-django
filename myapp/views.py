from django.shortcuts import render
from subprocess import PIPE
import subprocess
import os

# Create your views here.
def index(request):
    cppcode="get lost"
    cppoutput="no output"
    pycode=" "
    pyoutput=" "
    if request.method == 'POST':
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
        #             cppoutput="runtime error"
        #     else:
        #         cppoutput="compilation error"
        #     os.remove("cpy.cpp")

        pycode=request.POST['py']
        if len(pycode)>0:
            f2 = open("pyt.py", "w")
            f2.write(pycode)
            f2.close()
            cmd = "pyt.py"
            p3=subprocess.run(["python3", cmd], stdout=PIPE, stderr=PIPE)
            if p3.returncode==0:
                pyoutput=p3.stdout.decode()
            else:
                pyoutput="error"
            os.remove("pyt.py")

    context={
        
        'cppcode':cppcode,
        'cppoutput':cppoutput,
        'pycode':pycode,
        'pyoutput':pyoutput
    }
    return render(request, 'index.html',context)
