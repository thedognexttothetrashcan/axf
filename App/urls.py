from django.conf.urls import url
from App.views import *
urlpatterns = [
    url(r'^$', main.index,name='index'),
    url(r'^main/$', main.index,name='index'),
    url(r'^market/$', market.market,name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', market.market,name='market2'),
    url(r'^car/$', car.car,name='car'),
    url(r'^docar/$', car.doCar,name='docar'), # 对于购物车中的商品的处理
    url(r'^findChoose/$', car.findChoose, name='findChoose'),#ajax判断是否有商品选中

    url(r'^mine/$', mine.mine,name='mine'),

    url(r'^login/$',mine.login,name='login'),
    url(r'^logout/$',mine.logout,name='logout'),
    url(r'^register/$',mine.register,name='register'),

    #订单
    url(r'^order/$', order.order, name='order'),
    url(r'^doorder/$', order.doOrder, name='doOrder'),

]