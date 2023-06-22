# SimpleOJ

本项目是一个轻量级 OJ 系统，是南开大学软件学院2023年前端开发课程设计。

整体采用前后端分离开发模式，前端开发使用近几年流行的`Vue.js`框架，后端开发使用`Python`中的`Django RESTful framework`Web 开发框架，判题机利用`Python`实现，部署在 Linux 系统上，数据库使用`MySQL`。最终实现了此轻量级 OJ 系统，具有登陆注册、查看题目、提交代码、查看判题结果等功能，同时实现了简单的权限管理。

## 一、特点

- 前后端分离，避免了静态网页的单一性，同时也使项目结构更加清晰
- 简易、轻量级，便于部署和二次开发
- 包含了一个 OJ 平台应该具有的基本功能，麻雀虽小，五脏俱全

## 二、功能

**1.注册登录功能**

登录页面可以进行登录和注册，登录注册时使用 Element Plus 自带的表单验证。

<img src="images\\register.png" alt="register" style="zoom:67%;" />

<img src="images\\login.png" alt="login" style="zoom:67%;" />

**2.查看题目列表**

主页页面中列举了已经保存在后端的所有题目的列表，支持按照不同的名称对题目进行检索，方便用户根据自己的需求和兴趣寻找适合的题目。

<img src="images\\problems.jpg" alt="register" style="zoom:67%;" />

**3.查看具体的题目信息**

点开某一个题目后，可以查看该题的具体信息，包括题目描述、输入输出、时间空间限制等。

<img src="images\\problem.jpg" alt="register" style="zoom:67%;" />

**4.提交代码**

在代码输入区域，用户可以输入自己的代码并提交。

<img src="images\\code.jpg" alt="register" style="zoom:67%;" />
**5.查看判题结果**

此界面可以动态加载判题结果并显示。

<img src="images\\submit.jpg" alt="register" style="zoom:67%;" />

## 三、前端介绍

前端采用 Vue 的组建式开发，整个前端由若干个组件组成。

```
src: 包含项目的源代码文件
api: 存放与后端通信的API文件。
assets: 存放静态资源，如图片、样式表等。
components: 存放可复用的Vue组件。
router: 存放路由配置文件。
views: 存放页面级的Vue组件，通常与路由对应。
App.vue: 项目的根组件，包含应用的整体结构和布局。
main.js: 项目的入口文件，初始化Vue应用实例并加载所需的插件和组件
public: 包含公共资源和静态文件
index.html: 项目的HTML模板文件
favicon.ico: 网站的图标文件
package.json: 项目的配置文件，包含项目依赖、脚本命令等信息
```

其中，src 目录具体代码结构如下：-**/src/components** 保存了网站主要的控件

- **/src/components/JudgeList**保存了网站判题页面的相关的控件

- **/src/components/SubmitPanel** 保存了网站具体题目页面相关的控件

- **/src/views**存放网站的不同视图组件

- /**src/views/login.vue** 保存了网站的登录页面

- /**src/views/Home.vue** 保存了网站的主页

- /**src/views/SubmitPanel.vue** 保存了网站的具体题目页面

- /**src/views/JudgeList.vue** 保存了网站的判题信息

- **/src/router/index.js** 保存了网站的路由信息

- **/src/api** 保存了后端通信的方法和接口定义

- **/src/App.vue** 保存了网站的入口

- **/src/main.js** 保存了网站的 Js 入口

如果要修改网站，实际上也是添加或修改组件，然后导入到自己的网站中。

## 四、后端介绍

### 1.后端数据库设计

后端模式图如下：

<img src="images\\Diagram.jpg" alt="register" style="zoom:67%;" />
其中值得重点关注的表有：

- user_user：这张表保存的是有关用户的信息
- problem_problem：这张表保存所有的题目信息
- judgestatus_judgestatus：这张表保存判题状态的信息
- judgestatus_casestatus：这张表保存有关测试用例的信息，判题机判题时会用到这张表

user_user 表：

| 属性         | 含义                                          |
| ------------ | --------------------------------------------- |
| username     | 用户名(主键)                                  |
| password     | 密码(Django 自带`pbkdf2_sha256`加密算法)      |
| last_login   | 上次登录时间                                  |
| is_superuser | 是否是超级用户(涉及到权限管理)                |
| first_name   | 名                                            |
| last_name    | 姓                                            |
| email        | 电子邮件                                      |
| is_staff     | 是否是员工(Django 自动生成字段，并不会使用到) |
| is_active    | 是否是激活状态(只有在激活状态下才能正常使用)  |
| date_joined  | 注册的时间                                    |
| type         | 用户类型(1-普通用户 2-管理员 3-超级管理员)    |

