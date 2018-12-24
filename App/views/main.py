from django.shortcuts import render
from App.models import Wheel,Nav,MustBuy,Shop,MainShow

# Create your views here.

def index(req):
    wheel = Wheel.objects.all() #轮波图
    nav = Nav.objects.all()#nav导航的数据
    mustBuy = MustBuy.objects.all() #必买品
    shop1 = Shop.objects.first() #取出 第一个shop的商品
    all = Shop.objects.all()
    shop2 = all[1:3]#取出shop的第二个和第三个商品
    shop3 = all[3:7]#取出shop的第二个和第三个商品
    shop4 = all[7:12]
    mainShow = MainShow.objects.all()
    return render(req, 'main/index.html',{'wheel':wheel,'nav':nav,'mustBuy':mustBuy,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,'mainShow':mainShow})