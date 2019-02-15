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
