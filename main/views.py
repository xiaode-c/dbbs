# coding:utf-8

from django.shortcuts import render, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from forms import ArticleForm, handle_uploaded_file, UserForm, UserProfileForm
# Create your views here.
import models

def index(request):
    articles = models.Article.objects.all()
    print articles
    return render(request, "index.html", {'articles':articles})

def category(request, category_id):
    articles = models.Article.objects.filter(category_id=category_id)
    return render(request, "index.html", {'articles':articles})

def article_detail(request, article_id):
    try:
        article = models.Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        return render(request, '404.html',{'err_msg':u"文章不见了！！！"})
    return render(request, 'article.html', {'article':article})

def account_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def account_login(request):
    print(request.POST)
    err_msg = ""
    if request.method == "POST":
        print ('user authention...')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 如成功返回用户
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            err_msg = 'Wrong username or password'
    return render(request, 'login.html', {'err_msg':err_msg})

def account_register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user_id = user.id
            # profile.groups.add(models.UserGroup.objects.filter(name="user"))
            profile.save()
            profile.groups.add(models.UserGroup.objects.filter(name="user").first().id)

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form':profile_form, 'registered':registered})



def new_article(request):
    # 小于2.5M的文件存在内存中，大于的存在临时文件中
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            print("--form data:", form.cleaned_data)
            form_data = form.cleaned_data
            form_data['author_id'] = request.user.userprofile.id
            img_path = handle_uploaded_file(request, request.FILES['head_imag'])
            form_data['head_imag'] = img_path
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(request, 'new_article.html', {'new_article_obj': new_article_obj})
        else:
            print("err:", form.errors)
    category_list = models.Category.objects.all()
    return render(request, 'new_article.html', {'category_list':category_list})

def new_comment(request, article_id):
    article = models.Article.objects.get(id=article_id)
    if request.method == 'POST':
        parent_id = request.POST.get("parent_id")
        user = request.user.userprofile
        if parent_id:
            parent_comment = models.Comment.objects.get(id=parent_id)
        else:
            parent_comment = None
        comment = request.POST.get("comment")
        
        comment = models.Comment(article=article, user=user, comment=comment, parent_comment=parent_comment)
        comment.save()
        return HttpResponseRedirect('/article/%s/new_comment/' % article_id)
    return render(request, 'article.html', {'article':article})

    

# def tree_search(d_dic, parent, son):
#     for k, v_dic in d_dic.items():
#         if k == parent:
#             d_dic[k][son] = {}
#             print("find parent of:", son)
#             return
#         else:
#             print("going to deep")
#             tree_search(d_dic[k], parent, son) 


# data_dic = {}

# for item in data:
#     parent, son = item
#     if parent is None:
#         data_dic[son] = {}
#     else: #找爸爸
#         tree_search(data_dic, parent, son)
