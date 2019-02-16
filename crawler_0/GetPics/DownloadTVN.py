from bs4 import BeautifulSoup

from crawler_0.GetPics import BaseRequest


def get_Boards(drama_url, drama_name):
    """
    抓取TVN电视剧所有剧照
    :param drama_url: 剧照Board第一页
    :param drama_name: 剧名，用于单独存储
    :return:
    """
    tvn_url = 'http://program.tving.com'
    web_url = tvn_url + drama_url
    folder_path = '/Users/77z/Pictures/PythonPro_Img/' + drama_name + '/'

    # 初始化类
    beauty = BaseRequest.BeautifulPics(folder_path=folder_path)
    beauty.mkdir()  # 创建本地文件夹

    print('开始请求url')
    r = beauty.request(web_url)
    soup = BeautifulSoup(r.text, 'lxml')
    print('html抓取成功')

    child_page = soup.find('a', class_='thumb')
    child_page_href = child_page['href']
    # 子贴总数
    count_index = child_page_href.index("b_seq=")
    child_page_count = child_page_href[count_index:].replace('b_seq=', '')
    # 子贴通用url部分
    front_index = child_page_href.index("page=")
    child_page_url_front = tvn_url + child_page_href[: front_index] + 'b_seq='
    # http://program.tving.com/tvn/encounter/3/Board/View?b_seq=
    # 55
    i = 1
    while i <= int(child_page_count):
        print('i= ', i)
        child_page_url = child_page_url_front + str(i)
        print(child_page_url)
        r_child = beauty.request(child_page_url)
        soup_child = BeautifulSoup(r_child.text, 'lxml')
        try:
            child_data = soup_child.find('p', class_='info_write').find('span').string
            child_title = child_data[: child_data.index(' ')].strip().replace('.', '')
        except AttributeError:
            i += 1
            continue
        child_images = soup_child.find_all('img', class_='chimg_photo')
        for img in child_images:
            img_url = img['src']
            img_name = child_title + '_' + str(i) + '_' + img['alt'].strip()
            # print(img_url)
            # print(img_name)
            beauty.save_img(img_url, img_name)
        i += 1
    print('文件抓取完毕')



# 2018 TVN Encounter
drama_url = '/tvn/encounter/3/Board/List?page=1'
drama_name = 'Encounter'

# 2017 TVN Firstlife
drama_url = '/tvn/tvnfirstlife/10/Board/List?page=1'
drama_name = 'firstlife'

# 2018 TVN Mymister
drama_url = '/tvn/mymister/5/Board/List?page=1'
drama_name = 'mymister'

# Run Here
get_Boards(drama_url, drama_name)
