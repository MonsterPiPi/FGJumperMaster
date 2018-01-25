
## 凡哥带你玩转OpenCV之跳一跳主题 - 授课计划

没有很多高大上的算法, 都是基础操作, 都是基础， 凡哥严肃的教学贴。重点不是教你如何做外挂的好嘛， 严肃。

![http://image.myfange.com/jumpmaster_visualization.png-fg](http://image.myfange.com/jumpmaster_visualization.png-fg)



## Python基础篇

* 在Win10下安装Anaconda并配置Anaconda环境变量
* 在Ubuntu下配置Anaconda
* 变量
* 列表与元组
* 字典
* 字符串
* 字节与字节数组
* 基本控制流语句
* Import系统之同目录跨文件的引用
* Import系统之跨目录引用(内置简单的面向对象教程)



## Python科学计算入门之Numpy

> 主要讲解numpy, matplotlib与scipy会在课程中穿插讲解.



* ndarray的初始化
* ndarray属性
* ndarray的数据类型
* ndarray切片(索引)操作
* ndarray变形
* ndarray拼接 (横向, 纵向)
* ufunc 全局函数
* broadcast 广播
* np.linalg线形代数包-numpy包选讲
* np.random 随机函数包-numpy包选讲



## Linux基础入门



* CLI vs GUI
* 初识终端
* 文件系统,文件操作
* 如何查询linux使用手册
* 在Linux下运行你的第一个Python程序



## 在Ubuntu下配置opencv开发环境

> 虚拟机采用VirtualBox



* 在VirtualBox上安装Ubutu16-04的虚拟机
* 在Ubuntu下安装Anaconda科学计算包并运行python程序
* Ubuntu下利用Anaconda安装opencv
* 在VirtualBox虚拟机里使用Opencv获取USB摄像头的图像



彩蛋 x2



## 正八经的OpenCV教程



![http://image.myfange.com/output_details.png-fg](http://image.myfange.com/output_details.png-fg)



### CH1 图片读入与HighGUI 初步

* CH1.1_读入图片并显示图片的相关属性
* CH1.2_通过Matplotlib展示图片_
* CH1.3_通过HighGUI展示图片
* CH1.4_图片保存imwrite

### CH2 图形绘制与简易上位机制作

* CH2.1_花式创建空白画布-凡哥带你玩转opencv

* CH2.2_通过HighGUI的Trackbar制作可变色背景

* CH2.3_几何图像绘制与文字绘制

* CH2.4_鼠标事件监听与自制绘图板

  ​

### CH3 读入视频与半自动跳一跳上位机

* CH3.1_使用USB摄像头读入视频 
* CH3.2_使用adb驱动读入手机的实时图像并模拟点击
* CH3.3_**跳一跳实战** 利用HighGUI中的鼠标事件
* CH3.4_**跳一跳实战** 计算距离, 并转换成时间


* CH3.5_**跳一跳实战** 跳一跳的半自动玩法鼠标点击计算距离
* CH3.6_采集图像样本与样本标注(为训练做准备)



### CH4 ROI颜色统计与图像二值化 



* CH4.1 Select ROI区域选择与图像裁剪
* CH4.2 颜色统计与分布曲线绘制
* CH4.3 利用高斯分布拟合颜色分布曲线
* CH4.4 图像二值化的几种方法
* CH4.5 二值化图像的逻辑运算
* CH4.6 **跳一跳实战**  扣除背景与盒子阴影



### CH5 联通域检索

* CH5.1 检索矩形连通域
* CH5.2 **跳一跳实战** 计算棋子底部的中心点
* CH5.3 获取连通域的多边形点集
* CH5.4 多个连通域的选择与多边形点集的生成
* CH5.5 **跳一跳实战** 获取最顶部的盒子(连通域), 以及可能会遇到的问题
* CH5.6 **跳一跳实战** 计算距离, 并转换成时间
* CH5.7 **跳一跳实战** FGJumperMaster工具类详解
* CH5.8 **跳一跳实战** 编写测试, 测试算法



### CH6 训练HaarCascade模型

* CH6.1_HaarCascade简介
* CH6.2_快速调用人脸识别函数
* CH6.3_如何训练自己的HaarCascade模型并生成xml文件
* CH6.4_**跳一跳实战** 利用CH3搜集的样本集合训练自己的HaarCascade模型
* ？ (神秘章节)



## 物理外挂之MicroPython实现方案

> ps: 可以使用openmv  io也够用



* DIY电容笔与物理原理介绍


* 利用MicroPython进行舵机控制
*  micropython与ubuntu的通信
*  通信协议的确定与二进制数据的打包