problem_problem 表：

| 属性          | 含义                   |
| ------------- | ---------------------- |
| id            | 题目 id(主键)          |
| title         | 题目的标题             |
| description   | 题目描述               |
| input         | 输入要求               |
| output        | 输出要求               |
| inputExample  | 输入样例               |
| outputExample | 输出样例               |
| timeLimit     | 时间限制(以毫秒为单位) |
| memoryLimit   | 空间限制(以字节为单位) |

judgestatus_judgestatus 表：

| 属性         | 含义                                   |
| ------------ | -------------------------------------- |
| id           | id 号(主键)                            |
| result       | 判题结果，不同的数字代表不同的判题结果 |
| time         | 用时                                   |
| memory       | 占用空间                               |
| language     | 提交语言                               |
| submitTime   | 提交时间                               |
| judge        | 该题所属的判题机                       |
| code         | 代码                                   |
| testCase     | 在那个样例出错                         |
| message      | 保存编译错误信息，运行时错误信息等     |
| problemID_id | 外键参考于 problem.id                  |
| username_id  | 外键参考于 user.username               |

judgestatus_casestatus 表：

| 属性       | 含义             |
| ---------- | ---------------- |
| id         | id 号(主键)      |
| statusID   | 所属的提交 ID    |
| username   | 所属的用户       |
| problemID  | 所属的题目       |
| result     | 该样例的判题结果 |
| time       | 该样例所花时间   |
| memory     | 该样例所耗空间   |
| testCase   | 样例名称         |
| caseData   | 样例输入截取     |
| outputData | 样例输出截取     |
| userOutput | 用户输出截取     |

以上数据库基本可以包含此 OJ 系统所需的全部信息。

### 2.后端技术栈

后端使用的 Python 版本号、相关的软件包及版本如下：

`python==3.8.0`、`pymysql==1.0.3`、`django==3.2`、`djangorestframework==3.14.0`、`django-filter==23.2`、`django-cors-headers==4.0.0`

### 3.后端结构

后端的整个结构如下：

```python
|--Backend  # 后端根目录
  |--Backend  #后端项目目录
     |--init.py
     |--asgi.py
     |--setting.py  # 此文件包含项目的设置信息
     |--urls.py  # 此文件包含总路由信息，实现路由分发功能
     |--wsgi.py  # # runserver命令会使用wsgiref模块做简单的web server
  |--users  # 此app实现用户相关接口
  |--problem  # 此app实现题目相关接口
  |--judgeStatus  # 此app实现判题信息相关接口
  |--manage.py  # 后端十分重要的管理文件
  |--requirements.txt  # 后端需要的软件包及版本
```

在每个 app 下，有若干个文件，详细介绍如下：

```python
|--app  # 某一个app的根目录
  |--migrations  # 此文件夹主要保存数据迁移相关记录
  |--__init__.py  # 初始化文件
  |--admin.py  # 后台管理模块相关文件
  |--apps.py  # app配置信息
  |--models.py  # 定义模型
  |--permission.py  # 配置权限管理的文件
  |--serializers.py  # 定义序列化器
  |--tests.py  # Django自带的测试文件
  |--urls.py  # 定义路由，将路由对应到相关的视图
  |--views.py  # 定义视图
```

## 五、判题机介绍

判题部分由判题机与判题机核心组成，在Fedora Linux下部署运行。判题机从数据库中拉取待评测记录，将其发送给判题机核心。
判题机核心基于用户的可执行文件以及标准输入输出目录、资源限制等配置，执行并给出资源消耗情况，并能防止恶意调用。
判题机核心会返回一个 json 数据，代表每个测试点的测试情况。

返回的数据结构如下

