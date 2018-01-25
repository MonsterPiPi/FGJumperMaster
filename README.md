#凡哥带你玩转OpenCV之跳一跳小程序


![output](http://image.myfange.com/jumpmaster_visualization.png-fg)
![output_details.png](http://image.myfange.com/output_details.png-fg)


## 前言

看到之前那么多同学做出来自己的跳一跳的物理外挂， 凡哥也忍不住想自己动手做一个。

终于， 花了好几天的时间做出来了自己的（相对）稳定版本的跳一跳opencv识别程序。



凡哥为了**挑战自己**， 采用的是摄像头采集画面。用**USB摄像头**拍摄画面， 通过`opencv`的videocapture，获取图像， 然后使用`opencv`进行图像处理。

为什么说是挑战自己呢？ 首先摄像头采集的画面， 受到光照的影响， 另外还有镜头本身的畸变， 等等。

所以变相地给自己添加了很多工作量， 但是从学习的角度， 是很棒的一种体验。



凡哥做这件事情一方面是想尝试一下知识付费的模式, 另一方面是想教授大家学习计算机视觉, 总是, 被人认可,被人信任是一件很幸福的事情. 感谢大家的支持.


## 注意事项



请不要问我如何在windows下运行`python`的程序, 如何在`	windows`下编译opencv, 使用什么IDE的问题, 因为凡哥本身桌面系统使用的是Linux, 所以对windows不是很熟悉. 相关的问题, 大家可以在群里相互交流.

另外, 尽量别私聊我, **凡哥想花更多的时间为大家提供更优质的教程.**



教程的文章, 部分我会放在我的个人网站上, 同时也有部分离线文档. 

所有教程都需要离线文档的同学, 请自行将网页另存为`pdf` .  凡哥的个人网站为大家创建了非常好的阅读体验, 请在PC下浏览学习.



请遵守学习秩序, 将文明有礼貌. 对于扰乱教学秩序的同学, 会推群处理.



**考虑到大多数同学正在准备期末考试【凡哥带你玩转OpenCV小班精品课第一期】的学习周期由原定的30天延长为44天, 从 2018年1月16日 至 2018年2月28日, 请及时保存群共享里的教学文件.**



## 课程内容

* 在Ubuntu下配置OpenCV开发环境
* OpenCV 教程
    - 第一章  图片读入与HighGUI 初步

    - 第二章  图形绘制与简易上位机制作

    - 第三章  读入视频与半自动跳一跳上位机

    - 第四章  ROI颜色统计与图像二值化

    - 第五章  连通域检索

    - 第六章  训练HaarCascade模型
* 【番外篇】物理外挂之MicroPython实现方案
  注：教学内容结合跳一跳小程序实例，项目式驱动

## 授课形式

* QQ群小班授课
* 每日教程文档 + 操作视频演示
* 课后练习
* 作业批改
* 有问必答

opencv的教程会陆续发布.

为了照顾,学习速度超级快的大牛, 凡哥会将工程文件放到群共享里,  码神们请自行浏览, 看不懂的地方, 截图给我, 我会在教程中说明.

对于初学者, 还是建议大家从基础一点点来.

## 课程福利
* 配好的VitualBox虚拟机，内含跳一跳源代码，直接上手，零配置

* 做作业赢红包

* 赠送【番外篇】物理外挂之MicroPython实现方案

* 学期末参与抽奖

## 课程售价
第一期尝鲜价 24元 （机不可失，失不再来)

## 报名方式
加QQ（244561792），转红包 ，拉你入群

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
