from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



# Create your models here.
class User(AbstractUser):
    icon = models.CharField(max_length=70,default='default.jpg')
    class Meta:
        db_table = 'user'


#定义一个抽象类 公有的父类 用子类继承实现
class Common(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract = True

#轮波图
class Wheel(Common):
    class Meta:
        db_table = 'axf_wheel'

#轮波图下面的导航 每日必抢
class Nav(Common):
    class Meta:
        db_table = 'axf_nav'

#每日必抢下面的 必买
class MustBuy(Common):
    class Meta:
        db_table = 'axf_mustbuy'

#必买 下面的便利店
class Shop(Common):
    class Meta:
        db_table = 'axf_shop'

#主要卖品
class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=10)
    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=40)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=40)
    marketprice1 = models.CharField(max_length=40)
    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)
    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)
    class Meta:
        db_table = 'axf_mainshow'


#商品类别模型
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=10)
    childtypenames = models.CharField(max_length=120)
    typesort = models.IntegerField()
    class Meta:
        db_table = 'axf_foodtypes'

#商品模型
class Goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=100)
    productname = models.CharField(max_length=30)
    productlongname = models.CharField(max_length=100)
    isxf = models.BooleanField()
    pmdesc = models.BooleanField()
    specifics = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    marketprice = models.CharField(max_length=30)
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=30)
    dealerid = models.CharField(max_length=10)
    storenums = models.IntegerField()
    productnum = models.IntegerField()
    class Meta:
        db_table = 'axf_goods'



#购物车模型
class Car(models.Model):
    goods = models.ForeignKey(Goods)
    user = models.ForeignKey(User)
    num = models.IntegerField(default=1)
    isChoose = models.BooleanField(default=True)
    class Meta:
        db_table = 'axf_car'
    #添加一个字段 全部选中字段  当点击全选的时候 把全选改为True  并且把所有的 isChoose 的值改为True/False


#地址模型
class Address(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=10)
    state = models.BooleanField(default=False)
    class Meta:
        db_table = 'axf_address'

#订单模型
class Order(models.Model):
    user = models.ForeignKey(User)
    address = models.ForeignKey(Address)
    money = models.DecimalField(max_digits=8,decimal_places=2)
    message = models.CharField(max_length=100)
    createTime = models.DateTimeField(auto_now_add=True)
    orderId = models.CharField(max_length=32)
    status = models.IntegerField(default=0) #订单的状态 0下单未付款 1 已付款 2未发货 3 已发货 4 已收货
    class Meta:
        db_table = 'axf_order'

#订单详情
class OrderDetail(models.Model):
    order = models.ForeignKey(Order)
    goodsImg = models.CharField(max_length=100)
    goodsName = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    num = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=8,decimal_places=2)
    class Meta:
        db_table = 'axf_orderdetail'









