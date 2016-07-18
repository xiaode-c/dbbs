# coding:utf-8

from django import forms
from django.contrib.auth.models import User
from models import UserProfile, UserGroup
import os

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5)
    summary = forms.CharField(max_length=255, min_length=5)
    category_id = forms.CharField()
    head_imag = forms.ImageField()
    content = forms.CharField(min_length=10)

# class RegistreForm(forms.Form):
#     name = forms.CharField(max_length=255, min_length=5)
#     email = forms.EmailField()
#     password = forms.CharField()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name',)


def handle_uploaded_file(request,f):
    print(f.name)
    base_img_upload_path = 'statics/imgs'
    user_path = "%s/%s" % (base_img_upload_path, request.user.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open('%s/%s' % (user_path, f.name), 'wb+') as destination:
        # chunk是一个生成器(yield),一点点的存文件
        for chunk in f.chunks():
            destination.write(chunk)
    return '/static/imgs/%s/%s' % (request.user.userprofile.id ,f.name)


   