```c++
struct judgeResult {
    // 实际消耗时间
    rlim_t realTimeCost;
    // 消耗内存
    rlim_t memoryCost;
    // 消耗 CPU 时间
    rlim_t cpuTimeCost;
    // 执行状态，请参考 RUNNING_CONDITION 枚举类型
    int condition;
};

enum RUNNING_CONDITION {
    RUN_SUCCESS = 1, // 程序通过
    RUNTIME_ERROR, // 运行时错误
    TIME_LIMIT_EXCEED, // 时间超限
    MEMORY_LIMIT_EXCEED, // 内存超限
    OUTPUT_LIMIT_EXCEED, // 输出超过限制
    SEGMENTATION_FAULT,  // 段错误
    FLOAT_ERROR, // 浮点错误
    UNKNOWN_ERROR, // 未知错误
    INPUT_FILE_NOT_FOUND, // 找不到输入文件
    CAN_NOT_MAKE_OUTPUT, // 无法寻找输出
    SET_LIMIT_ERROR, // 设限失败
    NOT_ROOT_USER,  // 非管理员用户
    FORK_ERROR, //fork失败
    CREATE_THREAD_ERROR, //监控线程创建失败
    VALIDATE_ERROR // 数据验证失败
};
```

## 六、开发文档

这里介绍整个项目是如何开发的，方便读者在本地部署运行或者进行二次开发。

### 1.前端开发

**（1）安装 OJ 前端**

在开始前端开发前，需要做一些准备工作。

首先要安装`Nodejs`和`npm`，具体安装教程自行搜索。

接下来我们只需要安装各种库即可，得益于 NPM，这里只需执行一个非常简单的命令即可：

```powershell
cd Frontend
```

```powershell
npm install
```

第一次安装需要等待大概二十多分钟左右，安装完毕后可以执行如下命令来查看前端是否能运行:

```powershell
npm run serve
```

然后打开浏览器访问 **localhost:8080** 如果能看到页面，证明前端已成功安装。

**（2） 添加新页面**

本节将会介绍如何在网站中添加一个自己的页面，并且可以通过地址栏访问它。

在阅读本节前，需要有简单的 Vue 知识。

**（3）编写 Vue 组件**

首先我们在**components**目录中新建一个文件**mycom.vue**，其内容如下：

```vue
<template>
  <welcomemessage></welcomemessage>
  <!-- 注册后的组件，可以直接引用来嵌入到页面中，详见Vue教程 -->
</template>

<script>
import welcomemessage from "@/components /welcomemessage"; //导入现有的组件，或者自己开发的组件
export default {
  name: "mycom",
  components: {
    welcomemessage, //注册组件
  },
  data() {
    return {
      msg: "Hello World", //数据项，详见Vue教程
    };
  },
  created() {},
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
```

如果学过 Vue 简单的组件开发，则会明白代码中内容的含义。

Vue 的组件由三部分组成

1. **template** 网页主体

2. **script** 网页 js

3. **style** 网页的 CSS

具体编写，参考 Vue 教程。由于本 OJ 引入了**ElementPlus**且在**main.js**中进行了全局注册,因此可以直接使用**ElementPlus**的控件。

**（4）添加路由信息**

