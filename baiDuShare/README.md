# 代码功能说明
1. 可以批量导入百度云盘的分享链接
2. 可以通过百度云盘的账号密码，自动获取到cookie
3. share_url的内容样例  
https://pan.baidu.com/s/1WuOFZuBdeui2gohif0c12g	密码:12cd  
https://pan.baidu.com/s/1Qr6WaBh_pkq-i8hIpu6d7A	密码:o3tr  
https://pan.baidu.com/s/1dbp0zXE6xs3XMiJsssssNw	密码:i4rz  


# 还要完善的地方
1. 缺少一些异常处置的功能，导致运行一段时间后崩掉
2. 缺少一些校验的机制，导致崩掉后没办法断点续传
3. 跟云盘的交互不太友好，目前只能往根目录里面存
4. 代码功能比较烂，没有做太多的封装，需要手动配合执行


# 随便写的内容
需求来源其实是发现一位师傅在通过百度云盘分享他的电子书，由于个人的收藏嗜好，想要全给撸下来。  
开始是想寻找一些官方提供的api，个人比较喜欢命令行的工具，比较有效率，但是搜了一圈后似乎说是已经不太让用了；  
然后是找了一些工具，比如pandownload、邓西xxxx(免费版)，都不太符合自己预期，刚好想起来前段时间好像看了点selenium的教程，干脆就自己写一个好了～。  

看代码长度就知道了，其实蛮简单的，就是获取cookie的时候没注意sleep，导致拿到的cookie信息一直是没有认证过的，傻乎乎的调试了很久。。  
另外一个坑就是step的间隔过短，然后偶尔网络会卡顿那么一下，导致程序崩掉，需要频繁手动进行“断点续传功能”。  
最后用pkl来保存cookie似乎会更优雅一点，不管了，反正要的东西都撸下来了（笑）  

最后的最后，作为编程爱好者，能够通过代码处理掉一些重复性的工作/不想做的事情，还是蛮有成就感的，再接再厉吧  
