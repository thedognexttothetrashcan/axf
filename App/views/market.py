from django.shortcuts import render
from App.models import FoodTypes,Goods
#闪购
# select * from axf_goods where categoryid=103541 and childcid=103543  销量 价格

def market(req,categoryid=104749,childcid=0,orderby=0):
    foodType = FoodTypes.objects.all() #把所有类别查询出来 在左侧进行展示

    #判断是否有子类别传递过来
    if int(childcid):
        goodsData = Goods.objects.filter(categoryid=categoryid,childcid=childcid)
    else:
        goodsData = Goods.objects.filter(categoryid=categoryid)
    #排序
    orderby = int(orderby)
    if orderby == 1:
        goodsData = goodsData.order_by('-productnum')

    elif orderby == 2:
        goodsData = goodsData.order_by('price')

    elif orderby == 3:
        goodsData = goodsData.order_by('-price')

    #查找当前选中的类别的对象的子类类别的数据
    childCidData = foodType.filter(typeid=categoryid).first().childtypenames

    #childtypenames 进行拆分成 子类名和id 的字符串
    childTypeList = childCidData.split('#')
    typeList = []
    for childname in childTypeList:
        typeList.append(childname.split(':')) #子类名和id 的字符串 在次拆分 成列表 0为名称 1 为id

    return render(req, 'market/market.html',{'leftSlider':foodType,'goodsData':goodsData,'typeList':typeList,'categoryid':categoryid,'childcid':childcid})