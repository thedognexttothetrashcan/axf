/**
 * Created by xlg on 18-9-12.
 */
function doCart(goodsid, state) {
    console.log(goodsid, state);
    // {#      ajax传输      #}
    $.get('/docar/', {'goodsid': goodsid, 'state': state}, function (data, status) {
        // {#      如果值为500 则表示未登录          #}
        if (data.state == 500) {
            if (window.confirm('是否前去登录？')) {
                window.location.href = '/login/';
            }
        }
        // {#       修改显示购物车中的数量         #}
        $('#' + goodsid).html(data.num);
    })
}