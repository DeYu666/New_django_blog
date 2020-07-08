1、  File "D:\Program Files\Python\Python36\lib\socket.py", line 674, in getfqdn
     hostname, aliases, ipaddrs = gethostbyaddr(name)
     UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd2 in position 0: invalid continuation byte

解决方法：经研究错误提示发现gethostbyaddr()函数是中文翻译就是获取主机地址，而传参是名字，那么name传入的就是主机名，也就是我们电脑名。我的电脑名是中文，

是不是改成英文就可以了，经测试发现的确是主机中文名导致的问题，改成英文名即可顺利启动本地服务器。





2、安装   pip install django-mdeditor  时，报错：

	    File "C:\Users\ADMINI~1\AppData\Local\Temp\pip-install-qh3ef77v\django-mdeditor\setup.py", line 6, in <module>
           long_description = readme.read()
    	UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 167: illegal multibyte sequence


解决方法：
		把setup.py中第五行改为：
		with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:





3、Form 中的一些方法：
	https://www.liujiangblog.com/course/django/156
	https://stackoverflow.com/questions/5827590/css-styling-in-django-forms











安装的包

	markdown 编辑器
	pip install django-mdeditor

	分页
	pip install django-pure-pagination

	pip install Pillow


	pip install git+git://github.com/sshwsfc/xadmin.git@django2








使用说明：

	文章的分类 和 总类 中必须含有 “其他”













我要做那种 宝藏网站。



上线前的改进：
	
  √ 1、异步点赞
  √ 2、友情链接   
  √ 3、边栏第二页（最多喜欢、最多评论）
  √ 4、底部的其他文章
  √ 5、详细页的相关文章
  √ 6、404页面
  √ 7、轮播图
  √ 8、修复留言板的bug
	 9、微博、公众号链接


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












# 停止 
uwsgi --stop uwsgi.pid
pkill -f uwsgi -9