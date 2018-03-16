# 凡哥带你玩转OpenCV之跳一跳小程序



## 前言

历经1个月的准备，凡哥写出了稳定的跳一跳自动运行脚本，可以稳定地识别跳一跳平面的边缘点，分数轻松破万。

同时凡哥也编写了干货满满的**凡哥带你玩转OpenCV之跳一跳主题教程 .**  在凡哥的公司网站上会陆续更新。[myfange.com](http://www.myfange.com)
需要完整教程的同学也可加入**OpenCV广场群：627671914**，查看会员制度。 
 
![opencv jump course](http://b316.photo.store.qq.com/psb?/V109f8591dRph7/nHu2BEnSweKyjOVJQGyWqb9ARt1AbpitANI8PtDs84c!/b/dDwBAAAAAAAA&bo=wAMcAgAAAAAREPo!&rf=viewer_311)

实际上，我们做的这个稳定的跳一跳图像识别程序，用到的都是**基础的图像处理方法**。

非常传统，这些简单的几何体，还不至于劳烦人工智能深度学习。

**基本上，所有涉及的函数，凡哥都已经在课程中讲解过了。** 所以，你直接阅读凡哥写的代码会非常容易。

在这篇文章里，还提到了实现哪部分的代码，需要阅读凡哥的教程的章节号，方便大家查阅。



## 效果展示



![2018-02-22-17-03-19-081616.png](http://image.myfange.com/2018-02-22-17-03-19-081616-mark.png-fg)





## 识别过程与原理介绍



### 步骤1: 利用**SelectROI** 截取棋子的图片，用于色彩统计。

> SelectROI 截取图片的部分区域， 见教程**CH4.1_SelectROI区域选择与图像裁剪-凡哥带你玩转OpenCV** 。


![little_chess.png](http://image.myfange.com/little_chess.png-bk)
 
首先将BGR格式的图片转换为HSV色彩空间。

```python
# 先转换为HSV格式的图片
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

> 颜色空间转换(cvtColor)的详细使用方法见 **CH1.2_通过Matplotlib展示图片-凡哥带你玩转OpenCV**

根据对hsv颜色空间下棋子的颜色分布的观察：

> 颜色分布图的绘制见 **CH4.2_颜色统计与分布曲线绘制-凡哥带你玩转OpenCV** 

![little_chess_hsv_stat.png](http://image.myfange.com/little_chess_hsv_stat.png-fg)



* **H通道** 代表颜色  ，用蓝色曲线绘制 
* **S通道** 代表色彩饱和度， 用绿色曲线绘制
* **V通道** 代表亮度 ， 用红色曲线绘制

观察到颜色的分布后，记录颜色的上下阈值，写在代码里。
 
```python
# 阈值下界
lowerb = (104, 33, 58)
# 阈值上界
upperb = (136, 121, 104)
```

有了上界与下界之后，就可以将图片进行二值化.

```python
mask = cv2.inRange(img_hsv, lowerb, upperb)
```

> 图像二值化（inRange)  见教程 **CH4.3_图像全局二值化与可视化调参-凡哥带你玩转OpenCV**



接下来我们在图像中寻找**固定宽高范围**的矩形区域。

> 轮廓的外接矩形寻找，见教程 **CH5.2_轮廓的外接矩形-凡哥带你玩转OpenCV**



![20180222_demo02_bin_chess.png](http://image.myfange.com/20180222_demo02_bin_chess.png-fg)



如果找到的话，就可以确定棋子的底部中心， 如上图红点所标注。

> 图片的标注与几何图形绘制请参见第二章，**CH2.3_几何图像绘制与文字绘制-凡哥带你玩转OpenCV**

如果找不到的话， 或者图像中存在多个满足宽高要求的连通域， 我们可以使用**模板匹配Template Matching** 进行进一步检索。

> 模板匹配见 **CH6.1_模板匹配-凡哥带你玩转OpenCV**

![template_match_res](http://image.myfange.com/template_match_res.png-fg)

棋子的识别代码的具体实现见文件：`BlackChess.py`。

### 步骤2: 寻找跳一跳平台



> 为了更好更高效的看懂这部分的代码，对numpy的掌握程度要求比较高．
>
> 见教程　[Numpy快速入门-凡哥带你玩转Python科学计算](http://www.myfange.com/p/numpy-quick-start)



首先我们将图片`BGR`三通道， 分别进行Canny算子求得盒子的边缘二值图像，然后将三个通道的边缘图像叠加在一起。

> 你需要了解二值化图片之间的与，或，非等逻辑运算．详见教程**CH4.6_二值化逻辑运算-凡哥带你玩转openCV**

![20180222_demo03.png](http://image.myfange.com/20180222_demo03.png-fg)



接下来我们找到边缘图像中，最顶上的那个轮廓点集合，如下图中红线标注。

> 轮廓的获取与遍历，请参见教程 **CH5.1_获取边缘点集与绘制-凡哥带你玩转OpenCV**

![find_top_point_and_make_sample.png](http://image.myfange.com/find_top_point_and_make_sample.png-fg)

然后还要找到最顶上的顶点，与顶点所在的坐标，如下图绿色圆圈处。

> 

![20180222_next_plat_demo03.png](http://image.myfange.com/20180222_next_plat_demo03.png-fg)

在顶点所在的序号分别向左向右延伸， 找到平台的左顶点**left_point**

![find_left_point_of_box](http://image.myfange.com/find_left_point_of_box.png-fg)



跟平台右顶点**right_point**



![find_right_point_of_box](http://image.myfange.com/find_right_point_of_box.png-fg)

三点确定一个四边形。 根据平行四边形的特性， 我们可以方便地求出来另外一个点的坐标。

```python
# 通过平行四边形的定理 获取下方的点
down_point = (left_point[0]+right_point[0]-top_point[0],left_point[1]+right_point[1]-top_point[1])
```



四个点确定一个外接矩形区域， 在这个矩形区域内检索小白点。如果存在的话， 这个就是中心。

![20180222_white_point_demo02.png](http://image.myfange.com/20180222_white_point_demo02.png-fg)



如果不存在的话， 就将左顶点**left_point**与右顶点**right_point** 中心作为平面中心点。



平台中心点检索详情见`NextJumpPlat.py`



### 步骤3: 计算距离并求得按压延时

有意思的是延迟与距离并不是完全线形的， 随着距离的变大， 比例因子ratio也在变小。

$$ ratio = delay / distance$$

所以按照经验，用一条直线来拟合距离跟`ratio`之间的关系。

首先你需要确定两个点. **这两个参考点需要自己调参。**

```python
pt1 = (800, 1.4) # 距离是800像素的时候， ratio是1.4
pt2 = (300, 1.63) # 距离是300像素的时候， ratio是1.63
```

给定一个距离**distance**, 先求出来在这条直线上对应**distance** 处的比例因子**ratio**

然后再相乘得到延迟时间。

```python
def distance2time(distance):
    '''
        距离与延迟时间不完全成正比，需要添加惩罚项
    '''
    print(distance)
    pt1 = (800, 1.4)
    pt2 = (300, 1.63)


    ratio = pt1[1] - (pt1[1]-pt2[1])*(pt1[0]-distance)/(pt1[0]-pt2[0])
    print("distance: %.2f  ratio=%.2f"%(distance, ratio))

    # 时间必须是整数类型
    return int(distance * ratio)
```



## 准备工作

### 预备0: ADB安装与手机配置

安装ADB驱动与打开手机的USB调试功能
 
> 见教程　**CH3.1_ADB安装过程与ADB部分指令介绍-凡哥带你玩转OpenCV**
>
> 注意： 电脑每次开机都需要重启adb server，手机每次断开连接都需要开启USB调试功能与PTP文件传输。 详情见教程CH3.1。


ADB的功能介绍，命令行使用说明，也在**CH3.1_ADB安装过程与ADB部分指令介绍-凡哥带你玩转OpenCV**中．


为了能够在python中执行ADB指令，我们需要借助python的子进程`subprocess` 模块 。

在使用`subprocess` 之前， 你需要补习一些操作系统的基本概念， 例如什么是管道什么是进程等等。

> 操作系统基本概念，见教程**CH3.2 补习操作系统中的基本概念-凡哥带你玩转OpenCV**



接下来你需要学习`subprocess` 模块使用
 
> 见教程**CH3.3_subprocess模块的使用说明-凡哥带你玩转OpenCV**

我们用python对我们需要用到的几个功能 **截图** 与**模拟点击** 做了一个封装。 在教程**CH3.3**中也有详细说明。

代码见`ADBHelper.py`



### 预备1: 设定手机屏幕分辨率

修改`AutoJump.py` 文件中

```python
# 初始化ADBHelper 传入手机分辨率
adb = ADBHelper(1080, 1920)
```





### 预备2: 替换模板文件

模板匹配不具备变尺度的特性， 如果你的手机分辨率跟我不相同， 就需要手机截图后，用**SelectROI**重新选取。替换`little_chess.png`

> 模板匹配教程，详见**CH6.1模板匹配-凡哥带你玩转OpenCV** 


![little_chess.png](http://image.myfange.com/little_chess.png-bk)

### 预备3: Debug模式

你可以在`AutoJump.py` 中开启或者关闭Debug模式。



### 预备4: 开发环境的搭建



**开发环境详细参数**

- `os` 不限，推荐使用linux（ubuntu，树莓派等）


- `python` 3.6

- `numpy` 1.13.3

- `opencv` 3.3.0 

> 凡哥配的树莓派的操作系统有编译好的最新的`3.4.0` 版本
>
> **如果你已经配置好了linux开发环境并安装好了opencv， 请跳过此部分**



#### 虚拟机镜像

凡哥帮大家配好了带opencv运行环境的Ubuntu跟树莓派两个版本的操作系统。

**镜像文件均可以在我们的会员群里下载。** 树莓派的系统直接拷贝到SD卡中即可。

凡哥配好的Ubuntu虚拟机，你也可以一键导入VirtualBox。

详情见视频教程：

[视频教程-第四节_使用Virtualbox导入凡哥配置好开发环境的虚拟主机](https://www.bilibili.com/video/av18569702/#page=4)

![96_20180117213930](http://image.myfange.com/VisualBox%E6%8B%93%E5%B1%95%E7%9A%84%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85%E4%B8%8EUSB%E6%91%84%E5%83%8F%E5%A4%B4%E8%AF%BB%E5%8F%96_20180117213930.JPG-fg)

#### Linux配置教程

如果你想自己配置的话，凡哥帮大家写好了详细的Ubuntu安装与配置说明。详细步骤放在了凡哥的教学网站上 [www.myfange.com](www.myfange.com)

**建议大家在PC上浏览教程（PC上，bilibili的播放器才能正常使用）**



[在VirtualBox上安装Ubutu16-04的虚拟机-凡哥带你配置OpenCV开发环境](http://www.myfange.com/p/install-ubuntu-in-virtualbox)

> 在本次教程里, 凡哥带大家安装VirtualBox, 介绍了一下VirtualBox与VMWare的不同之处. 教大家如何创建一个虚拟机, 如何分配物理资源等. 然后我们挂载Ubuntu16.04的镜像, 凡哥逐步教大家安装Ubuntu.课程最后, 你可以进入到你自己安装的Ubuntu桌面, 是不是很有成就感.



[在Ubuntu下安装Anaconda科学计算包并运行python程序-凡哥带你配置OpenCV开发环境](http://www.myfange.com/p/install-anaconda-on-ubuntu)

> 在这节课, 凡哥带大家从Anaconda的官网下载sh安装文件, 并在本地运行它. 安装完成之后, 需要添加环境变量PATH到.bashrc下, 接下来我们测试一下anaconda是否安装成功. 最后, 凡哥给大家演示了, 安装Anaconda之后运行IPython与Jupyter Notebook 交互式编程环境.



[Ubuntu下利用Anaconda安装opencv-凡哥带你配置OpenCV开发环境](http://www.myfange.com/p/install-opencv-on-ubuntu-by-anaconda)

> 这篇文章一来教大家如何使用anaconda 来搜索包， 添加channel , 二来也演示配置opencv开发环境的过程。 我们安装来自conda-forge , 我们选择的opencv版本是opencv=3.3.0. 另外, 当你安装完anaconda之后, 管理python包的工具就从pip转变为conda 文章写的比较仓促, 为anaconda指令讲解不是很详细, 请多包涵.



[在VirtualBox虚拟机里使用Opencv获取USB摄像头的图像-凡哥带你配置OpenCV开发环境](http://www.myfange.com/p/virtualbox-opencv-usb-camera-video-capture)

> 在这一讲里， 凡哥将会带大家在virtualbox中运行opencv的程序， 并且读取usb摄像头的图像。 在运行程序之前, 你需要在VirtualBox上安装对应的拓展包. 然后, 凡哥还详细讲解了opencv中调用VideoCapture获取图像并展示在窗口的程序. 通过这篇文章的操作, 你可以检测你的USB设备是否可以在虚拟机里正常读取, 另外, 测试你配置的opencv开发环境是否正常.







## 运行代码

进入工程根目录 ，并执行指令。

```bash
python AutoJump.py
```





## 联系凡哥

**OpenCV广场群**  627671914

![](http://image.myfange.com/微信公众号底部.png-bk)
