---
doc_type: lab_demo
title: DataGrip 安装与使用参考
concepts: [DataGrip, 安装, 使用]
difficulty: 0.6
prerequisites: [操作系统基础]
author: [覃修交,赵美凤]
date: 2025-08-20
tags: [DataGrip, 安装, 使用]
status: approved
updated: 2026-03-22
---

# DataGrip 安装与使用参考
> 作者：覃修交（22级计算机科学与技术3班）,赵美凤（24级软件工程1班）
> 在[Obelisk Docs：安装 SQL IDE](https://obelus.cc/guide/mysql/ide/)的基础上进行补充。


## 一、产品说明
DataGrip 是 JetBrains 出品的专业 SQL IDE，**非商业用途可免费使用**，支持 MySQL、PostgreSQL、SQL Server 等多种数据库，适合数据库开发与学习使用。

---

## 二、下载地址
官方下载页面：[https://www.jetbrains.com/datagrip/download/](https://www.jetbrains.com/datagrip/download/)
- 选择对应操作系统（Windows/macOS/Linux）的安装包进行下载。

---

## 三、安装步骤（Windows 为例）
1.双击下载的 `.exe` 安装包，进入安装向导。

![aaa图片](../assets/images/4_excellent_labs/datagripimages/aaa.png)

2.选择安装路径（建议默认），点击「下一步」。

![11图片](../assets/images/4_excellent_labs/datagripimages/11.png)

3.安装选项推荐勾选：

- [x] Create Desktop Shortcut（创建桌面快捷方式）
- [x] Add "Open Folder as Project"（添加文件夹右键打开为项目）
- [x] Associate .sql files（关联 .sql 文件）

    无需勾选「Add bin folder to PATH」

![15图片](../assets/images/4_excellent_labs/datagripimages/15.png)

4.开始菜单文件夹保持默认 `JetBrains`，点击「安装」。

![14图片](../assets/images/4_excellent_labs/datagripimages/14.png)     

5.安装完成后勾选「Run DataGrip」，点击「Finish」启动。
![19图片](../assets/images/4_excellent_labs/datagripimages/19.png)    



## 四、首次启动配置
1.**导入设置**：启动后在「Import Settings」界面，选择 **`Do not import settings`**（全新配置）。

![18图片](../assets/images/4_excellent_labs/datagripimages/18.png)    


2.**插件管理（中文设置）**：
    点击左侧 `Plugins`
    ![12图片](../assets/images/4_excellent_labs/datagripimages/12.png)

点击 `Installed`→ 搜索 `Chinese (Simplified) Language Pack`
DataGrip 2025.3.5 版本 已经内置了中文语言包,无需在自己安装

![16图片](../assets/images/4_excellent_labs/datagripimages/16.png)

 之后需要手动设置语言

![13图片](../assets/images/4_excellent_labs/datagripimages/13.png)

---

## 五、新建项目
打开 DataGrip 欢迎界面：  
1.点击 **`+ 新建项目`** 按钮  
2.输入项目名称  
3.选择文件保存路径  
4.点击「确定」，即可进入项目主界面
![bbb图片](../assets/images/4_excellent_labs/datagripimages/bbb.png)

## 六、连接 MySQL 数据库
1.进入 DataGrip 主界面，点击左上方 `主菜单`（3 个竖白点）  →点击`文件`→选择 `数据源` 
![fff图片](../assets/images/4_excellent_labs/datagripimages/fff.png)    
在数据源栏左上角点击 `+` → `MySQL`。
![ggg图片](../assets/images/4_excellent_labs/datagripimages/ggg.png)
2.  **下载驱动**：若提示「下载缺少的驱动程序文件」，点击蓝色链接自动下载 MySQL Connector/J 驱动。
![eee图片](../assets/images/4_excellent_labs/datagripimages/eee.png)    
3.  填写连接信息：  
    - 主机：`localhost`  
    - 端口：`3306`  
    - 用户：`root`（你的 MySQL 用户名）  
    - 密码：你的 MySQL 登录密码
    - 数据库：（可选，填写要连接的具体数据库名）
![kkk图片](../assets/images/4_excellent_labs/datagripimages/kkk.png)
4.  **测试连接**：点击 `测试连接`，若显示 `已成功` 则连接成功。
点击「确定」保存配置，即可在 DataGrip 中管理和操作 MySQL 数据库。
![hhh图片](../assets/images/4_excellent_labs/datagripimages/hhh.png)
## 七、MySQL 数据库的基础管理与表操作
1.在界面左侧的数据库资源管理器中，点击架构数字，并勾选所需的数据库。
![jjj图片](../assets/images/4_excellent_labs/datagripimages/jjj.png)

2.选择其中一个架构即可查看架构中的表等信息。
![nnn图片](../assets/images/4_excellent_labs/datagripimages/nnn.png)

3.可以点击上方的「控制台」图标并选择新建或已有控制台，在其中写入 MySQL 语句进行执行。
![lll图片](../assets/images/4_excellent_labs/datagripimages/lll.png)

4.以添加表为例，除了通过 MySQL 语句外，也可以右键点击架构并选择「新建 > 表」进行快速创建。
![mmm图片](../assets/images/4_excellent_labs/datagripimages/mmm.png)

5.在创建表页面填写表名称、列名称、数据类型和键等信息即可。
![sss图片](../assets/images/4_excellent_labs/datagripimages/sss.png)

## 八、非商业用途授权激活（免费使用）
1.启动选择非商业用途
打开 DataGrip 后，在「试用：剩余 30 天」界面，点击 「学习和教育可免费使用」 按钮，进入非商业用途授权流程。
![1图片](../assets/images/4_excellent_labs/datagripimages/1.png)

2.确认个人非商业用途协议
在「个人非商业用途」页面：
勾选 「学习和教育用途」（或对应非商业用途选项）
阅读并确认授权协议
点击 「仅以非商业用途使用」 蓝色按钮
![2图片](../assets/images/4_excellent_labs/datagripimages/2.png)

3.绑定 / 创建 JetBrains 账号
系统将跳转到 JetBrains 账号授权页面：
选择登录方式（如微信登录）

<img src="../assets/images/4_excellent_labs/datagripimages/6.png" width="60%" style="height: auto;">

输入邮箱地址，将微信与 JetBrains 账号关联若为新用户：接收邮箱验证码并完成验证

<img src="../assets/images/4_excellent_labs/datagripimages/4.png" width="50%" style="height: auto;">

输入个人姓名，点击 「创建账户」

<img src="../assets/images/4_excellent_labs/datagripimages/7.png" width="40%" style="height: auto;">

4.完成授权并返回 IDE
账号验证成功后，页面将显示 「授权成功」 提示，提示语为：
您可以关闭此页面并返回 IDE
关闭浏览器页面，回到 DataGrip 即可完成非商业用途的永久免费激活。

<img src="../assets/images/4_excellent_labs/datagripimages/8.png" width="60%" style="height: auto;">

5.再次确认授权状态
若后续启动 DataGrip，再次进入「个人非商业用途」界面：
- 确认已勾选 **「我同意非商业用途 条款与条件」**
- 点击左下角 **「我已有许可证」** 按钮，即可直接进入软件，无需重复授权

![9图片](../assets/images/4_excellent_labs/datagripimages/9.png)



说明：此授权适用于学习、教育、个人非商业项目，无功能限制，可长期免费使用，需保持 JetBrains 账号登录状态。
