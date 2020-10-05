# django博客

## 博客主题

博客的初版前端是完全仿照 [panda 博主的博客](http://panda.panda-studio.cn/)来的。未来会进行一定的改版。

博客后端是django，初版是按照[追梦人物的博客](https://www.zmrenwu.com/)中的django教程进行编写的。



## 博客界面 - 电脑端

首先说明这个界面基本上百分之九十以上都是模仿 panda 博主的上一版博客界面。现在那一版好像已经不在出售了。

##### 博客的首页展示：(包括轮播图、一些博客文章列表、个人信息展示 等)

​	顶部的导航栏在下滑时也会有相应的变化：

![index](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/index.png)



##### 在博客页中的分页栏的展示效果：

​	仍然和原版有些出入，目前就是这样了

![nav-tag](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/page.png)



##### 标签云和导航分类栏的展示：

![nav-tag](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/nav-tag.png)



##### 最多评论文章和最受欢迎文章需要点击才能显示出来

![most-like](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/most-like.png)



##### 日记页面展示：(这个是模仿的另一个博主的，忘了源地址了。。。 对它的风格做了一些调整，使得它契合这个主题)

![diary](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/diary.png)



同时这个页面和文章详情页都有全屏显示的功能，即隐藏右边栏：

![diary-screen](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/diary-screen.png)



##### 留言版展示：（主要原理就只是将评论区的功能移植了过来）

![board](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/board.png)



##### 最后就是文章详情页展示：(自动生成文章目录，)

**重点  ！！**

**重点 ！！**

**重点  ！！**

##### **为了高度还原原博客主题，修改了markdown 样式，所有标题都需要使用 二级标题  ，才能最完美适配**



![detail](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/detail.png)



当然这个博客页面对 平板端 、手机端 也做了相应的适配。

##  博客界面 - 平板端

![pad](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/pad.png)



## 博客界面 - 手机端

手机端将顶部导航栏以及个人信息进行了相应的隐藏。 

导航栏也可以点击右上角的图标进行显示。

![phone](https://github.com/DeYu666/New_django_blog/blob/master/doc/pic/phone.png)



## bug

这个博客有一个bug，初始化时，需要将数据库中的 “总类” 和 "分类" 中都添加上 “其他” 这一分类。



## 版本

django 是3.0版。其中需要的配置，都存放在 `requirements.txt`  中。

只需要运行以下命令，即可安装完全部配置。

```
pip install -r requirements.txt
```



## 未来版本迭代方向：

上线后第一批：

	1、rss订阅
	2、评论分页
	3、留言板分页
	4、日记，下拉显示更多
	5、分享文章、打赏文章
	6、搜索框、搜索文章
	7、评论区的评论回复
	8、评论区的表情
	9、文章中的markdown显示流程图
	10、每人每篇文章只能点赞一次，cookie ?
	11、总类 —> 分类 的链接 hover 样式
	12、头像、图片显示和保存
	13、复制文章 会多出一些东西链接，网站名 ...
	14、优化网站的css、js等样式。加载速度要快。
	15、按 F12 要出现一些网站的信息
	16、评论得经过同意才能显示到前端



上线后第二批：
	

	1、SEO优化
	2、观看网页的时长
	3、要做一个宝藏网站，惊喜挖掘不完的那种。
	4、网站的安全



## 遗憾

​	未来版本的迭代方向可能不会再实现了。如有同样需求，可以自行研究 python 和 django 解决，当然假如需求人数过多，我们可以一起共同开发。

​	在安装和使用过程中，如果遇到一些问题解决不了，请发送到 issue 中。



## 接下来方向

我又迷上的前后端分离的操作模式，打算使用 react 将此前端界面重新实现。

同时简化博客一些显示内容。增加一些其他更加好玩，更加实用的功能。



## 其他

script 文件夹下是批量制作测试内容的脚本，脚本具体用法，仍是参照追梦人物中的教程。
