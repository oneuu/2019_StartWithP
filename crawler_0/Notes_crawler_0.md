# 爬虫你好

看了看python实际应用方向，之前向往爬虫很久，先从爬虫实战开始吧。<br/>
入门参考了阿利波特在cnblogs发的小白入门系列文章，讲的很明晰。
[点这里](https://www.cnblogs.com/Albert-Lee/tag/%E7%88%AC%E8%99%AB/) <br/>
入门知识就不再一一记下来了，笔记就写一些遇到的问题。
#### 0、PyCharm
编译环境需要选自己要用的python版本
#### 1、Requests
安装requests库的时候发现一个低级错误，import报错引用失败，搜了一下才发现是个低级错误啊。
<br/>
也算是准备python环境的一个需要注意的地方，
我用的OS X，系统本身自带python2.7，但自个儿又安装了python3.7。
<br/>
命令行输入python实际进入的还是系统的环境。
<pre>
...$ python #是系统自带的python2.7
...$ python3 #这才是自己安装的python3.7
</pre>
使用pip安装第三方库时指令时都需要变更成`pip3 install xxxxxx`，如果确定不需要系统自带的python及相关库，
执行下列语句将python的命令链接到新安装的3.7版本。
<pre>
(1)打开bash_profile文件
...$ open ~/.bash_profile
(2)添加下列语句后保存
alias python="/usr/local/bin/python3"
(3)重新读取.bash_profile文件
...$ source .bash_profile
</pre>
搞定之后检查了`pip list`发现之前安装的开发必备包`pip，distribute，nose，virtualenv`果然都跑到系统自带的python库里了，晕！
<br/>
其中distribute死活安不上，查了才发现不支持3.3以上版本，目前也没用到，逐放弃。
#### 2、BeautifulSoup+lxml
解析HTML和XML，真他娘的香啊！<br/>
4.4.0 .string 不支持输出comment，若混合存在也会输出None
通过属性的值来查找。<br/>
不过下面这段select用的`^=, $=, *=`语法不太明白，查了一下还没查到所以然。
<pre>
soup.select('a[href="http://example.com/elsie"]')
soup.select('a[href^="http://example.com/"]')
soup.select('a[href$="tillie"]')
soup.select('a[href*=".com/el"]')
</pre>
#### 3、PhantomJS
page.render()一开始无法截图，后来发现是必须要在js的目录下执行phantomjs语句才可以。<br/>
悲伤的是现在PhantomJS被弃，选择用Chrome--headless替代之，感叹啊参考的教程不过2017年，有些东西已经不适用于现在了，时代终究会抛弃一个又一个凡尘之物。
#### 4、Selenium
再一次真香！！！
<br/>
试着写几句话就得查一次官方文档，像婴儿学字。。
#### 5、练习
1）pniao首页图片<br/>
2）tvn任意一部剧的所有剧照<br/>
3）unsplash首页的raw文件，支持下滚页面<br/>
