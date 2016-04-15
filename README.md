# markdown-upload-qiniu
将图片上传到七牛云存储并直接返回markdown可用的图片链接

功能虽然很简单，但确实刚需啊！！！以前写个markdown想要贴个图简直让人崩溃啊！！！

* 你可能先要截个图
* 然后打开浏览器
* 打开你的图床网站
* 点击上传图片
* 等待上传完成
* 复制外链
* 返回markdown
* 当然这是只是一个url，你还得写成markdown的格式，才算完成

执行完这些操作之后，思路早就跑到九霄云外了有木有，写文章的激情早就耗尽了！！！

废话太多了。言归正传

##运行要求：

1. python环境，并且有pywin32，没有的话[这里下][1]
2. AutoHotKey,这个真是个神器，自己下吧
3. windows系统
4. 七牛云存储账户
5. 没了

##使用方法：

+ 首先配置config.ini：
	- [qiniu]
	- ak     = # 填入你的AK
	- sk     = # 填入你的SK
	- url    = # 填入你的域名地址
	- bucket = # 填入你的七牛空间名称
	- 注意！！！注释一定都要删掉， 写值时不要加引号。ak,sk不是用户名和密码，是在账户管理中的密钥管理那里找到。填完是这样婶儿的：
![qiniuconfig](http://7xry4c.com1.z0.glb.clouddn.com//2016_04_15_qiniuconfig.png "qiniuconfig")

+ 然后是把config.ini和upload_qiniu.py放到同一个目录。
+ 然后修改upload_qiniu.ahk中的upload_qiniu.py路径
+ 然后双击upload_qiniu.ahk就可以了。
+ 用鼠标左键点击一张图片，然后点击ctrl+alt+c，然后窗口消失后再markdown里ctrl+v 神奇的事就发生了！

##借鉴
> 这个python脚本和ahk脚本并不是我的原创，只是因为我看的这些资料并不能直接运行，所以在他们的基础上做了相应的修改。感谢以下各位大神的分享

* [简化markdown写作中的贴图流程][3] 这个是写的很好，可是是mac的
* [简化markdown中的贴图流程][2] 这个是借鉴上问的windows版，作者是大神，写的比较简略。这里边的利用微信dll截图的功能非常值得借鉴
* [markdown-img-upload-windows][4]这个是github项目，可能是dll版本不对，我这里不成功














[1]:https://sourceforge.net/projects/pywin32/files/pywin32/ "pywin32"
[2]:http://mickir.xyz/blog/2015/12/simplify-the-img-upload-in-markdown.html 
[3]:http://tianweishu.com/2015/10/16/simplify-the-img-upload-in-markdown/
[4]:https://github.com/xzop/markdown-img-upload-windows/blob/master/ReadMe.md