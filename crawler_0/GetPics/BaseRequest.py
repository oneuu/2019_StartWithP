import requests
import os
import time
from bs4 import BeautifulSoup


class BeautifulPics():

    def __init__(self,folder_path):
        """
        类的初始化操作
        :param folder_path: 设置图片要存放的文件目录
        """
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; '
                                      'Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/71.0.3578.98 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.folder_path = folder_path

    def request(self, url):
        """
        返回网页的response
        :param url:
        :return:r
        """
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象
        return r

    def mkdir(self):
        """
        创建文件夹
        :return:
        """
        path = self.folder_path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

    def save_img(self, url, name):
        """
        保存单张图片
        :param url: 单张图片请求url
        :param name: 文件名
        :return:
        """
        print('开始保存图片...')
        img = self.request(url)
        if name == 'UNSPLASH':
            # 单独为Unsplash处理
            file_strs = img.headers.get('Content-Disposition').strip("'").strip('"').split('"')
            file_name = self.folder_path + file_strs[1]
        else:
            file_name = self.folder_path + name
        time.sleep(1)
        print('开始保存文件')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '文件保存成功！')
        f.close()



