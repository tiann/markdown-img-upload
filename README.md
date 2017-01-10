# markdown图片实用工具

这是一个方便的图片上传实用工具，可以**方便**, **快速**地把一张图片上传然后得到一个图片链接：

1. 极速截图转图片链接
2. 极速本地图片转图片链接
3. 极速网络图片转自定义图片链接

图片上传到图床之后，会自动把上传返回的链接放置到系统剪切版上，同时它对markdown格式有特殊的支持；整个过程只需要两步：

1. 截图/复制本地图片/复制网络图片链接
2. 快捷键 `cmd + ctrl + v` 进行上传

上传完成之后，返回的图片链接自动放入到系统剪切版中，可以直接使用`cmd + V` 使用。

## 预览

1. 极速截图转图片链接

<img src="http://7sbqce.com1.z0.glb.clouddn.com/markdownmarkdownimg.gif" width="660" />

2. 极速本地图片转图片链接

![本地图片转图片链接](http://7xp3xc.com1.z0.glb.clouddn.com/201602markdown_img_local.gif)

##  特性

- 直接将图片粘贴为markdown支持的图片链接
- 支持retina的截图处理，在非retina的显示器上不会变大
- 自动图片上传，失败通知栏通知
- 支持多种截图格式，压缩过大图片
- 方便的图片上传工具 

## 使用前准备

### 安装依赖

由于七牛SDK使用了`requests`库进行网络请求，所以，**首先得安装python的`requests`库**；推荐使用pip进行安装。

> 注意：是`requests`库，而不是`request`库，安装错误则无法正常使用。

### 获取七牛图床信息
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

### 配置
#### 安装 Alfred 工作流

- 首先请确认`request`库安装成功；
- 然后下载并导入项目目录中的 Alfred 工作流文件；
- **设置触发热键！**，如`Cmd + Ctrl + V`，注意保证不要与其他软件的热键冲突。

#### 配置图床

在前面，图床的信息拿到之后，在 alfred 里面输入`mdimgsetup`,就会弹出一个文本文档，如下：
<img src="http://7sbqce.com1.z0.glb.clouddn.com/markdown/1447222708345.png" width="256"/>

设置你的七牛图床的信息，AK，SK是访问密钥，url是上面配置的图床访问地址，bucket是空间名字，prefix是图床上传的前缀，这个可以随意配置，作为分类使用，比如我的是 markdown。

## 使用

### 通过截图上传

使用任意截图工具截图之后，在任意编辑器里面你需要插入markdown格式图片的地方，按下cmd + ctrl + V即可！

另外，markdwon里面的图片链接不是标准的markdown格式，而是html的img标签；这是因为在retina屏幕下截图的话，如果不做任何处理，在非retina屏幕下面，这个图片会直接扩大两倍，非常粗糙难看；因此，需要保存图片显示大小的信息，保证截图大小和显示大小一致；这里使用mac系统自带的sips工具拿到截图大小，然后直接把宽度放在img标签里面。这样在显示的时候，可以保证是和截图时大小一致。

### 通过本地图片上传

如果你已经有一张图片了，希望上传到图床得到一个链接；通常的方式需要图床客户端或者浏览器插件，通过这个alfred插件：

直接复制本地图片，然后按下cmd + ctrl + v 就能得到图床的链接！

## TODO
1. 支持剪切版里面的文本格式的图片链接先下载然后上传到图床
2. ~~如果复制的直接时图片文件，能直接上传生成URL.~~
2. ~~图片过大时自动压缩~~
3. ~~qq截图的tiff格式暂时有bug~~
4. ~~临时文件夹不使用/tmp 用TempFile解决。~~
