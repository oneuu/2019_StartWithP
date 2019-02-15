from bs4 import BeautifulSoup
from bs4 import Comment
from bs4 import NavigableString

# 声明BeautifulSoup对象
soup = BeautifulSoup(open("BeautifulSoup_ex.html"), 'lxml')

find = soup.find('p')  # 使用find方法查到第一个p标签
print("find's return type is :::", type(find))  # 输出返回值类型
print("find's content is :::", find)  # 输出find获取的值
print("find's Tag Name is :::", find.name)  # 输出标签的名字
print("find's Attribute(class) is :::", find['class'])  # 输出标签的class属性值
print("find's Attribute(class) is :::", find.get('class'))  # 输出标签的class属性值

print('---------------------------')
print('soup.title :::', soup.title)
# <title>The Dormouse's story</title>

print('---------------------------')
print('soup.title.name :::', soup.title.name)
# u'title'

print('---------------------------')
print('soup.title.string :::', soup.title.string)
# u'The Dormouse's story'

print('---------------------------')
print('soup.title.parent.name :::', soup.title.parent.name)
# u'head'

print('---------------------------')
print('soup.p :::', soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

print('---------------------------')
print('soup.p[\'class\'] :::', soup.p['class'])
# u'title'

print('---------------------------')
print('soup.a :::', soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print('---------------------------')
print('soup.find_all(\'a\') :::', soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print('---------------------------')
print('soup.find(id="link3") :::', soup.find(id="link3"))
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

print('-------------insert追加-------------')
comment1 = soup.find(id="comment1")
print('String: ', comment1.string)

# new_string = NavigableString(" there")
# comment1.append(new_string)
# print('String: ', comment1.contents)

new_comment = comment1("Nice to see you.", Comment)
comment1.insert(1, '<!-- nice nice shot！-->')
print('Contents: ', comment1.parent)

# --------------遍历--------------

print('-------------所有父节点-------------')
link = soup.a
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print('-------------前后同级节点-------------')
link2 = soup.find("a", id="link2")
print(link2)
print(repr(link2.find_next_sibling()))  # 后兄弟节点
print(link2.find_previous_sibling())  # 前兄弟节点
