from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import BaseRequest


def get_Unsplash():
    """
    通过Requests+Beautifulsoup方式实现图片抓取下载
    :return:
    """
    web_url = 'https://unsplash.com'
    folder_path = '/Users/77z/Pictures/PythonPro_Img/Unsplash/'

    # 初始化类
    beauty = BaseRequest.BeautifulPics(folder_path=folder_path)
    beauty.mkdir()  # 创建本地文件夹

    print('开始请求url')

    # 1、通过requests模拟浏览器发起请求获取
    # r = beauty.request(web_url)
    # soup = BeautifulSoup(r.text, 'lxml')

    # 2、# 通过phantomjs获取
    # 通过chrome请求
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(web_url)
    print('Driver 启动完毕 ：', driver)
    page_scroll(driver, times=1)  # 模拟下拉操作
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print('html抓取成功')

    # 格式化元素输出至html文件
    # filepath = "/Users/77z/PycharmProjects/2019_StartWithP/crawler_0/GetPics/temp.html"
    # file = open(filepath, 'w')
    # file.write(soup.prettify())
    # file.close()

    # 过滤所有含有download链接的div
    divs = soup.find_all('a', class_='_2Mc8_')
    print('图片数量：', len(divs))
    for div in divs:
        img_url = 'https://unsplash.com/photos/' + div['href'].replace('/photos/', '') + '/download?force=true'
        print(img_url)
        # https://unsplash.com/photos/wI6o8OwUwdw/download?force=true
        beauty.save_img(img_url, 'UNSPLASH')
    driver.close()  # 关闭webdriver
    print('文件抓取完毕')


def page_scroll(driver, times):
    print("开始下拉页面")
    i = 1
    while i <= times:
        print('第' + str(i) + '次滚动')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(300)
        print('第' + str(i) + '次等待 Successful!')
        i += 1


# Run Here
get_Unsplash()
