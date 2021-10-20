from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


LANGUAGES = (
    ('C++', 'c++'),
    ('JAVA', 'java'),
    ('PYTHON', 'python'),
)

class Code(models.Model):
    title = models.CharField(max_length=100,default='#CODE')
    lang = models.CharField(max_length=6, choices=LANGUAGES, default='C++')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        sub=0
        for code in Code.objects.all():
            if(code.author==self.author):
                sub+=1
            if(code.content==self.content):
                break

        return str(self.author)+"##"+str(sub)

    def get_absolute_url(self):
        return reverse('code-detail', kwargs={'pk': self.pk})