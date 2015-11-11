markdown图片上传&插入实用工具

这是一个方便在markdown格式的文档中插入截图的工具；能自动化完成图片上传，以及格式化为markdown格式实现无缝粘贴，体验起来就像直接把一张截图粘贴为一个markdown格式的图片链接一样。
## 预览

<img src="http://7sbqce.com1.z0.glb.clouddn.com/markdownmarkdownimg.gif" width="660" />

##  特性
1. 直接将剪切版里面的图片粘贴为markdown支持的图片链接
2. 支持retina的截图处理，在非retina的显示器上不会变大
3. 自动图片上传，失败通知栏通知

## 使用

### 设置七牛图床
#### 注册七牛
选择使用七牛的图床，没有账号的话先[注册](https://portal.qiniu.com/signup?code=3ldifp9oti442);

#### 新建图床
注册成功之后登陆，先新建一个图床：在左上角选择**新建空间**

<img src="http://7sbqce.com1.z0.glb.clouddn.com/markdown/1447222213451.png" width="271"/>

记下这个名字，比如：booluimg

#### 图床访问地址
新建空间之后，进入空间设置，点击左边的**域名设置**，记下你的图床对外的域名：

<img src="http://7sbqce.com1.z0.glb.clouddn.com/markdown/1447222404913.png" width="960"/>

#### 图床的Ak和SK
要使用七牛SDK来访问图床，需要拿到图床的Access Key以及Secret Key；点击右上角你的用户名，选择账号设置：

<img src="http://7sbqce.com1.z0.glb.clouddn.com/markdown/1447222540299.png" width="164"/>

然后，点击左边的**密钥**就可以看到你的**AK**以及**SK**

以上图床的信息拿到之后，在alfred里面输入mdimgsetup,就会弹出一个文本文档，如下：
<img src="http://7sbqce.com1.z0.glb.clouddn.com/markdown/1447222708345.png" width="256"/>

设置你的七牛图床的信息，AK，SK是访问密钥，url是上面配置的图床访问地址，bucket是空间名字，prefix是图床上传的前缀，这个可以随意配置，作为分类使用，比如我的时markdown

### 使用
使用任意截图工具截图之后，在任意编辑器里面你需要插入markdown格式图片的地方，按下cmd + ctrl + V即可！

另外，markdwon里面的图片链接不是标准的markdown格式，而是html的img标签；这是因为在retina屏幕下截图的话，如果不做任何处理，在非retina屏幕下面，这个图片会直接扩大两倍，非常粗糙难看；因此，需要保存图片显示大小的信息，保证截图大小和显示大小一致；这里使用mac系统自带的sips工具拿到截图大小，然后直接把宽度放在img标签里面。这样在显示的时候，可以保证是和截图时大小一致。

## TODO
1. 支持剪切版里面的文本格式的图片链接先下载然后上传到图床
2. 图片过大时自动压缩
3. qq截图的tiff格式暂时有bug
4. 临时文件夹不使用/tmp 用T噩梦批 File解决。




