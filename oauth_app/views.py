from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from codes.models import Code
from django.contrib.auth.models import User


class UserView(TemplateView):
    template_name = 'oauth_app/users.html'

    def get_context_data(self, **kwargs):
        context = {
            'users' : User.objects.all()
        }
        return context

def UserCodes(user):
    codes = []
    for code in Code.objects.all():
        if code.author == user:
            codes.append(code)
    return codes[::-1]

def search_profile(user_id):
    for user in User.objects.all():
        if(user.id == user_id):
            return user

class ProfileView(TemplateView):
    template_name = 'oauth_app/profile.html'

    def get_context_data(self, **kwargs):
        context = {
            'user' : search_profile(kwargs['id']),
            'codes' : UserCodes(search_profile(kwargs['id']))
        }
        return context

class AboutUsView(TemplateView):
    template_name = 'oauth_app/about_us.html'        