from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from App.models import User,Car,Goods
import json

#购物车模板的展示
@login_required(login_url='/login/')
def car(req):
    carData = req.user.car_set.all()
    # for obj in carData:
    #     obj.goods.
    money = 0
    for obj in carData:
        if obj.isChoose:
            money += eval(obj.goods.price)*obj.num
    print(money)
    return render(req,'car/car.html',{'carData':carData,'money':'%.2f'%money})



def doCar(req):
    if not req.user.is_authenticated:
        return JsonResponse({'state':500})
    # print(req.GET)
    state = int(req.GET.get('state'))
    goodsid = int(req.GET.get('goodsid'))

    user = req.user #拿到当前用户对象

    goodsObj = Goods.objects.filter(id=goodsid).first() #取出商品对象
    cartObj = user.car_set.filter(goods=goodsObj) #拿到当前用户在购物车中的数据对象
    totalNum = 0 #初始化数量num
    money = 0 #初始化 钱0元
    #数量-1
    if state == 0:
        if cartObj.exists():  # 判断该商品是否在购物车中 在则数量-1
            num = cartObj.first().num  # 取出购物车该商品的数量
            totalNum = num-1
            if totalNum>0:
                cartObj.update(num=totalNum)  #修改购物车中商品的数量-1
            else:
                cartObj.delete()  #删除购物车的商品

    #数量+1
    if state == 1:
        if cartObj.exists(): #判断该商品是否在购物车中 在则数量+1
            num = cartObj.first().num #取出购物车该商品的数量
            totalNum = num+1
            # totalNum = goodsObj.storenums
            if totalNum > int(goodsObj.storenums): #判断购物车的商品数量是否大于商品库存量
                totalNum = int(goodsObj.storenums)
            cartObj.update(num=totalNum) #将购物车商品的数量+1
        else:
            Car(goods = goodsObj,user = user).save() #保存到购物车
            totalNum = 1

    #等于2 就对isChoose的值进行取反
    chooseObj = cartObj.first()
    Bool = True
    if chooseObj:
        Bool = chooseObj.isChoose #取出选中还是未选中的布尔值
        if state == 2:
            chooseObj.isChoose = not Bool
            chooseObj.save()
            totalNum = chooseObj.num
            Bool = not Bool

    #当点击+或者-的时候 对应改变钱的数值
    carChoose = user.car_set.filter(isChoose=True)
    if carChoose.exists():
        for obj in carChoose:
            money += eval(obj.goods.price) * obj.num
    return JsonResponse({'state':200,'num':totalNum,'money':'%.2f'%money,'Bool':Bool})
    # return HttpResponse(json.dumps({'data':200}))

#判断是否有选中的商品下订单
def findChoose(req):
    return JsonResponse({'result':req.user.car_set.filter(isChoose=True).exists()})