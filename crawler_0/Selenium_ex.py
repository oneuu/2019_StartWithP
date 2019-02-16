from selenium import webdriver  # 导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  # 导入Keys
from selenium.webdriver.support.select import Select

# 输入框搜索
driver = webdriver.Chrome()  # 指定使用的浏览器，初始化webdriver
driver.get("https://www.baidu.com/")  # 请求网页地址
assert "百度" in driver.title  # 看看Python关键字是否在网页title中，如果在则继续，如果不在，程序跳出。
elem = driver.find_element_by_name("wd")  # 找到name为q的元素，这里是个搜索框
elem.clear()  # 清空搜索框中的内容
elem.send_keys("pycon")  # 在搜索框中输入pycon
elem.send_keys(Keys.RETURN)  # 相当于回车键，提交
driver.close()  # 关闭webdriver

# select下拉框
driver1 = webdriver.Chrome()
driver1.get('file:///Users/77z/PycharmProjects/2019_StartWithP/crawler_0/Selenium_ex.html')
assert "oneuu" in driver1.title
sele = Select(driver1.find_element_by_name('cars'))
sele.select_by_index(2)
driver1.close()  # 关闭webdriver
