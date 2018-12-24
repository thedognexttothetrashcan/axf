from django.shortcuts import render,HttpResponse, redirect
from django.urls import reverse

from App.models import User,Car,Order,OrderDetail,Address

#订单展示页
def order(req):
    #把所有选中的商品在订单生成模板页面进行展示
    carData = req.user.car_set.filter(isChoose=True)
    money = 0
    for obj in carData:
            money += eval(obj.goods.price) * obj.num
    # 拿到默认的地址
    address = req.user.address_set.filter(state=True).first()

    return render(req,'order/generateorder.html',{'carData':carData,'money':'%.2f'%money,'address':address})

import time
#处理订单生成
def doOrder(req):
    # 拿到传递过来的留言
    message = req.POST.get('message')
    #保存生成订单
    orderObj = Order(user=req.user,address=req.user.address_set.filter(state=True).first(),money=req.POST.get('money'),message=message,orderId=time.strftime('%y%m%d%H%M%s'))
    orderObj.save()
    #保存订单详情
    carData = req.user.car_set.filter(isChoose=True)
    for car in carData:
        OrderDetail(order=orderObj,goodsImg=car.goods.productimg,goodsName=car.goods.productname,price=car.goods.price,num=car.num,total=car.num*eval(car.goods.price)).save()
    return redirect(reverse('App:car'))