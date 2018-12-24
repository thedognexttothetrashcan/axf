from django.contrib.auth import authenticate, login as Login, logout as Logout
from django.contrib.auth.decorators import login_required
from App.models import User
from django.shortcuts import render,HttpResponse, redirect
from django.urls import reverse

def mine(req):
    return render(req, 'mine/mine.html')


def login(req):
    if req.method == 'GET':
        return render(req,'mine/login.html')

    if req.method == 'POST':
        #authenticate用户认证的方法 如果用户名和密码正确 则返回对象  否则返回None
        u = authenticate(username=req.POST.get('username'),password=req.POST.get('userpass'))
        if u:
            if u.is_active:
                Login(req,u)
                # return HttpResponse('登录称该并且该用户已经激活 你只需要保持当前用户的登录状态')
                return redirect(reverse('App:index'))

        return HttpResponse('输入正确的用户名或者密码')

    return HttpResponse('登录')


def register(req):
    if req.method == 'GET':
        return render(req,'mine/register.html')
    if req.method == 'POST':
        u = User.objects.create_user(req.POST.get('username'),req.POST.get('email'),req.POST.get('userpass'))
        u.save()
    return redirect(reverse('App:login'))


def logout(req):
    Logout(req)
    return redirect(reverse('App:mine'))
