# 导入requests库
import requests


def print_con(r, type):
    # r.text是http response的网页HTML
    print(r.text)
    print('------------------------------------------------------')
    print('⬆⬆⬆ %s 请求：' % str(type))
    print('------------------------------------------------------')


# 简单的get请求
r = requests.get('https://unsplash.com')
print_con(r, 'GET')

# 带参数的get请求
get_param = {'q': 'Boy+Erased'}
r = requests.get("https://www.zimuku.cn/search", params=get_param)
print_con(r, 'GET')

# 简单的post请求
post_param = {'key_1': 'python','key_2': 'baby'}
r = requests.post("http://httpbin.org/post", params=post_param)
print_con(r, 'POST')
