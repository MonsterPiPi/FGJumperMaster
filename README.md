#凡哥带你玩转OpenCV之跳一跳小程序



![output_details.png](http://image.myfange.com/output_details.png-fg)


## 前言

看到之前那么多同学做出来自己的跳一跳的物理外挂， 凡哥也忍不住向自己动手做一个。

终于， 花了好几天的时间做出来了自己的（相对）稳定版本的跳一跳opencv识别程序。



凡哥为了**挑战自己**， 采用的是摄像头采集画面。用**USB摄像头**拍摄画面， 通过`opencv`的videocapture，获取图像， 然后使用`opencv`进行图像处理。

为什么说是挑战自己呢？ 首先摄像头采集的画面， 受到光照的影响， 另外还有镜头本身的畸变， 等等。

例如我向提取背景颜色， 如果是手机截图的话， 背景颜色的RGB像素点的值， 应该都是同一个RGB值。

如果你用的是**USB摄像头**的话， 背景像素有明有暗，大致呈正态分布。所以变相地给自己添加了很多工作量， 但是从学习的角度， 是很棒的一种体验。



凡哥做这件事情一方面是想尝试一下知识付费的模式, 另一方面是想教授大家学习计算机视觉, 总是, 被人认可,被人信任是一件很幸福的事情. 感谢大家为凡哥贡献的"鸡排".

## 我是广告

自己动手用opencv写一个自己的跳一跳物理外挂。
凡哥想尝试一下付费模式，提供完成版的教程与代码，讲解所有涉及的opencv的函数，还有个人辅导，教程定价在24元，(随着学员增加价格会上调, 以本文为准)  感兴趣的同学可以私聊我哦，

零基础也可以学会,python基础，opencv入门教程,凡哥都帮大家整理好了。
加凡哥QQ: **244561792**


## 注意事项



请不要问我任何如何在windows下运行`python`的程序, 如何在`	windows`下编译opencv, 使用什么IDE的问题, 应为凡哥本身桌面系统使用的是Linux, 所以对windows不是很熟悉. 相关的问题, 大家可以在群里相互交流.

另外, 尽量别私聊我, **凡哥想花更多的时间为大家提供更优质的教程.**



教程的文章, 部分我会放在我的个人网站上, 同时也有部分离线文档. 

所有教程都需要离线文档的同学, 请自行将网页另存为`pdf` .  凡哥的个人网站为大家创建了非常好的阅读体验, 请在PC下浏览学习.



请遵守学习秩序, 将文明有礼貌. 对于扰乱教学秩序的同学, 会推群处理.



**此QQ学习群的生命周期为30天, 20180216 - 20180316, 请及时保存群共享里的教学文件.**



## 关于授课

关于授课, 凡哥之前写了一些`python` , `numpy`, `linux`相关的基础入门教程, 在我的网站上(www.myfange.com). 必要的内容我会列在预备知识里.
预备知识请查阅`预备知识_Python_Numpy_Linux.pdf` 文件.


**授课形式**

`源代码` + `文档教程` +` 定时答疑` 

opencv的教程会陆续发布.

为了照顾,学习速度超级快的大牛, 凡哥会将工程文件放到群共享里,  码神们请自行浏览, 看不懂的地方, 截图给我, 我会在教程中说明.

对于初学者, 还是建议大家从基础一点点来.




## 开发环境



如果你手里有树莓派, 凡哥有配好的现成的开发环境, 作为本次课程学院的福利. 需要的话, @我一下, 我放到群共享里.



* `os` 不限，　凡哥使用的是`linux`, 虚拟机装`Ubuntu`凡哥也会很高兴的.


* `python` 3.6
* `numpy` 1.13.3
* `opencv` 3.3.0  我配的树莓派的操作系统有编译好的最新的`3.4.0` 版本



> 后面, 可能我用到了哪些需要安装的包, 后面我再补充.



## 工程目录说明



`smaples` 

这里存放的是通过USB摄像头采集的原始图片.

![sample_raw_01.png](http://image.myfange.com/sample_raw_01.png-fg)

`samples-roi` 

文件夹里存放的是原始图片经过裁减后的 (选中对应的ROI, 部分手机屏幕游戏部分的照片)

![sample_roi_01.png](http://image.myfange.com/sample_roi_01.png-fg)



`output` 

这个文件夹存放的是最后输出的样例, 标注好了棋子的位置跟box的中心.

![jumpmaster_visualization](http://image.myfange.com/jumpmaster_visualization.png-fg)

`output`

 这个文件夹存放的是详细版本的输出样例, 可以看到计算过程中的一些中间图像 (mask 罩层等)

![output_details](http://image.myfange.com/output_details.png-fg)



`代码实验区` 

存放的是写这个工程的时候的实验代码

`FGJumperMster.py`

**核心文件** 图像识别的部分都封装在了这个类中.  凡哥起名为 跳一跳大师. 嘿嘿

`FGJumperMasterTest.py`

这个文件是`FGJumperMaster.py`的测试文件. 你可以通过阅读测试程序的代码了解`FGJumperMaster`的使用方式.

`FGVisionUtil.py`

这里是我写一个一个工具类, 封装了一些图像处理的过程, 自己用这爽, 代码比较整洁.

`SampleCollect.py` 

用于采集图像

![sample_collector.png](http://image.myfange.com/sample_collector.png-fg)

`SampleROI.py`

用于采集图片的局部`ROI` .

也就是从samples中的图片到samples-roi的过程.



![sample_roi_generator.png](http://image.myfange.com/sample_roi_generator.png-fg)





`ThresholdEditorGUI.py`

这是凡哥写的利用`opencv` 的`HighGUI`组件实现的阈值调节工具.

![ThresholdEditorGUI](http://image.myfange.com/ThresholdEditorGUI.png-fg)



