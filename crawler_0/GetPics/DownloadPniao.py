from bs4 import BeautifulSoup

from crawler_0.GetPics import BaseRequest


def get_pics():
    web_url = 'http://www.pniao.com/'
    folder_path = '/Users/77z/Pictures/PythonPro_Img/pniao/'

    # 初始化类
    beauty = BaseRequest.BeautifulPics(folder_path=folder_path)
    beauty.mkdir()  # 创建本地文件夹

    print('开始请求url')
    r = beauty.request(web_url)
    soup = BeautifulSoup(r.text, 'lxml')
    print('html抓取成功')

    pics = soup.find_all('img', class_='orginSrc')
    for img in pics:
        img_url = img['data-url']
        img_name = img['alt'] + '.jpg'
        # print(img_name)
        # print(img_str)
        beauty.save_img(img_url, img_name)
    print('文件抓取完毕')


# Run
get_pics()