编写完自己的组件后，如果要给他添加一个路由，则需要修改 **/src/router/** 中的 index.js

首先我们先**import**我们自己的组件，记住路径不能写错。

```javascript
import mycon from "@/components/mycon";
```

然后我们再添加自己的路由信息。我们在**routers**中添加一项内容:

```javascript
{
    path: '/mycon', //路由地址
    name: 'mycon', //路由名称
    component: main //路由对应的控件
},

```

如无意外，我们已经成功的实现自己的页面现在执行 `npm run serve`来运行自己的网站，然后通过浏览器访问`localhost:8080/mycon/`

即可看到自己编写的控件的效果。

### 2.后端开发

整个后端开发再 Windows 10 环境下进行。如果是 Mac，Linux 等操作系统，进行对等的操作即可。

**（1）安装 Python 3.8.0**

如果本地还没有安装过任何版本的 Python，那么直接安装即可。但是仍然建议(尤其对 Windows 用户而言)使用虚拟环境，可以使用 Anaconda 这一备受欢迎的工具，如果使用 PyCharm，也可以使用 PyCharm 创建虚拟环境，以避免多个版本的 Python 带来问题。

接下来将以 Anaconda 创建虚拟环境为例，搭建开发环境。

首先，打开 Anaconda Prompt,创建一个虚拟环境:

```powershell
conda create -n Django python==3.8.0
```

中途若出现询问，按 y 键即可

之后查看环境是否成功创建：

```powershell
conda env list
```

如果出现的列表中包含了刚才创建的环境名称，说明已经成功创建。此时，本地已经拥有了一个 Python 版本为 3.8.0 的运行环境，并且不会影响其他程序的运行。

**（2）安装必要的包**

再次打开 Anaconda Prompt，激活刚才创建的虚拟环境：

```powershell
activate Django
```

如无意外，之后的命令行会以(Django) 开头

进入后端文件夹：

```powershell
cd Backend
```

输入如下命令安装所需的包：

```powershell
pip install -r requirements.txt
```

如无意外，应该会安装成功。

**（3）创建并连接到 MySQL 数据库**

使用 Navicat Premium、MySQL Workbench 等工具或者命令行，创建一个 MySQL 数据库(注意使用 UTF-8 编码)，例如此数据库名字为 oj

接下来，打开如下文件：

`Backend\\Backend\\settings.py`

在以下位置做修改：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oj',  # 刚才创建的数据库的名字
        'USER': os.environ.get("DB_USER") if os.environ.get("DB_USER") else 'user',  # 数据库连接的用户名
        'PASSWORD': os.environ.get("DB_PASSWORD") if os.environ.get("DB_PASSWORD") else 'password',  # 密码
        'HOST': os.environ.get("DB_HOST") if os.environ.get("DB_HOST") else 'localhost',  # 主机名
        'PORT': os.environ.get("DB_PORT") if os.environ.get("DB_PORT") else 3306,  # 端口号
    }
}
```

这样，后端就能成功连接到 MySQL 数据库

**（4）进行数据迁移**

再次打开 Anaconda Prompt，激活虚拟环境：

```powershell
activate Django
```

进行数据迁移，执行下面两个命令：

```powershell
python manage.py makemigrations
```

```powershell
python manage.py migrate
```

如无意外，数据库中会多出若干张表。

**注意！**

由于本项目的 settings.py 中文件中已经完善好了相关的配置，因此不需要进行更多的操作。后续若出现跨域访问问题、用户认证模型错误等问题，可查看报错堆栈信息，自行搜索解决。

**（5）创建一个超级用户**

（注：此步骤主要是为了方便开发，也可以跳过）

为了使用 Django 的后台管理模块方便地进行数据的增删改查，可以创建一个超级用户。

首先输入如下命令：

```powershell
python manage.py createsuperuser
```

然后按照提示输入用户名、电子邮件地址和密码。**注意**，密码在输入时不会显示在终端上，你只需键入并按下回车键即可。

成功创建超级用户后，将收到一条成功的消息。你可以使用该用户的凭据登录到 Django 的管理后台。

**（6）运行后端**

使用如下命令运行后端：

```powershell
python manage.py runserver
```

如无意外，后端会在本地 8000 端口启动，监听并处理所有的请求。

如果刚才创建了超级用户，可以在浏览器输入如下 URL:

> http://127.0.0.1:8000/admin/

如无意外，能够进入后台管理模块。

输入刚才所创建的超级用户的用户名和密码，会看到后台管理界面。

为了获得更多后端定义的权限，点击 Users ,找到刚才创建的用户名，在表单中找到 Type ，将其修改为 3

之后，这个用户已经获得了后端的所有访问权限，可以在后台管理界面上方便地进行数据的增删改查。

如果以上过程均顺利进行，那么说明后端已经在本地部署成功！此时如果运行前端，那么前端和后端就能正常进行交互。

你还可以在 PyCharm 或者 VS Code 上配置之前创建的虚拟环境，方便地查看、运行代码。

**（7）修改后端**

**添加一个模型**

如果要添加一个模型，只需要创建相应的模型类，添加相应的序列化器，再添加对应的路由、视图、等信息，还可以利用分页、过滤、限流等中间件实现一些更高级的功能。对于老手而言是常规无奇的操作。

**添加一个新的 app**

如果要添加一个新的 app，在终端输入以下命令即可：

```powershell
python manage.py startapp myapp
```

之后进行相应的开发即可。

不要忘了进行数据迁移：

```powershell
python manage.py makemigrations
```

```powershell
python manage.py migrate
```

### 3.判题机开发

Judger/code/data文件夹中用于存放题目所有测试数据的压缩包。
在Judger文件夹中，通过执行如下命令来启动判题机：

```powershell
sudo python main.py
```

