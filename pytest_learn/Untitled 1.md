目录

```
mumunote
├─ .git
├─ .idea
├─ app
│    ├─ __init__.py
│    ├─ app.py
│    ├─ config
│    │    ├─ __init__.py
│    │    ├─ __pycache__
│    │    ├─ config.py
│    │    └─ ue_config.py
│    └─ settings.py
├─ common
│    ├─ __init__.py
│    ├─ database.py
│    ├─ email_utils.py
│    ├─ redis_demo.py
│    ├─ redisdb.py
│    ├─ response_message.py
│    └─ utils.py
├─ controller
│    ├─ __init__.py
│    ├─ article.py
│    ├─ favorite.py
│    ├─ feedback.py
│    ├─ index.py
│    ├─ personal.py
│    ├─ redis_user.py
│    └─ user.py
├─ log
│    └─ mumunote.log
├─ main.py
├─ model
│    ├─ __init__.py
│    ├─ article.py
│    ├─ favorite.py
│    ├─ feedback.py
│    └─ user.py
├─ requirements.txt
├─ resource
│    ├─ css
│    │    ├─ article-info.css
│    │    ├─ base.css
│    │    ├─ index.css
│    │    ├─ login.css
│    │    ├─ new-article.css
│    │    └─ personal_center.css
│    ├─ font
│    │    ├─ demo.css
│    │    ├─ demo_index.html
│    │    ├─ iconfont.css
│    │    ├─ iconfont.js
│    │    ├─ iconfont.json
│    │    ├─ iconfont.ttf
│    │    ├─ iconfont.woff
│    │    └─ iconfont.woff2
│    ├─ images
│    │    ├─ article
│    │    ├─ article-desc.png
│    │    ├─ article-header.jpg
│    │    ├─ article-logo.png
│    │    ├─ article_icon.jpg
│    │    ├─ article_img.jpeg
│    │    ├─ author.jpeg
│    │    ├─ author_profile_pic.jpeg
│    │    ├─ handbook-desc.png
│    │    ├─ handbook-logo.png
│    │    ├─ headers
│    │    ├─ image-upload.png
│    │    ├─ new.png
│    │    ├─ personal_background.png
│    │    ├─ second_article.jpeg
│    │    └─ user_picture.jpeg
│    ├─ js
│    │    ├─ article-info.js
│    │    ├─ axios.min.js
│    │    ├─ header.js
│    │    ├─ index.js
│    │    ├─ new-article.js
│    │    └─ sub-header.js
│    ├─ plugins
│    │    ├─ bootstrap
│    │    └─ ueditor-plus
│    └─ upload
│           ├─ article-header-20230501_005619.jpg
│           └─ article-header-20230501_005809.jpg
├─ template
│    ├─ article-info.html
│    ├─ index.html
│    ├─ new-article.html
│    ├─ personal_center.html
│    └─ public
│           ├─ header.html
│           └─ sub-header.html
```

有些图片文件过多，没有显示

文件的具体内容：(不给出内容的文件，内容为空)

## main.py

```
from app.app import create_app
import logging

app = create_app()

if __name__ == '__main__':
   logging.info("我是info的日志")
   logging.debug("我是debug的日志")

   app.run()

```



## app文件夹

```
app
├─ __init__.py
├─ app.py
├─ config
│    ├─ __init__.py
│    ├─ config.py
│    └─ ue_config.py
└─ settings.py
```

### app.app.py

```
import os

from flask import Flask
def create_app():
    app = Flask(__name__,template_folder="../template",static_url_path="/",static_folder="../resource")
    # 注册蓝图
    init_blueprint(app)
    app.config['SECRET_KEY'] = os.urandom(24)
    return app

def init_blueprint(app):
    from controller.user import user
    app.register_blueprint(user)

    from controller.index import index
    app.register_blueprint(index)

    from controller.article import article
    app.register_blueprint(article)

    from controller.favorite import favorite
    app.register_blueprint(favorite)

    from controller.feedback import feedback
    app.register_blueprint(feedback)

    from controller.personal import personal
    app.register_blueprint(personal)

    from controller.redis_user import redis_user
    app.register_blueprint(redis_user)
```

### app.settings.py

```
env="test"
```

### `app.config.config.py`

```
# 全局通用配置
class Config(object):
    db_url = "mysql+pymysql://admin1:123@192.168.101.66:3306/flask_db"
    # 前端页面显示的条数
    page_count = 10
    # 配置一下文章图片的存储路径
    article_header_image_path = "/images/article/header/"

    email_name = '42197393@qq.com'  # 发送方邮箱
    passwd = 'aqkhnufqifxkbijf'  # 填入发送方邮箱的授权码
    # 配置一下头像存储路径
    user_header_image_path = "/images/headers/"

    label_types = {
        "recommend": {"name": "请选择需要投递的栏目", "selected": "selected"},
        "auto_test": {"name": "自动化测试", "selected": "no-selected"},
        "python": {"name": "Python", "selected": "no-selected"},
        "java": {"name": "Java", "selected": "no-selected"},
        "function_test": {"name": "功能测试", "selected": "no-selected"},
        "perf_test": {"name": "性能测试", "selected": "no-selected"},
        "funny": {"name": "幽默段子", "selected": "no-selected"},
    }
    article_types = {
        "recommend": {"name": "请选择", "selected": "selected"},
        "first": {"name": "首发", "selected": "no-selected"},
        "original": {"name": "原创", "selected": "no-selected"},
        "other": {"name": "其它", "selected": "no-selected"},
    }
    article_tags = ["Html5","Angular","JS","CSS3","Sass/Less",
                    "JAVA","Python","Go","C++","C#","MySQL",
                    "Oracle","MongoDB","Android","Unity 3","DCocos2d-x"]

    # 配置redis
    REDIS_HOST = '192.168.1.129'
    REDIS_PORT = 6379
    REDIS_PASSWORD = ''
    REDIS_POLL = 10
    REDIS_DB = 2
    REDIS_DECODE_RESPONSES = True

# 测试环境
class TestConfig(Config):
    # db_url = ""
    if_echo=True
    LOG_LEVEL="DEBUG"

class ProductionConfig(Config):
    if_echo=False
    LOG_LEVEL = "INFO"

config = {
    "test":TestConfig,
    "prop":ProductionConfig
}
```

### app.config.ue_config.py

```
UECONFIG = {
    # 编辑器初始化内容
    "initialContent": '<p>我是初始化内容，设不设置都可以</p>',
    # 初始化编辑器宽度,默认 1000
    "initialFrameWidth":700,
    # 初始化编辑器高度,默认 320
    # "initialFrameHeight":1000,
    # ##### 宽度和高度设置都没好用 ########
    # 初始化时，是否让编辑器获得焦点，默认为 false
    "focus":True,
# #      执行上传图片的action名称，默认值：uploadimage
    "imageActionName": "image",
    # #  提交的图片表单名称，默认值：upfile
    "imageFieldName": "file",
    # #  上传大小限制，单位B，默认值：2048000
    "imageMaxSize": 10485760,
    # #  上传图片格式显示，默认值：[".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    "imageAllowFiles": [
        ".jpg",
        ".png",
        ".jpeg"
    ],
    # #  是否压缩图片,默认是true
    "imageCompressEnable": True,
    # #  图片压缩最长边限制，默认值：1600
    "imageCompressBorder": 5000,
    # #  插入的图片浮动方式，默认值：none
    "imageInsertAlign": "none",
    # #  图片访问路径前缀，默认值：空
    "imageUrlPrefix": "",

    #  执行上传涂鸦的action名称，默认值：uploadscrawl
    "scrawlActionName": "crawl",
    #  提交的图片表单名称，默认值：upfile
    "scrawlFieldName": "file",
    #  上传大小限制，单位B，默认值：2048000
    "scrawlMaxSize": 10485760,
    #  图片访问路径前缀，默认值：空
    "scrawlUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "scrawlInsertAlign": "none",

    #  执行上传截图的action名称，默认值：uploadimage
    "snapscreenActionName": "snap",
    #  图片访问路径前缀
    "snapscreenUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "snapscreenInsertAlign": "none",

    #  例外的图片抓取域名
    "catcherLocalDomain": [
        "127.0.0.1",
        "localhost"
    ],
    #  执行抓取远程图片的action名称，默认值：catchimage
    "catcherActionName": "catch",
    #  提交的图片列表表单名称，默认值：source
    "catcherFieldName": "source",
    #  图片访问路径前缀，默认值：空
    "catcherUrlPrefix": "",
    #  上传保存路径,可以自定义保存路径和文件名格式，默认值：{filename}{rand:6}
    "catcherMaxSize": 10485760,
    #  抓取图片格式显示，默认值：[".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    "catcherAllowFiles": [
        ".jpg",
        ".png",
        ".jpeg"
    ],

    #  执行上传视频的action名称，默认值：uploadvideo
    "videoActionName": "video",
    #  提交的视频表单名称，默认值：upfile
    "videoFieldName": "file",
    #  视频访问路径前缀
    "videoUrlPrefix": "",
    #  上传大小限制，单位B，默认值：102400000
    "videoMaxSize": 104857600,
    #  上传视频格式显示
    "videoAllowFiles": [
        ".mp4"
    ],

    #  执行上传文件的action名称，默认值：uploadfile
    "fileActionName": "file",
    #  提交的文件表单名称，默认值：upfile
    "fileFieldName": "file",
    #  文件访问路径前缀
    "fileUrlPrefix": "",
    #  上传保存路径,可以自定义保存路径和文件名格式，默认值：{filename}{rand:6}
    "fileMaxSize": 104857600,
    #  上传文件格式显示
    "fileAllowFiles": [
        ".zip",
        ".pdf",
        ".doc"
    ],

    #  执行图片管理的action名称，默认值：listimage
    "imageManagerActionName": "listImage",
    #  每次列出文件数量
    "imageManagerListSize": 20,
    #  图片访问路径前缀
    "imageManagerUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "imageManagerInsertAlign": "none",
    #  列出的文件类型
    "imageManagerAllowFiles": [
        ".jpg",
        ".png",
        ".jpeg"
    ],

    #  执行文件管理的action名称，默认值：listfile
    "fileManagerActionName": "listFile",
    #  指定要列出文件的目录
    "fileManagerUrlPrefix": "",
    #  每次列出文件数量
    "fileManagerListSize": 20,
    #  列出的文件类型
    "fileManagerAllowFiles": [
        ".zip",
        ".pdf",
        ".doc"
    ],

    #  公式配置
    "formulaConfig": {
        #  公式渲染的路径
        "imageUrlTemplate": "https://latex.codecogs.com/svg.image?{}"
    }
}

#  发表评论的ue配置

FEEDBACK_UECONFIG = {
    # 编辑器初始化内容
    "initialContent": '<p>请在此发表您的评论</p>',
    # 初始化编辑器宽度,默认 1000
    "initialFrameWidth":670,
    # 初始化编辑器高度,默认 320
    # "initialFrameHeight":1000,
    # ##### 宽度和高度设置都没好用 ########
    # 初始化时，是否让编辑器获得焦点，默认为 false
    "focus":True,
# #      执行上传图片的action名称，默认值：uploadimage
    "imageActionName": "image",
    # #  提交的图片表单名称，默认值：upfile
    "imageFieldName": "file",
    # #  上传大小限制，单位B，默认值：2048000
    "imageMaxSize": 10485760,
    # #  上传图片格式显示，默认值：[".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    "imageAllowFiles": [
        ".jpg",
        ".png",
        ".jpeg"
    ],
    # #  是否压缩图片,默认是true
    "imageCompressEnable": True,
    # #  图片压缩最长边限制，默认值：1600
    "imageCompressBorder": 5000,
    # #  插入的图片浮动方式，默认值：none
    "imageInsertAlign": "none",
    # #  图片访问路径前缀，默认值：空
    "imageUrlPrefix": "",

    #  执行上传涂鸦的action名称，默认值：uploadscrawl
    "scrawlActionName": "crawl",
    #  提交的图片表单名称，默认值：upfile
    "scrawlFieldName": "file",
    #  上传大小限制，单位B，默认值：2048000
    "scrawlMaxSize": 10485760,
    #  图片访问路径前缀，默认值：空
    "scrawlUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "scrawlInsertAlign": "none",

    #  执行上传截图的action名称，默认值：uploadimage
    "snapscreenActionName": "snap",
    #  图片访问路径前缀
    "snapscreenUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "snapscreenInsertAlign": "none",

    #  例外的图片抓取域名
    "catcherLocalDomain": [
        "127.0.0.1",
        "localhost"
    ],
    #  执行抓取远程图片的action名称，默认值：catchimage
    "catcherActionName": "catch",
    #  提交的图片列表表单名称，默认值：source
    "catcherFieldName": "source",
    #  图片访问路径前缀，默认值：空
    "catcherUrlPrefix": "",
    #  上传保存路径,可以自定义保存路径和文件名格式，默认值：{filename}{rand:6}
    "catcherMaxSize": 10485760,
    #  抓取图片格式显示，默认值：[".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    "catcherAllowFiles": [
        ".jpg",
        ".png",
        ".jpeg"
    ],

    #  执行上传视频的action名称，默认值：uploadvideo
    "videoActionName": "video",
    #  提交的视频表单名称，默认值：upfile
    "videoFieldName": "file",
    #  视频访问路径前缀
    "videoUrlPrefix": "",
    #  上传大小限制，单位B，默认值：102400000
    "videoMaxSize": 104857600,
    #  上传视频格式显示
    "videoAllowFiles": [
        ".mp4"
    ],

    #  执行上传文件的action名称，默认值：uploadfile
    "fileActionName": "file",
    #  提交的文件表单名称，默认值：upfile
    "fileFieldName": "file",
    #  文件访问路径前缀
    "fileUrlPrefix": "",
    #  上传保存路径,可以自定义保存路径和文件名格式，默认值：{filename}{rand:6}
    "fileMaxSize": 104857600,
    #  上传文件格式显示
    "fileAllowFiles": [
        ".zip",
        ".pdf",
        ".doc"
    ],

    #  执行图片管理的action名称，默认值：listimage
    "imageManagerActionName": "listImage",
    #  每次列出文件数量
    "imageManagerListSize": 20,
    #  图片访问路径前缀
    "imageManagerUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "imageManagerInsertAlign": "none",
    #  列出的文件类型
    "imageManagerAllowFiles": [
        ".jpg",
        ".png",
        ".jpeg"
    ],

    #  执行文件管理的action名称，默认值：listfile
    "fileManagerActionName": "listFile",
    #  指定要列出文件的目录
    "fileManagerUrlPrefix": "",
    #  每次列出文件数量
    "fileManagerListSize": 20,
    #  列出的文件类型
    "fileManagerAllowFiles": [
        ".zip",
        ".pdf",
        ".doc"
    ],

    #  公式配置
    "formulaConfig": {
        #  公式渲染的路径
        "imageUrlTemplate": "https://latex.codecogs.com/svg.image?{}"
    }
}
```



## common文件夹

```
common
├─ __init__.py
├─ __pycache__
├─ database.py
├─ email_utils.py
├─ redis_demo.py
├─ redisdb.py
├─ response_message.py
└─ utils.py
```

### `__init__.py`

```
import logging
from logging.handlers import RotatingFileHandler
from app.config.config import config
from app.settings import env

# 增加日志的配置
def set_log():
    config_class = config[env]

    # 设置日志的等级
    logging.basicConfig(level=config_class.LOG_LEVEL)
    # 创建日志记录器 ,指定日志的保存路径、每个日志文件的最大大小、保存的日志个数
    file_log_handler = RotatingFileHandler("log/mumunote.log",maxBytes=1024*1024*300,backupCount=10)
    # 创建日志记录的格式
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d %(message)s")
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


set_log()


```

### database.py

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from app.config.config import config
from app.settings import env
print(env)
def db_connect():
    # 创建一个引擎，目的是连接到我们的数据库上
    config_class = config[env]
    print(config_class)
    engine = create_engine(config_class.db_url,echo=config_class.if_echo,pool_size=10,max_overflow=30)
    # 打开数据库的连接会话
    session = sessionmaker(engine,autoflush=False)
    # 保证线程安全
    db_session = scoped_session(session)
    # 获取基类
    Base = declarative_base()
    return db_session,Base,engine

```

### email_utils.py

```
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config.config import config
from app.settings import env

def gen_email_code():
    list = random.sample(string.ascii_letters+string.digits, 6)
    return "".join(list)

def send_email(email,code):
    email_name = config[env].email_name  # 发送方邮箱
    passwd = config[env].passwd  # 填入发送方邮箱的授权码
    # 不要，千万不要写我的授权码，你一定要写你自己的授权码！！！

    # 你要把邮件发给谁
    msg_to = email

    # 正文
    content = """
    慕慕手记注册验证码是:<h1 style='color:red'>{}</h1>
    """.format(code)
    msg = MIMEMultipart()
    msg["Subject"] = "慕慕手记验证码"
    # msg["From"] = "慕慕手记"
    msg["From"] = email_name
    msg["To"] = msg_to
    # 发送邮件正文，html格式的
    msg.attach(MIMEText(content, "html", "utf-8"))
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮箱服务器及端口号
    s.login(email_name, passwd)
    s.sendmail(email_name, msg_to, msg.as_string())



```

### redis_demo.py

```
# pip install redis
import redis

# 不推荐这么写
# red = redis.Redis(host='192.168.1.129',port=6379,db=1)

# 使用连接池的方式进行连接，这样它就会对我们的连接进行一个管理
# 推荐这么写
# decode_responses 这个参数如果不加，下边就给你返回bytes，需要转换才能看到中文
pool = redis.ConnectionPool(host='192.168.1.129',port=6379,db=1,decode_responses=True)
redis_client = redis.Redis(connection_pool=pool)
# 字符串类型的处理
redis_client.set("name","大周老师")  # 单独设置一个值
print(redis_client.get("name"))

redis_client.mset({"age":18,"address":"北京"})
print(redis_client.mget("name","age","address"))  # 我们同时获取多个值的时候，这里返回的是列表类型
print(redis_client.exists("name"))  # 存在是1，不存在是0
print(redis_client.exists("myname"))

print(redis_client.get("myname"))
print(redis_client.dbsize())
print(redis_client.lastsave())

#==========================hash类型操作===========================
# 新增一个
redis_client.hset(name="userHash",key="username",value="dazhoulaoshi")
# 新增多个
redis_client.hset(name="userHash2",mapping={"username":"大周老师",
                                            "password":"123456",
                                            "nickname":"大大",
                                            "address":"北京"})

print(redis_client.hget("userHash2","username"))
print(redis_client.hgetall("userHash2"))
#==========================list类型、set操作===========================
redis_client.rpush("numberRight",1,2,3,4,5,6)
redis_client.lpush("numberLeft",1,2,3,4,5,6)

# 这里越打印越长，是因为每一次我们运行代码的时候都会往numberRight里边重新放1到6
for i in range(redis_client.llen("numberRight")):
    print(redis_client.lindex("numberRight",i))
redis_client.sadd("setNum",11,12,13,14)
set_number = redis_client.smembers("setNum")
print(set_number)
for i in set_number:
    print(i)
#==========================zset操作===========================
redis_client.zadd("myzset",{"v1":10,"v2":20,"v3":30})
r = redis_client.zrangebyscore("myzset",20,30)
print(r)
r = redis_client.zrangebyscore("myzset",20,30,withscores=True)
print(r)
# 差具体成员的索引值，或者叫排名也行
print(redis_client.zrank("myzset","v1"))
```

### redisdb.py

```
from datetime import datetime

from app.config.config import config
from app.settings import env
import redis

def redis_connect():
    redis_config = config[env]
    pool = redis.ConnectionPool(
        host=redis_config.REDIS_HOST,
        port=redis_config.REDIS_PORT,
        db=redis_config.REDIS_DB,
        decode_responses=redis_config.REDIS_DECODE_RESPONSES
    )
    return redis.Redis(connection_pool=pool)

# 一次性把mysql中的用户数据初始化到redis中

from common.database import db_connect
from app.config.config import config
from app.settings import env
from model.user import User

db_session,Base,engine = db_connect()

def model_list(result):
    list = []
    for row in result:
        dict = {}
        for k, v in row.__dict__.items():
            if not k.startswith("_sa_"):
                if isinstance(v, datetime):
                    v = v.strftime("%Y-%m-%d %H:%M:%S")
                dict[k] = v
        list.append(dict)
    return list


def mysql_to_redis_string():
    redis_client = redis_connect()
    result = db_session.query(User).all()
    # 把这个result需要转换成 [{},{},{}]
    user_list = model_list(result)
    for user in user_list:
        redis_client.set("user:"+user["username"],str(user))

# mysql_to_redis_string()

def mysql_to_redis_hash():
    redis_client = redis_connect()
    result = db_session.query(User).all()
    # 把这个result需要转换成 [{},{},{}]
    user_list = model_list(result)
    for user in user_list:
        redis_client.hset("hash_user:" + user["username"], user["username"],user["password"])

# mysql_to_redis_hash()

```

### response_message.py

```
class UserMessage():
    """
    我们在企业当中，一般每个企业都会对响应的状态码做出一些规定
    比如说，用户响应的都以1开头，然后规定成功了 {status:1000,data:'asdf'}
    错误的状态码1002
    其它状态码1001

    """
    @staticmethod
    def success(data):
        return {"status":1000,"data":data}

    @staticmethod
    def error(data):
        return {"status": 1002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 1001, "data": data}

# article文章的状态 就以2开头
class ArticleMessage():
    @staticmethod
    def success(data):
        return {"status":2000,"data":data}
    @staticmethod
    def save_success(article_id,data):
        return {"status":2003,"article_id":article_id,"data":data}

    @staticmethod
    def error(data):
        return {"status": 2002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 2001, "data": data}


# 收藏的就以3开头
class FavoriteMessage():
    @staticmethod
    def success(data):
        return {"status":3000,"data":data}

    @staticmethod
    def error(data):
        return {"status": 3002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 3001, "data": data}



# 评论的就以4开头
class FeedbackMessage():
    @staticmethod
    def success(data):
        return {"status":4000,"data":data}

    @staticmethod
    def error(data):
        return {"status": 4002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 4001, "data": data}

# 个人中心的就以5开头
class PersonalMessage():
    @staticmethod
    def success(data):
        return {"status":4000,"data":data}

    @staticmethod
    def error(data):
        return {"status": 4002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 4001, "data": data}

```

### utils.py

```
from datetime import datetime
import random
import string
from io import BytesIO

# 这个PIL就是pillow  pip install pillow
from PIL import Image, ImageFont, ImageDraw


class ImageCode():

    def get_text(self):
        # list = random.sample("123456789asdfghjk",4)
        list = random.sample(string.ascii_letters+string.digits,4)
        # print(list)
        return "".join(list)

    def rand_color(self):
        # rgb的颜色
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return red,green,blue

    def draw_lines(self,draw,num,width,height):
        for i in range(num):
            x1 = random.randint(0,width)
            y1 = random.randint(0,height)
            x2 = random.randint(0,width)
            y2 = random.randint(height,height)
            draw.line(((x1,y1),(x2,y2)),fill="black",width=2)

    def draw_verify_code(self):
        # 生成随机字符串
        code = self.get_text()
        print(code)
        # 设置图片的宽和高 ,在实际项目当中最好跟前端显示图片的大小一致，这样就不用前端再重写图片大小了
        width,height = 80,38
        im = Image.new("RGB",(width,height),"white")
        font = ImageFont.truetype(font="C:\Windows\Fonts\Arial.ttf",size=20)
        draw = ImageDraw.Draw(im)
        # 绘制字符串
        for i in range(4):
            draw.text((random.randint(3,10)+15*i,random.randint(3,10)),
                      text=code[i],fill=self.rand_color(),font=font)
        # 绘制干扰线
        self.draw_lines(draw,2,width,height)

        # im.show()
        return im,code

    def get_code(self):
        image,code = self.draw_verify_code()
        buf = BytesIO()
        image.save(buf,"jpeg")
        image_b_string = buf.getvalue()
        return code,image_b_string

# image_code = ImageCode()
# image_code.draw_verify_code()

def model_to_json(result):
    dict = {}
    for k,v in result.__dict__.items():
        if not k.startswith("_sa_"):
            if isinstance(v,datetime):
                v = v.strftime("%Y-%m-%d %H:%M:%S")
            dict[k] = v
    return dict

# ue图片压缩
def compress_image(source,dest,width=1200):
    im = Image.open(source)
    # 获取图片的宽和高
    x,y = im.size
    if x>width:
        # 进行等比例缩放
        ys = int(y*width/x)
        xs = width
        # 调整图片大小
        temp = im.resize((xs,ys),Image.ANTIALIAS)
        temp.save(dest,quality=80)
    else:
        im.save(dest,quality=80)
```



## controller

```
controller
├─ __init__.py
├─ article.py
├─ favorite.py
├─ feedback.py
├─ index.py
├─ personal.py
├─ redis_user.py
└─ user.py
```

### article.py

```
import json
import random
import time

from flask import Blueprint, render_template, request, session, jsonify, make_response, url_for
import logging

from app.config.config import config
from app.settings import env
from common import response_message
from common.utils import compress_image, model_to_json
from model.article import Article
from model.favorite import Favorite
from model.feedback import Feedback
from model.user import User

article = Blueprint("article",__name__)
label_types = config[env].label_types
article_types = config[env].article_types
article_tags = config[env].article_tags
@article.before_request
def article_before_request():
    url = request.path
    is_login = session.get("is_login")
    if url.startswith("/article") and "new" in url and is_login != 'true':
        response = make_response("登录重定向",302)
        response.headers["Location"] = url_for("index.home")
        return response



@article.route("/detail")
def article_detail():
    article_id = request.args.get("article_id")
    article = Article()
    # 获取文章的所有信息
    article_content = article.get_article_detail(article_id)
    article_tag_string = article_content.article_tag
    article_tag_list = article_tag_string.split(",")


    # 获取文章作者信息
    user = User()
    user_info = user.find_by_userid(article_content.user_id)
    feedback_data_list = Feedback().get_feedback_user_list(article_id)

    is_favorite=1

    if session.get("is_login") == "true":
        user_id = session.get("user_id")
        is_favorite = Favorite().user_if_favorite(user_id,article_id)
    # 查询评论的数量
    feedback_count = Feedback().get_article_feedback_count(article_id)

    # 相关文章的功能
    about_article = article.find_about_article(article_content.label_name)
    return render_template("article-info.html",
                           article_content=article_content,
                           user_info=user_info,
                           is_favorite=is_favorite,
                           article_tag_list=article_tag_list,
                           about_article=about_article,
                           feedback_data_list=feedback_data_list,
                           feedback_count=feedback_count)

@article.route("/article/new")
def article_new():
    user_id = session.get("user_id")
    # 我的草稿相关实现
    all_drafted = Article().get_all_article_drafted(user_id)

    return render_template("new-article.html",
                           label_types=label_types,
                           article_types=article_types,
                           article_tags=article_tags,
                           all_drafted=all_drafted,
                           drafted_count=len(all_drafted))

# 获取某一篇草稿的详情
@article.route("/article/drafted",methods=["post"])
def get_drafted_detail():
    request_data = json.loads(request.data)
    result = Article().get_one_artcile_drafted(request_data.get('id'))
#    把结果转成json，然后给前端返回
    article_drafted = model_to_json(result)
    return response_message.ArticleMessage.success(article_drafted)


def get_article_request_param(request_data):
    user = User().find_by_userid(session.get("user_id"))
    title = request_data.get("title")
    article_content = request_data.get("article_content")
    return user,title,article_content

# 草稿或文章存储
@article.route("/article/save",methods=["post"])
def article_save():
    request_data = json.loads(request.data)
    # 我们根据article_id来判断是不是第一次保存，如果没有这个id就存储为草稿，如果有那么就文章发布
    # 其实文章发布就是文章更新
    article_id = request_data.get("article_id")
    # 取出是否是草稿
    drafted = request_data.get("drafted")
    # 必须让前端传一个article_id，那么这个值如果是-1我们就认为是草稿
    if article_id == -1 and drafted==0:
        user,title,article_content = get_article_request_param(request_data)
        if title == "":
            return response_message.ArticleMessage.other("请输入文章头信息")
        # 存储草稿的时候一定要返回一个article_id回来
        article_id = Article().insert_article(user.user_id,title,article_content,drafted)
        return response_message.ArticleMessage.save_success(article_id,"草稿存储成功")
    elif article_id > -1:
        user, title, article_content = get_article_request_param(request_data)
        if title == "":
            return response_message.ArticleMessage.other("请输入文章头信息")
        # 图片信息就不在这里获取了，当用户点击上传头像的时候，这个头像信息就应该已经更新到数据库里了
        # 所以图片上传这个动作应该发生在文章发布的前边
        label_name = request_data.get("label_name")
        article_tag = request_data.get("article_tag")
        article_type = request_data.get("article_type")

        article_id = Article().update_article(
            article_id=article_id,
            title=title,
            article_content=article_content,
            drafted=drafted,
            label_name=label_name,
            article_tag=article_tag,
            article_type=article_type
        )
        return response_message.ArticleMessage.save_success(article_id,"发布文章成功")
# 上传文章头部图片
@article.route("/article/upload/article_header_image",methods=["post"])
def upload_article_header_image():
    # 获取前端图片文件
    f = request.files.get("header-image-file")
    filename = f.filename

    # 文件的后缀名
    suffix = filename.split(".")[-1]
    newname = time.strftime("%Y%m%d_%H%M%S." + suffix)
    newname = "article-header-" + newname
    f.save("resource/upload/" + newname)
    # 大图片压缩
    source = dest = "resource/upload/" + newname
    compress_image(source, dest, 1200)

    # 更新数据库
    article_id = request.form.get("article_id")
    Article().update_article_header_image(article_id,newname)
    # 构造响应数据
    result = {}
    result["state"] = "SUCCESS"
    result['url'] = "/upload/" + newname
    result["title"] = filename
    result["original"] = filename
    return jsonify(result)

@article.route("/article/random/header/image",methods=["post"])
def random_article_header_image():
    name = random.randint(1,539)
    newname = str(name) + ".jpg"
    # 更新数据库
    article_id = request.form.get("article_id")
    Article().update_article_header_image(article_id,newname)
    # 构造响应数据
    result = {}
    result["state"] = "SUCCESS"
    result['url'] = "/images/headers/" + newname
    result["title"] = newname
    result["original"] = newname
    return jsonify(result)
```

### favorite.py

```
import json

from flask import Blueprint, render_template, request, session
import logging

from app.config.config import config
from app.settings import env
from common import response_message
from model.article import Article
from model.favorite import Favorite
from model.user import User

favorite = Blueprint("favorite",__name__)

@favorite.route("/favorite/update_status",methods=["post"])
def update_status():
    request_data = json.loads(request.data)
    user_id = session.get("user_id")
    article_id = request_data.get("article_id")  # []
    canceled = request_data.get("canceled")
    try:
        Favorite().update_status(article_id=article_id,
                                 user_id=user_id,
                                 canceled=canceled)
        return response_message.FavoriteMessage.success("收藏成功")
    except Exception as e:
        logging.error(e)
        print(e)
        return response_message.FavoriteMessage.error("收藏失败")

```

### feedback.py

```
import json
import time

from flask import Blueprint, render_template, request, session, make_response, jsonify
import logging

from app.config.config import config
from app.settings import env
from common import response_message
from common.utils import compress_image, model_to_json
from model.article import Article
from model.favorite import Favorite
from model.feedback import Feedback
from model.user import User

from app.config.ue_config import FEEDBACK_UECONFIG


feedback = Blueprint("feedback",__name__)


@feedback.before_request
def before_comment():
    if session.get("is_login") is None or session.get("is_login") !='true':
        return {"status":9999,"data":"您好，请登录"}

@feedback.route("/feedback",methods=["get","post"])
def ueditor():
    param = request.args.get("action")
    print(param)
    if request.method=="GET" and param == "config":
        return make_response(FEEDBACK_UECONFIG)
    # 下边是我们做图片上传的代码
    # elif param == "uploadimage":
    elif param == "image":
        f = request.files.get("file")
        filename = f.filename
        # 文件的后缀名
        suffix = filename.split(".")[-1]
        newname = time.strftime("%Y%m%d_%H%M%S."+suffix)
        f.save("resource/upload/"+newname)
        # 大图片压缩
        source = dest = "resource/upload" + newname
        compress_image(source,dest,1200)

        # 构造响应数据
        result = {}
        result["state"] = "SUCCESS"
        result['url']="/upload/"+newname
        result["title"]=filename
        result["original"]=filename
        return jsonify(result)

# 添加一个评论
@feedback.route("/feedback/add",methods=['post'])
def add():
    request_data = json.loads(request.data)
    article_id = request_data.get("article_id")
    content = request_data.get("content").strip()
    ipaddr = request.remote_addr
    user_id = session.get("user_id")

    # 对内容进行校验
    if len(content)<5 or len(content)>1000 :
        return response_message.FeedbackMessage.other("内容长度不符")

    feedback = Feedback()
    try:
        result = feedback.insert_comment(user_id=user_id,
                                         article_id=article_id,
                                         content=content,
                                         ipaddr=ipaddr)
        result = model_to_json(result)
        return response_message.FeedbackMessage.success("评论成功")
    except Exception as e:
        print(e)
        return response_message.FeedbackMessage.error("评论失败")

@feedback.route("/feedback/reply",methods=["post"])
def reply():
    request_data = json.loads(request.data)
    article_id = request_data.get("article_id")
    content = request_data.get("content").strip()
    ipaddr = request.remote_addr
    user_id = session.get("user_id")
    reply_id = request_data.get("reply_id")
    base_reply_id = request_data.get("base_reply_id")

    # 对内容进行校验
    if len(content) < 5 or len(content) > 1000:
        return response_message.FeedbackMessage.other("内容长度不符")

    feedback = Feedback()
    try:
        result = feedback.insert_reply(user_id=user_id,
                            article_id=article_id,
                            content=content,
                            ipaddr=ipaddr,
                            reply_id=reply_id,
                            base_reply_id=base_reply_id)
        return response_message.FeedbackMessage.success("评论成功")
    except Exception as e:
        print(e)
        return response_message.FeedbackMessage.error("评论失败")


```

### index.py

```
from flask import Blueprint, render_template, request
import logging

from app.config.config import config
from app.settings import env
from model.article import Article

index = Blueprint("index",__name__)



# 对应前端显示分类的字典
label_types = {
    "recommend":{"name":"推荐","selected":"selected"},
    "auto_test":{"name":"自动化测试","selected":"no-selected"},
    "python":{"name":"Python","selected":"no-selected"},
    "java":{"name":"Java","selected":"no-selected"},
    "function_test":{"name":"功能测试","selected":"no-selected"},
    "perf_test":{"name":"性能测试","selected":"no-selected"},
    "funny":{"name":"幽默段子","selected":"no-selected"},
}

@index.route("/")
def home():
    # 获取当前到底是第几页
    page = request.args.get("page")
    article_type = request.args.get("article_type")
    logging.debug("page:"+str(page))
    logging.debug("article_type:"+str(article_type))
    if page is None:
        page = 1
    if article_type is None:
        article_type = "recommend"
    #     到数据库中查询文章数据，然后返回给前端页面
    article = Article()
    # 文章搜索功能实现
    search_keyword = request.args.get("keyword")
    if search_keyword is not None:
        db_result = article.search_article(page,search_keyword)
    else:
        db_result = article.find_article(page,article_type)

    for article,nickname in db_result:
    #     分类内容显示的转换
        article.label = label_types.get(article.label_name).get("name")

    # 日期的显示
        article.create_time = str(article.create_time.month) + '.' + str(article.create_time.day)

    # 图片路径的处理  "/images/article/header/"
        article.article_image = config[env].article_header_image_path + str(article.article_image)

    # 文章标签格式的修改
        article.article_tag = article.article_tag.replace(","," · ")

    start_num = request.args.get("start_num")
    if start_num is None:
        start_num=0
    end_num = len(db_result)

    # 左侧菜单栏文章分类的逻辑
    for k,v in label_types.items():
        if article_type == k:
            v["selected"] = "selected"
        else:
            v["selected"] = "np-selected"

    return render_template("index.html",
                           result=db_result,
                           start_num=start_num,
                           end_num=end_num,
                           label_types=label_types)


```

### personal.py

```
import json
import random
import time

from flask import Blueprint, render_template, request, session, jsonify, make_response, url_for
import logging

from app.config.config import config
from app.settings import env
from common import response_message
from common.utils import compress_image, model_to_json
from model.article import Article
from model.favorite import Favorite
from model.feedback import Feedback
from model.user import User

personal = Blueprint("personal",__name__)
@personal.before_request
def personal_before_request():
    url = request.path
    is_login = session.get("is_login")
    if url.startswith("/personal") and is_login != 'true':
        response = make_response("登录重定向",302)
        response.headers["Location"] = url_for("index.home")
        return response

@personal.route("/personal")
def personal_center():
    # url  ?type=我的评论、 我的收藏
    type_name = request.args.get("type")
    if type_name is None:
        type_name = "article"
    user_id = session.get("user_id")
    # user_id = 1
#     如果是文章
    article = Article()
    if type_name == "article":
        article_data = article.get_article_by_userid(user_id)
#     如果是收藏
    elif type_name == "favorite":
        article_data = article.get_favirite_article_by_userid(user_id)

    # 如果是评论
    elif type_name == "feedback":
        article_data = article.get_feedback_article_by_userid(user_id)

    else:
        return response_message.PersonalMessage.error("参数传递错误")
    user = User().find_by_userid(user_id)
    return render_template("personal_center.html",
                           article_data=article_data,
                           type_name=type_name,
                           active=type_name,
                           user=user)

```

### redis_user.py

```
import hashlib
import json
import re

from flask import Blueprint, make_response, session, request, url_for

from common import response_message
from common.email_utils import gen_email_code, send_email
from common.utils import ImageCode
from model.user import User
from app.config.config import config
from app.settings import env
from common.redisdb import redis_connect
redis_user = Blueprint("redis_user",__name__)

redis_client = redis_connect()
@redis_user.route("/redis/ecode",methods=["post"])
def email_code():
    # email = request.form.get("email")
    email = json.loads(request.data).get("email")
    # 简单的邮箱格式验证
    if not re.match(".+@.+\..+",email):
        return response_message.UserMessage.other("无效的邮箱")
    # 生成邮箱验证码的随机字符串
    code = gen_email_code()
    # 发送邮件
    try:
        send_email(email,code)
        # session['ecode'] = code.lower()
        # redis_client.set(email,code.lower())
        # 我们的名字加一个冒号，RDM会帮助我们把所有冒号前边的内容形成一个文件夹，这样更方便我们的查看
        email_vcode = "email:"+email
        redis_client.set(email_vcode,code.lower())
        # 单独设置过期时间
        redis_client.expire(email_vcode,60)
        return response_message.UserMessage.success("邮件发送成功")
    except Exception as e:
        print(e)
        return response_message.UserMessage.error("邮件发送失败")


@redis_user.route("/redis/reg",methods=["post"])
def register():
    request_data = json.loads(request.data)
    username=request_data.get("username")
    password=request_data.get("password")
    second_password=request_data.get("second_password")
    ecode=request_data.get("ecode")
    redis_ecode = redis_client.get("email:"+username)
    # 做数据的验证
    if ecode.lower() != redis_ecode:
        return response_message.UserMessage.error("邮箱验证码错误")
    # 用户名 和 密码的验证
    if not re.match(".+@.+\..+", username):
        return response_message.UserMessage.other("无效的邮箱")

    if len(password) < 6:
        return response_message.UserMessage.error("密码不合法")

    if password != second_password:
        return response_message.UserMessage.error("两次密码不一致")
    # 用户名是否已经注册
    user = User()
    if len(user.find_by_username(username=username)) > 0:
        return response_message.UserMessage.error("用户名已经存在")

    # 实现注册的功能了
    password = hashlib.md5(password.encode()).hexdigest()
    result = user.do_register(username=username,password=password)
    return response_message.UserMessage.success("用户注册成功")


@redis_user.route("/redis/login",methods=["post"])
def login():
    request_data = json.loads(request.data)
    username = request_data.get("username")
    password = request_data.get("password")
    # vcode = request_data.get("vcode")
    #
    # if vcode != session.get("vcode"):
    #     return response_message.UserMessage.error("验证码输入错误")

    #实现登录功能
    password = hashlib.md5(password.encode()).hexdigest()
    # 首先我们需要到redis中查看用户的数据，如果查询不到再到mysql中进行查询
    result = redis_client.get("user:"+username)


    if result is None:
        user = User()
        result = user.find_by_username(username)
        if len(result) == 1 and result[0].password==password:
            # 需要进行登录状态的管理
            session["is_login"]="true"
            session["user_id"] = result[0].user_id
            session["username"] = username
            session["nickname"] = result[0].nickname
            session["picture"] = config[env].user_header_image_path+result[0].picture

            response=make_response(response_message.UserMessage.success("登录成功"))
            response.set_cookie("username",username,max_age=30*24*3600)
            # response.set_cookie("username",username,max_age=30*24*3600)
            return response
        else:
            return response_message.UserMessage.error("用户名或者是密码错误")
    else:
        # 把字符串变成一个字典
        result = eval(result)
        if result.get("password")==password:
            response = make_response(response_message.UserMessage.success("登录成功"))
            return response
        else:
            return response_message.UserMessage.error("用户名或者是密码错误")


@redis_user.route("/redis/login2",methods=["post"])
def login2():
    request_data = json.loads(request.data)
    username = request_data.get("username")
    password = request_data.get("password")
    # vcode = request_data.get("vcode")
    #
    # if vcode != session.get("vcode"):
    #     return response_message.UserMessage.error("验证码输入错误")

    #实现登录功能
    password = hashlib.md5(password.encode()).hexdigest()
    # 首先我们需要到redis中查看用户的数据，如果查询不到再到mysql中进行查询
    redis_password = redis_client.hget("hash_user:"+username,username)
    if redis_password == password:
        response = make_response(response_message.UserMessage.success("登录成功"))
        return response
    else:
        return response_message.UserMessage.error("用户名或者是密码错误")
```

### user.py

```
import hashlib
import json
import re

from flask import Blueprint, make_response, session, request, url_for

from common import response_message
from common.email_utils import gen_email_code, send_email
from common.utils import ImageCode
from model.user import User
from app.config.config import config
from app.settings import env

user = Blueprint("user",__name__)

# @user.route("/aaa")
# def get_one():
#     user = User()
#     result = user.get_one()
#     print(result)
#     print(result.username)
#     return "ok"

@user.route("/vcode")
def vcode():
    code,bstring = ImageCode().get_code()
    response = make_response(bstring)
    response.headers["Content-Type"]="image/jpeg"
    # 存储起来，我们暂时存储到内存中，也就是session里边
    session['vcode'] = code.lower()
    print(code.lower())
    return response

@user.route("/ecode",methods=["post"])
def email_code():
    # email = request.form.get("email")
    email = json.loads(request.data).get("email")
    # 简单的邮箱格式验证
    if not re.match(".+@.+\..+",email):
        return response_message.UserMessage.other("无效的邮箱")
    # 生成邮箱验证码的随机字符串
    code = gen_email_code()
    # 发送邮件
    try:
        send_email(email,code)
        session['ecode'] = code.lower()
        return response_message.UserMessage.success("邮件发送成功")
    except Exception as e:
        print(e)
        return response_message.UserMessage.error("邮件发送失败")

@user.route("/reg",methods=["post"])
def register():
    request_data = json.loads(request.data)
    username=request_data.get("username")
    password=request_data.get("password")
    second_password=request_data.get("second_password")
    ecode=request_data.get("ecode")
    # 做数据的验证
    if ecode.lower() != session.get("ecode"):
        return response_message.UserMessage.error("邮箱验证码错误")
    # 用户名 和 密码的验证
    if not re.match(".+@.+\..+", username):
        return response_message.UserMessage.other("无效的邮箱")

    if len(password) < 6:
        return response_message.UserMessage.error("密码不合法")

    if password != second_password:
        return response_message.UserMessage.error("两次密码不一致")
    # 用户名是否已经注册
    user = User()
    if len(user.find_by_username(username=username)) > 0:
        return response_message.UserMessage.error("用户名已经存在")

    # 实现注册的功能了
    password = hashlib.md5(password.encode()).hexdigest()
    result = user.do_register(username=username,password=password)
    return response_message.UserMessage.success("用户注册成功")

@user.route("/login",methods=["post"])
def login():
    request_data = json.loads(request.data)
    username = request_data.get("username")
    password = request_data.get("password")
    vcode = request_data.get("vcode")

    if vcode != session.get("vcode"):
        return response_message.UserMessage.error("验证码输入错误")

    #实现登录功能
    password = hashlib.md5(password.encode()).hexdigest()
    user = User()
    result = user.find_by_username(username)
    if len(result) == 1 and result[0].password==password:
        # 需要进行登录状态的管理
        session["is_login"]="true"
        session["user_id"] = result[0].user_id
        session["username"] = username
        session["nickname"] = result[0].nickname
        session["picture"] = config[env].user_header_image_path+result[0].picture

        response=make_response(response_message.UserMessage.success("登录成功"))
        response.set_cookie("username",username,max_age=30*24*3600)
        # response.set_cookie("username",username,max_age=30*24*3600)
        return response
    else:
        return response_message.UserMessage.error("用户名或者是密码错误")

# 注销功能的实现
@user.route("/logout")
def logout():
    # 清空session
    session.clear()
    response = make_response("注销并进行重定向", 302)
    # 这里的url_for写的不是一个url地址,而是我们的控制器的模块名称.函数名称，然后映射到这个控制器处理函数的地址上
    response.headers["Location"] = url_for("index.home")
    # 清除掉cookie
    response.delete_cookie("username")
    return response
```



## log

mumunote.og 日志文件

## model

```
model
├─ __init__.py
├─ article.py
├─ favorite.py
├─ feedback.py
└─ user.py
```

### article.py

```
from sqlalchemy import Table, or_, distinct

from common.database import db_connect
from app.config.config import config
from app.settings import env
from model.favorite import Favorite
from model.feedback import Feedback
from model.user import User

db_session,Base,engine = db_connect()
class Article(Base):
    __table__ = Table("article", Base.metadata, autoload_with=engine)
#     查询出所有文章，但是不要草稿
    def find_article(self,page,article_type="recommend"):
        #     一页显示多少内容呢,我们默认为一个10,page默认应该是从1开始
        if int(page) < 1:
            page = 1
        count = int(page) * config[env].page_count
        # 这就证明是来到了推荐的分类下边
        if article_type == "recommend":
            result = db_session.query(Article,User.nickname).join(
                User,User.user_id==Article.user_id
            ).filter(
                Article.drafted==1
            ).order_by(
                Article.browse_num.desc()
            ).limit(count).all()
        else:
            result = db_session.query(Article,User.nickname).join(
                User, User.user_id == Article.user_id
            ).filter(
                Article.label_name == article_type,
                Article.drafted==1
            ).order_by(
                Article.browse_num.desc()
            ).limit(count).all()
        return result

    def search_article(self,page,keyword):
        if int(page) < 1:
            page = 1
        count = int(page) * config[env].page_count
        result = db_session.query(
            Article,User.nickname).join(
            User,User.user_id==Article.user_id).filter(
            or_(Article.title.like("%"+keyword+"%"),
                Article.article_content.like("%"+keyword+"%"))
        ).order_by(
            Article.browse_num.desc()
        ).limit(count).all()
        return result

    # 获取文章详情
    def get_article_detail(self,article_id):
        result = db_session.query(Article).filter_by(id=article_id).first()
        result.browse_num += 1
        db_session.commit()
        return db_session.query(Article).filter_by(id=article_id).first()
        # return db_session.query(Article).filter(Article.id==article_id)

    # 获取相关文章的数据
    def find_about_article(self,label_name):
        return db_session.query(Article).filter_by(
            label_name=label_name).order_by(
            Article.browse_num.desc()
        ).limit(5)

    # 创建文章以及草稿
    def insert_article(self,user_id,title,article_content,drafted):
        article = Article(
            user_id=user_id,
            title=title,
            article_content=article_content,
            drafted=drafted
        )
        db_session.add(article)
        db_session.commit()
        return article.id

    # 更新文章相关信息，其实就是文章发布的逻辑
    def update_article(self,
                       article_id,
                       title,
                       article_content,
                       drafted,
                       label_name="",
                       article_tag="",
                       article_type=""
                       ):
        row = db_session.query(Article).filter_by(id=article_id).first()
        row.title=title
        row.article_content = article_content,
        row.drafted = drafted,
        row.label_name = label_name,
        row.article_tag = article_tag,
        row.article_type = article_type
        db_session.commit()
        return article_id
    def update_article_header_image(self,article_id,article_image):
        row = db_session.query(Article).filter_by(id=article_id).first()
        row.article_image = article_image
        db_session.commit()
        return article_id

    # 获取所有我的草稿
    def get_all_article_drafted(self,user_id):
        result = db_session.query(Article).filter_by(user_id=user_id,
                                                     drafted=0
                                                     ).all()
        return result
    # 获取某一篇草稿的详情
    def get_one_artcile_drafted(self,article_id):
        result = db_session.query(Article).filter_by(
            id=article_id,
            drafted=0
        ).first()
        return result

    # 获取某一个用户所有的不是草稿的文章
    def get_article_by_userid(self,user_id):
        result = db_session.query(Article).filter_by(
            user_id=user_id,
            drafted=1
        ).all()
        return self.app_path(result)

    # 获取某个用户所有的收藏的文章
    def get_favirite_article_by_userid(self,user_id):
        result = db_session.query(Article).join(
            Favorite,
            Favorite.article_id == Article.id
        ).filter(
            Favorite.user_id == user_id
        ).order_by(
            Favorite.create_time.desc()
        ).all()
        return self.app_path(result)

    # 获取所有用户评论过的文章
    def get_feedback_article_by_userid(self,user_id):
        # 用子查询解决查询结果的问题
        article_id_list = db_session.query(
            distinct(Feedback.article_id)
        ).filter_by(user_id=user_id).subquery()
        # 再通过文章id的集合查询到所有文章数据
        result = db_session.query(Article).filter(
            Article.id.in_(article_id_list)
        ).all()
        return self.app_path(result)


    # 添加文章中所有头部图片的路径
    def app_path(self,article_list):
        for article in article_list:
            article.article_image = config[env].article_header_image_path + article.article_image
        return article_list
```



### favorite.py

```
from sqlalchemy import Table, or_

from common.database import db_connect
from app.config.config import config
from app.settings import env
from model.user import User

db_session,Base,engine = db_connect()
class Favorite(Base):
    __table__ = Table("favorite", Base.metadata, autoload_with=engine)

    def update_status(self,article_id,user_id,canceled=0):
        # canceled的值为0的意思就是收藏，为1的意思就是取消收藏
        # 查询一下这个用户是否收藏过，如果没有收藏，那么就插入数据，如果收藏过，那么就更新数据
        favorite_data = db_session.query(Favorite).filter_by(
            article_id=article_id,
            user_id=user_id
        ).first()
        if favorite_data is None:
            favorite = Favorite(
                article_id=article_id,
                user_id=user_id,
                canceled=canceled
            )
            db_session.add(favorite)
        else:
            favorite_data.canceled=canceled
        db_session.commit()

# 查询某个用户是否收藏
    def user_if_favorite(self,user_id,article_id):
        result = db_session.query(Favorite.canceled).filter_by(
            user_id=user_id,
            article_id=article_id
        ).first()
        if result is None:
            return 1
        else:
            return result[0]
```



### feedback.py

```
from sqlalchemy import Table, or_, func

from common.database import db_connect
from app.config.config import config
from app.settings import env
from common.utils import model_to_json
from model.user import User

db_session,Base,engine = db_connect()
class Feedback(Base):
    __table__ = Table("comment", Base.metadata, autoload_with=engine)


    """
    我们需要最终给前端返回一个完整的数据
    那么最终的数据样式
    final_data_list=[{
    最上层评论的数据以及用户数据，
    replay_list:[{
        from_user:"",
        to_user:"",
        reply:""
    },{},{}]
    },{},{}]
    
    """
    def get_feedback_user_list(self,article_id):
        final_data_list = []
        # 查询文章的一级评论 ，就是那些带有楼层的，新开的评论
        feedback_list = self.find_feedback_by_article_id(article_id)
        for feedback in feedback_list:
            user = User()
            # 根据一级评论的数据，获取回复评论的评论的内容
            all_reply = self.find_reply_by_replyid(base_reply_id=feedback.id)
            feedback_user = user.find_by_userid(feedback.user_id)
            reply_list = []
            # 再根据每一条回复的评论，查询用户信息
            for reply in all_reply:
                # 用于存储当前这条原始评论的所有回复评论，如果没有回复，这个值就为空
                reply_content_with_user = {}
                from_user_data = user.find_by_userid(reply.user_id)
                # 获取回复谁的评论的用户信息
                to_user_reply_data = self.find_reply_by_id(reply.reply_id)
                to_user_data = user.find_by_userid(to_user_reply_data[0].user_id)

                reply_content_with_user["from_user"] = model_to_json(from_user_data)
                reply_content_with_user["to_user"] = model_to_json(to_user_data)
                reply_content_with_user["content"] = model_to_json(reply)
                reply_list.append(reply_content_with_user)

            # 存储每一个回复下的所有数据
            every_feedback_data = model_to_json(feedback)
            every_feedback_data.update(model_to_json(feedback_user))
            every_feedback_data["reply_list"] = reply_list
            final_data_list.append(every_feedback_data)
        return final_data_list




    def find_feedback_by_article_id(self,article_id):
        result = db_session.query(Feedback).filter_by(
            article_id=article_id,
            reply_id=0,
            base_reply_id=0
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def find_reply_by_replyid(self,base_reply_id):
        result = db_session.query(Feedback).filter_by(
            base_reply_id=base_reply_id
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def find_reply_by_id(self,id):
        result = db_session.query(Feedback).filter(
            Feedback.id == id
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def get_article_feedback_count(self,article_id):
        result = db_session.query(Feedback).filter_by(
            article_id=article_id,
            reply_id=0,
            base_reply_id=0
        ).count()
        return result


    # 插入一级评论
    def insert_comment(self,user_id,article_id,content,ipaddr):
        # label的意思就是重新起一个名字给字段
        feedback_max_floor = db_session.query(
            func.max(Feedback.floor_number).label("max_floor")
        ).filter_by(article_id=article_id).first()
        if feedback_max_floor.max_floor == 0 or feedback_max_floor.max_floor is None:
            feedback = Feedback(user_id=user_id,
                                article_id=article_id,
                                content=content,
                                ipaddr=ipaddr,
                                floor_number=1,
                                reply_id=0,
                                base_reply_id=0)
        else:
            feedback = Feedback(user_id=user_id,
                                article_id=article_id,
                                content=content,
                                ipaddr=ipaddr,
                                floor_number=int(feedback_max_floor.max_floor)+1,
                                reply_id=0,
                                base_reply_id=0)
        db_session.add(feedback)
        db_session.commit()
        # 做一个手动刷新就可以拿到插入的数据的值了
        # db_session.refresh()
        return feedback

    def insert_reply(self,article_id,user_id,content,ipaddr,reply_id,base_reply_id):
        feedback = Feedback(user_id=user_id,
                            article_id=article_id,
                            content=content,
                            ipaddr=ipaddr,
                            reply_id=reply_id,
                            base_reply_id=base_reply_id)
        db_session.add(feedback)
        db_session.commit()
```



### user.py

```
import random

from sqlalchemy import Table

from common.database import db_connect

from app.config.config import config
from app.settings import env

db_session,Base,engine = db_connect()

class User(Base):
    # 表结构的反射加载
    __table__ = Table("user",Base.metadata,autoload_with=engine)

    def get_one(self):
        return db_session.query(User).first()

    def find_by_username(self,username):
        return db_session.query(User).filter_by(username=username).all()

    def do_register(self,username,password):
        nickname = username.split("@")[0]
        # 头像
        picture_num = random.randint(1,539)
        picture = str(picture_num) + ".jpg"
        job="未定义"
        user = User(username=username,
                    password=password,
                    nickname=nickname,
                    picture=picture,
                    job=job)
        db_session.add(user)
        db_session.commit()
        return user

    def find_by_userid(self,user_id):
        user_info = db_session.query(User).filter_by(user_id=user_id).first()
        # 这个代码是为了方便调用者自己不用拼接用户头像的路径了

        if user_info.picture.startswith(config[env].user_header_image_path):
            return user_info
        else:
            user_info.picture = config[env].user_header_image_path + user_info.picture
            return user_info

```



## template

```
template
├─ article-info.html
├─ index.html
├─ new-article.html
├─ personal_center.html
└─ public
       ├─ header.html
       └─ sub-header.html
```

### article-info.html

```
{% extends 'public/header.html' %}
{% block content %}
<!--      按需引入-->
        {% include 'public/sub-header.html' %}
		
		<link rel="stylesheet" href="css/article-info.css">
	
		<script type="text/javascript" src="/plugins/ueditor-plus/ueditor.config.js"></script>
		<script type="text/javascript" src="/plugins/ueditor-plus/ueditor.all.js"></script>
		<script type="text/javascript" src="/plugins/ueditor-plus/lang/zh-cn/zh-cn.js"></script>
		<script type="text/javascript" src="/js/article-info.js"></script>
		<script type="text/javascript" src="/js/axios.min.js"></script>
  <div class="article-main">
	  <div class="article-container">
		  <div class="article-path">
			  <!-- <span>首页 > 手记 > 为什么面试聊得很好，转头却挂了？</span> -->
			  <span>首页 > 手记 > {{article_content.title}}</span>
			   
		  </div>
	  </div>
	  <div class="article-container-main clearfix">
		  <div class="left fl">
			  <div class="article-title">
				  <span>{{article_content.title}}</span>
			  </div>
			  <div class="note-article-info clearfix">
				  <div class="note-left fl">
					  <span class="tag-name">标签:</span>
					  {% for article_tag in article_tag_list %}
					  <!-- <span class="tag-value">{{article_content.article_tag}}</span> -->
					  <span class="tag-value">{{article_tag}}</span>
					  {% endfor %}
					  </div>
					  {% if is_favorite==1 %}
						<div class="note-right fr" onclick="favoriteUpdate({{article_content.id}},0)">收藏</div>
						{% else %}
						<div class="note-right fr" onclick="favoriteUpdate({{article_content.id}},1)">已收藏</div>
						{% endif %}
			  </div>
			  <div class="article-content-warp">
				  {{article_content.article_content | safe}}
			  </div>
			  <div class="article-create-time">发表于 {{article_content.create_time}}， 共 {{article_content.browse_num}} 人浏览</div>
			  <div class="imooc">本文原创发布于慕课网 ，转载请注明出处，谢谢合作</div>
			  <div class="praise">
				  <span class="iconfont">&#xe61b;</span>
			  </div>
			  

		  </div>
		  
		  <div class="right fl">
			  <div class="top clearfix">
				  <div class="author-image fl">
					  <img src="{{user_info.picture}}" alt="">
				  </div>
				  <div class="author-info fl">
					  <div class="author-name">{{user_info.nickname}}</div>
					  <div class="author-job">{{user_info.job}}</div>
				  </div>
			  </div>
			  <div class="bottom">
				  <div class="about-article">相关文章推荐</div>
					<div class="about-article-info">
						{% for article in about_article %}
						<div class="article-info-row">
							<a href="/detail?article_id={{article.id}}" class="iconfont">&#xe895;&nbsp;&nbsp;{{article.title}}</a>
						</div>
						{% endfor %}
					</div>
			  </div>
		  </div>	  
	  </div>
	  	  
		<div class="feedback-num">{{feedback_count}} 评论</div>  
		<div class="article-feedback clearfix">
			<div class="feedback-wrap fl">
				<div class="write-feedback-wrap clearfix">
					<div class="fl">评论</div>
					<span class="fl"  data-bs-toggle="modal" data-bs-target="#feedbackModal">共同学习，写下你的评论</span>
				</div>
				{% if feedback_data_list==[] %}
				<div class="no-data">
					<div class="no-data-line">
						<span>暂无评论</span>
					</div>
				</div>
				{% else %}
				<div class="feedback-list-wrap">
					{% for feedback_data in feedback_data_list %}
					<div class="feedback-detail-wrap">
						<div class="feedback-detail clearfix">
							<div class="feedback fl">
								<div class="feedback-author">
									<a href="">
										<img src="{{feedback_data.picture}}" alt="">
										<span>{{feedback_data.floor_number}}楼</span>
									</a>
								</div>
							</div>
							<div class="feedback-content fl">
								<a href="">{{feedback_data.nickname}}</a>
								<span>{{feedback_data.content |safe}}</span>
								<div class="feedback-content-footer clearfix">
									<span class="iconfont fl">&#xe61b;</span>
									<div class="reply-button fl" onclick="showWriteAuthorInput({{feedback_data.id}},{{feedback_data.article_id}},{{feedback_data.user_id}},'{{feedback_data.nickanme}}',{{feedback_data.id}})">回复</div>
									<div class="publish-time fr">{{feedback_data.create_time}}</div>
								</div>
							</div>
						</div>
					</div>
					<div class="reply-box">
						{% for reply in feedback_data.reply_list %}
						<div class="feedback-reply-detail clearfix">
							<div class="feedback-reply fl">
								<div class="feedback-author">
									<a href="">
										<!-- <img src="/images/headers/6.jpg" alt=""> -->
										<img src="{{reply.from_user.picture}}" alt="">
									</a>
								</div>
							</div>
							<div class="feedback-reply-content fl">
								<a href="#">{{reply.from_user.nickname}}</a>
								<span class="reply-text">回复</span>
								<a href="">{{reply.to_user.nickname}}</a>
								<p>{{reply.content.content|safe}}</p>
								<div class="feedback-reply-content-footer clearfix">
									<div class="reply2-button fl" onclick="showWriteAuthorInput({{feedback_data.id}},{{feedback_data.article_id}},{{reply.from_user.user_id}},'{{reply.from_user.nickanme}}',{{reply.content.id}})">回复</div>
									<div class="publish-time fr">{{reply.content.create_time}}</div>
								</div>
							</div>
						</div>
						
						{% endfor %}
						<div class="write-author-feedback" style="display: none;" id={{feedback_data.id}}>
							<!-- <img src="{{feedback_data.picture}}" alt=""> -->
							<img src="{{session.get('picture')}}" alt="">
							<textarea type="text" placeholder="写下你的回复......"></textarea>
							<div class="author-feedback-button">
								<button class="cancel-author-feedback" onclick="hiddenWriteAuthorInput({{feedback_data.id}})">取消</button>
								<button class="confirm-author-feedback" onclick="writeReply()">回复</button>
							</div>
						</div>
					</div>
					{% endfor %}
				</div>
				{% endif %}
			</div>
			<div class="useless-right fl"></div>
		</div>
		  
  </div>
  
  <div class="feedback-modal-wrap">
	  <div class="modal fade" id="feedbackModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
	    <div class="modal-dialog">
	      <div class="modal-content">
	        <div class="modal-header">
	          <h1 class="modal-title fs-5" id="feedbackModalLabel">发评论</h1>
	          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
	        </div>
	        <div class="modal-body">
	          <!-- 这里将来需要添加一个UEditor plus -->
	  		  <div id="feedback-container"></div>
	        </div>
	        <div class="modal-footer">
	          <button type="button" class="btn btn-primary" onclick="addFeedback({{article_content.id}})">提交</button>
	  	  </div>
	      </div>
	    </div>
	  </div>
  </div>

  
  
{% endblock %}

```



### index.html

```
{% extends 'public/header.html' %}
{% block content %}
<!--      按需引入-->
        {% include 'public/sub-header.html' %}
			<div class="article-container clearfix">
				<div class="left-menu fl">
					{% for label_name,label_value in label_types.items() %}
					<div class="{{label_value.selected}}">
						<a href="?article_type={{label_name}}&page=1">{{label_value.name}}</a>
						</div>
					{% endfor %}
				</div>
				<div class="article-warpper fl">
					<div class="article-inner">
						<!-- 文章数据渲染 -->
						{% for article,nickname in result %}
						<div class="article-row clearfix">
							<div class="article-header-image fl">
								<img src="{{article.article_image}}" alt="">
							</div>
							<div class="article-desc fl">
								<div class="article-name">
									<a href="/detail?article_id={{article.id}}" target="_blank">{{article.title}}</a>
								</div>
								<div class="article-info clearfix">
									<article class="article-left fl">
										<span>{{article.label}}</span>
										<span class="iconfont">{{article.browse_num}}</span>
										<span>{{nickname}}</span>
										<span>{{article.article_tag}}</span>
									</article>
									<div class="article-right fr">{{article.create_time}}</div>
								</div>
							</div>
						</div>
						{% endfor %}
						<div class="load-more">下滑加载更多内容</div>
					</div>
				</div>
			</div>
	</body>
	<script>
		window.startNum = {{start_num}};
		window.endNum = {{end_num}};
		
	</script>
	<script type="text/javascript" src="/js/index.js"></script>
	<script>
		if(location.search.includes("scroll")){
			window.scrollTo(0,document.body.scrollHeight-1000);
		}
	</script>
	
</html>
{% endblock %}
```



### new-article.html

```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>文章发布</title>

		<script type="text/javascript" src="/plugins/ueditor-plus/ueditor.config.js"></script>
		<script type="text/javascript" src="/plugins/ueditor-plus/ueditor.all.js"></script>
		<script type="text/javascript" src="/plugins/ueditor-plus/lang/zh-cn/zh-cn.js"></script>
		<script type="text/javascript" src="/js/new-article.js"></script>
		<link rel="stylesheet" href="/plugins/bootstrap/css/bootstrap.min.css">
		<script type="text/javascript" src="/plugins/bootstrap/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="/js/axios.min.js"></script>
	<link rel="stylesheet" href="/css/base.css">
	<link rel="stylesheet" href="/css/new-article.css">
	</head>
	<body>
		<div class="header">
			<div class="left">
				<span class="iconfont" onclick="showDraftedList()">&#xe895;我的草稿
					<div class="drafted-num">{{drafted_count}}</div>
				</span>
				
				<div class="drafted-info" style="display: none;">
					<div class="iconfont">&#xe601;</div>
					<div class="drafted-list">
						<i>我的草稿</i>
						{% for drafted in all_drafted %}
						<div class="clearfix" onclick="toDrafted({{drafted.id}})">
							<div class="drafted-icon fl">
								<i class="iconfont">&#xe618;</i>
							</div>
							<div class="drafted-create fl">
								<div class="drafted-name">{{drafted.title}}</div>
								<div class="drafted-update-time">{{drafted.create_time}}</div>
							</div>
						</div>
						{% endfor %}
			<!-- 			<div class="clearfix">
							<div class="drafted-icon fl">
								<i class="iconfont">&#xe618;</i>
							</div>
							<div class="drafted-create fl">
								<div class="drafted-name">我的草稿名字</div>
								<div class="drafted-update-time">2365-23-12 12:12:12</div>
							</div>
						</div>
						<div class="clearfix">
							<div class="drafted-icon fl">
								<i class="iconfont">&#xe618;</i>
							</div>
							<div class="drafted-create fl">
								<div class="drafted-name">我的草稿名字</div>
								<div class="drafted-update-time">2365-23-12 12:12:12</div>
							</div>
						</div> -->
					</div>
					
				</div>
				
			</div>
			<div class="mid">
				<span>
					UEditor
				</span>
			</div>
			<div class="right">
				<span class="publish" data-bs-toggle="modal" data-bs-target="#publishArticleModal" onclick="createArticle(0)">发表</span>
			</div>
		</div>
		<div class="main">
			<input class="article-header" placeholder="请在此输入标题"></input>
			<div class="ue">
				<script id="editor" type="text/plain" style="height:300px;">
					这是我的初始化内容
				</script>
			</div>
		</div>
		

<!-- 这个是文章发布的模态框 -->
			<div class="modal fade" id="publishArticleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			  <div class="modal-dialog">
			    <div class="modal-content">
			      <div class="modal-body clearfix">
						<div class="publish-left fl">
							<div class="upload-header-image">
								<label for="xFile">
									<img src="/images/image-upload.png" alt="">
								</label>
							</div>
							<div class="upload-header-button">
								<label for="xFile">本地上传</label>
								<form><input type="file" id="xFile" accept="image/*" style="display: none;"></form>
							</div>
							<div class="random-header" onclick="randomHeaderImage()">随机封面</div>
							<div class="upload-desc">
								请上传200*200px，小于等于80KB的PNG/JPG/GIF图片
							</div>
						</div>
						<div class="publish-right fl">
							<div class="article-cloumns clearfix">
								<div class="article-columns-left fl">
									<div class="article-label-name">投递栏目</div>
									<div class="article-label-value" onclick="showArticleLabelList()">
										<span>请选择需要投递的栏目</span>
										<span class="iconfont">&#xe6b5;</span>
										<div class="article-label-list" style="display: none;">
											<div>
												{% for label_name,label_value in label_types.items() %}
												<li data-label-type="{{label_name}}" class="{{label_value.selected}}" onclick="selectLabelName('{{label_name}}','{{label_value.name}}')">{{label_value.name}}</li>
												{% endfor %}
																<!-- 								<li class="article-label-selected">请选择需要投递的栏目</li>
												<li>Python</li>
												<li>Java</li>
												<li>功能测试</li>
												<li>性能测试</li>
												<li>自动化测试</li>
												<li>幽默段子</li> -->
											</div>

										</div>
									</div>
								</div>
								<div class="article-columns-right fl">
									<div class="article-type-name">文章类型</div>
									<div class="article-type-value" onclick="showArticleTypeList()">
										<span>请选择</span>
										<span class="iconfont">&#xe6b5;</span>
										<div class="article-type-list" style="display: none;">
											<div>
												{% for article_type_name,article_type_value in article_types.items() %}
												<li data-article-type="{{article_type_name}}" class="{{article_type_value.selected}}" onclick="selectArticleType('{{article_type_name}}','{{article_type_value.name}}')">{{article_type_value.name}}</li>
												{% endfor %}
												<!-- <li class="article-type-selected">请选择</li>
												<li>首发</li>
												<li>原创</li>
												<li>其它</li> -->
											</div>
										
										</div>
	
										
									</div>
								</div>
							</div>
							<div class="article-tags">
								<div class="article-tag-name">
									<span>文章标签</span>
									<!-- <span>0/3</span> -->
									<span>
										<span class="tag-num">0</span>
										<span>/</span>
										<span>3</span>
									</span>
								</div>
								<div class="article-tag-value clearfix">
									<div class="change-tags fl">
										<!-- <span>Python</span>
										<span>Js</span> -->
									</div>
									<input class="fl" type="text" placeholder="选择下列标签">
								</div>
								<script>
									window.globalArticleTags= {{article_tags | safe}}
								</script>
								<div class="article-tag-list">
									{% for article_tag in article_tags %}
										<span onclick="addTag('{{article_tag}}')">{{article_tag}}</span>
									{% endfor %}
									<!-- <span>Html5</span>
									<span>Angular</span>
									<span>JS</span>
									<span>CSS3</span>
									<span>Sass/Less</span>
									<span>JAVA</span>
									<span>Python</span>
									<span>Go</span>
									<span>C++</span>
									<span>C#</span> -->
								</div>
							</div>
							<button class="saveAndCancelButton" onclick="createArticle(0)">保存并取消</button>
							<button class="publishButton" onclick="createArticle(1)">确定发布</button>
						</div>
			      </div>
			  </div>
			</div>
			

	</body>
</html>
```



### personal_center.html

```
{% extends 'public/header.html' %}
{% block content %}
<link rel="stylesheet" href="/css/personal_center.css">
	<div class="person-center-header">
		<div class="user-info clearfix">
			<div class="user-picture fl">
				<img src="{{user.picture}}" alt="">
			</div>
			<div class="personal-name fl">{{user.nickname}}</div>
		</div>
	</div>
	<div class="personal-main">
		<div class="personal-content clearfix">
			<div class="menu fl">
			<!-- 	 <div class="every-menu">
				</div> 
				 -->
				 <!-- 判断具体哪个菜单是活动的菜单 -->
				 {% if active == 'article' %}
				 <div class="active">
				 {% else %}
				 <div class="every-menu">
				 {% endif %}
					 <a href="/personal?type=article">
						 <span class="iconfont">&#xe6c7;</span>
						 <span>我的文章</span>
					 </a>
				 </div>
				 
				 {% if active == 'favorite' %}
				 <div class="active">
				 {% else %}
				 <div class="every-menu">
				 {% endif %}
				 					 <a href="/personal?type=favorite">
				 						 <span class="iconfont">&#xeca7;</span>
				 						 <span>我的收藏</span>
				 					 </a>
				 </div>
				 
				 
				 {% if active == 'feedback' %}
				 <div class="active">
				 {% else %}
				 <div class="every-menu">
				 {% endif %}
				 					 <a href="/personal?type=feedback">
				 						 <span class="iconfont">&#xe607;</span>
				 						 <span>我的评论</span>
				 					 </a>
				 </div>
				
			</div>
			<!-- <div class="content fl">我是右侧的文章内容</div> -->
			<div class="content fl">
				<!-- 无内容时展现的内容 -->
				{% if article_data==[] %}
					<div class="item-list">
						{% if type_name == 'article' %}
						<p class="no-item">
							你还没有任何文章，快去
							<a href="/article/new">发表文章</a>
						</p>
						{% elif type_name == 'favorite' %}
						<p class="no-item">
							你还没有任何文章收藏，快去
							<a href="/">看看文章</a>吧
						</p>
						{% elif type_name == 'feedback' %}
						<p class="no-item">
							你还没有任何文章评论，快去
							<a href="/">看看文章</a>吧
						</p>
						{% endif %}
					</div>
				{% else %}
				<!-- 有内容时 -->
				<div class="item-list">
					{% for article in article_data %}
						<div class="every-item">
							<div class="item-title">
								<a href="/detail?article_id={{article.id}}" target="_blank">
									{{article.title}}
								</a>
								<span>{{article.article_type}}</span>
							</div>
							<div class="item-content clearfix">
								<div class="item-image fl">
									<a href="/detail?article_id={{article.id}}" target="_blank">
										<img src="{{article.article_image}}" alt="">
									</a>
								</div>
								<div class="item-text fl">
									{{article.article_content | striptags | truncate(255)}}
								</div>
							</div>
							<div class="item-info">
								<span>{{article.browse_num}}浏览</span>
								<span>0评论</span>
							</div>
						</div>
					{% endfor %}
				</div>
				{% endif %}
				
				
			</div>
		
		</div>
	</div>
  
	</body>
</html>
{% endblock %}
```

### public/header.html

```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>慕慕手记首页</title>
		<!-- 初始化样式 -->
		<link rel="stylesheet" href="../../plugins/bootstrap/css/bootstrap.min.css">
		<link rel="stylesheet" href="css/base.css">
		<link rel="stylesheet" href="css/index.css">
		<link rel="stylesheet" href="css/login.css">
		<script type="text/javascript" src="../../plugins/bootstrap/js/bootstrap.min.js"></script>
		<!-- <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> -->
			<script type="text/javascript" src="/js/axios.min.js"></script>
		<script type="text/javascript" src="/js/header.js"></script>

	</head>
	<body>
		<div class="header">
			<div class="header-container clearfix">
				<div class="header-left fl">
					<span><a href="">慕课网首页</a></span>
					<span><a href="">免费课</a></span>
					<span><a href="">实战课</a></span>
					<span>
						<a href="">体系课</a>
						<img src="images/new.png" alt="">
					</span>
					<span><a href="">慕课教程</a></span>
					<span><a href="">专栏</a></span>
					<span><a href="">手记</a></span>
					<span>
						<a href="">企业服务</a>
						<img src="images/new.png" alt="">
					</span>
				</div>
				<div class="header-right fr">
					<span>
						<i class="iconfont">&#xe60d;</i>
					</span>
					<span>
						<i class="iconfont">&#xe73c;</i>
					</span>
					
					<span class="login">
						{% if session.get('is_login') == 'true' %}
						
						<a href="/personal">欢迎{{session.get('nickname')}}</a>
						<a href="/personal"><img src="{{session.get('picture')}}" alt=""></a>
						<a href="/logout">注销</a>
						{% else %}
						<span data-bs-toggle="modal" data-bs-target="#exampleModal"><a href="#">登录</a></span>
						<span>/</span>
						<span data-bs-toggle="modal" data-bs-target="#regModal"><a href="#">注册</a></span>
						{% endif %}
					</span>

				</div>
			</div>
			</div>
			
			<!-- 这个是登录的模态框 -->
			<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			  <div class="modal-dialog">
			    <div class="modal-content">
			      <div class="modal-header">
			        <h1 class="modal-title fs-5" id="exampleModalLabel">用户登录</h1>
			        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			      </div>
			      <div class="modal-body">
			        <form>
			          <div class="mb-3">
			            <input type="text" class="form-control" id="username" placeholder="请输入您的邮箱">
			          </div>
			          <div class="mb-3">
							<input type="password" class="form-control" id="password" placeholder="请输入您的密码">
			          </div>
					  <div class="mb-3">
						  <img src="/vcode" alt="" onclick="this.src='/vcode?'+Math.random()" class="auto-code-image">
					  	  <input type="text" class="auth-code" id="auth-code" placeholder="请输入验证码">
					  </div>
					  
					  <button type="button" class="btn btn-primary login-button" onclick="doLogin()">登录</button>
			        </form>
			      </div>
			      <div class="modal-footer">
					  <span class="register" data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target="#regModal">注册</span>
					<!--  
			        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
			        <button type="button" class="btn btn-primary">Send message</button>
			      -->
				  </div>
			    </div>
			  </div>
			</div>
			
			<!-- 这是注册的模态框 -->
			
			<div class="modal fade" id="regModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			  <div class="modal-dialog">
			    <div class="modal-content">
			      <div class="modal-header">
			        <h1 class="modal-title fs-5" id="exampleModalLabel">用户注册</h1>
			        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			      </div>
			      <div class="modal-body">
			        <form>
			          <div class="mb-3">
			            <input type="text" class="form-control" id="reg-username" placeholder="请输入您的邮箱">
			          </div>
			          <div class="mb-3">
							<input type="password" class="form-control" id="reg-password" placeholder="请输入您的密码">
			          </div>
					  <div class="mb-3">
							<input type="password" class="form-control" id="reg-password1" placeholder="请再次输入您的密码">
					  </div>
					  <div class="mb-3">
					  	  <input type="text" class="auth-code" id="email-vcode" placeholder="请输入验证码">
						  <button class="send" id="send-email-vcode" onclick="sendEmailVCode()">发送</button>
					  </div>
					  
					  <button type="button" class="btn btn-primary login-button" onclick="userReg()">注册</button>
			        </form>
			      </div>
			      <div class="modal-footer">
					  <span class="register" data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target="#exampleModal">登录</span>
			    <!--    
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
			        <button type="button" class="btn btn-primary">Send message</button>
			      -->
				  </div>
			    </div>
			  </div>
			</div>
				
    {% block content %}
  {% endblock %}
```

### public/sub-header.html

```
		<div class="sub-header clearfix">
			<div class="sub-header-container">
				<div class="sub-header-left fl">
					<img src="images/article-logo.png" alt="">
					<img src="images/article-desc.png" alt="">
				</div>
				<div class="sub-header-right fr clearfix">
						<input type="text" class="fl searchbox" placeholder="搜索感兴趣的知识和文章">
						<span class="iconfont fl" onclick="search_article()">&#xe60d;</span>
						<button class="fl" onclick="toWriteArticlePage('{{session.get('is_login')}}')">写文章</button>
				</div>
			</div>
          </div>
		  <script type="text/javascript" src="/js/sub-header.js"></script>
```



## resource

```
resource
├─ css
│    ├─ article-info.css
│    ├─ base.css
│    ├─ index.css
│    ├─ login.css
│    ├─ new-article.css
│    └─ personal_center.css
├─ font
│    ├─ demo.css
│    ├─ demo_index.html
│    ├─ iconfont.css
│    ├─ iconfont.js
│    ├─ iconfont.json
│    ├─ iconfont.ttf
│    ├─ iconfont.woff
│    └─ iconfont.woff2
├─ images
│    ├─ article
│    │    ├─ .DS_Store
│    │    ├─ content
│    │    └─ header
│    ├─ article-desc.png
│    ├─ article-header.jpg
│    ├─ article-logo.png
│    ├─ article_icon.jpg
│    ├─ article_img.jpeg
│    ├─ author.jpeg
│    ├─ author_profile_pic.jpeg
│    ├─ handbook-desc.png
│    ├─ handbook-logo.png
│    ├─ headers
│    │    └─ 资源图片
│    ├─ image-upload.png
│    ├─ new.png
│    ├─ personal_background.png
│    ├─ second_article.jpeg
│    └─ user_picture.jpeg
├─ js
│    ├─ article-info.js
│    ├─ axios.min.js
│    ├─ header.js
│    ├─ index.js
│    ├─ new-article.js
│    └─ sub-header.js
├─ plugins
│    ├─ bootstrap
│    │    ├─ css
│    │    └─ js
│    └─ ueditor-plus
│           ├─ dialogs
│           ├─ index.html
│           ├─ lang
│           ├─ plugins
│           ├─ themes
│           ├─ third-party
│           ├─ ueditor.all.js
│           ├─ ueditor.config.js
│           └─ ueditor.parse.js
└─ upload
       ├─ article-header-20230501_005619.jpg
       └─ article-header-20230501_005809.jpg
```



### css/article-info.css

```
.article-main {
	background-color: #f8fafc;
}
.article-container {
	width: 1155px;
	margin: 0 auto;
	height: 60px;
	line-height: 60px;
}
.article-path {
	font-size: 14px;
}

.article-container-main {
	width: 1155px;
	margin: 0 auto;
	/* border:1px solid red; */
}
.article-container-main .left{
	
	display: inline-block;
	width: 800px;
	/* border:1px solid red; */
	border-radius: 10px;
	background-color: #fff;
	padding-left: 40px;
	padding-right:40px;
}

.article-container-main .right{
	display: inline-block;
	width: 330px;
	/* border:1px solid red;'' */
	margin-left: 23px;

	
}

.article-title {
	margin-top: 55px;
	font-size: 32px;
	font-weight: 700;
}

/* 标签 */
.note-article-info {
	margin-top: 25px;
}

.note-left {
}
.note-left .tag-name{
	height: 30px;
	line-height: 30px;
	color: #9199a1;
	font-size: 12px;
}
.note-left .tag-value{
	color: #6699ff;
	background-color: #f5f8ff;
	border: 1px solid #e9f0ff;
	font-size: 12px;
	border-radius: 15px;
	padding: 8px 5px;
}
.note-right {
	width: 60px;
	height: 40px;
	line-height: 40px;
	background-color: #3377ff;
	color: #fff;
	text-align: center;
	margin-right: 40px;
	border-radius: 20px;
	font-size: 12px;
}
.note-right:hover {
	cursor: pointer;
}

.article-content-warp {
	margin-top: 55px;
}
/* 修复文章内容图片过大的问题 */
.article-content-warp img{
	width: 100%;
}

.article-container-main .right .top {
	background-color: #fff;
	border-radius: 10px;
}


/* 右侧的头像 */
.author-image img{
	width: 45px;
	height: 45px;
	border-radius: 50%;
	margin: 20px;
}
/* 右侧的作者信息 */
.author-info {
	margin-top: 20px;
	background-color: #fff;
}

.author-info .author-name{
	font-weight: 700;
}

.author-info .author-job{
	margin-top: 15px;
	color: #5c5463;
	font-size: 12px;
}


.article-container-main .right .bottom {
	margin-top: 25px;
	background-color: #fff;
	border-radius: 10px;
}

/* 相关文章推荐的样式 */
.about-article {
	display: inline-block;
	margin: 25px;
	font-weight: 700;
}

/* @font-face {
  font-family: 'iconfont';
  src: url('/font/iconfont.woff2?t=1682690394456') format('woff2'),
       url('/font/iconfont.woff?t=1682690394456') format('woff'),
       url('/font/iconfont.ttf?t=1682690394456') format('truetype');
} 
 */
/* @font-face {
  font-family: 'iconfont';
  src: url('/font/iconfont.woff2?t=1682700384068') format('woff2'),
       url('/font/iconfont.woff?t=1682700384068') format('woff'),
       url('/font/iconfont.ttf?t=1682700384068') format('truetype');
} */
@font-face {
  font-family: 'iconfont';
  src: url('/font/iconfont.woff2?t=1683105399944') format('woff2'),
       url('/font/iconfont.woff?t=1683105399944') format('woff'),
       url('/font/iconfont.ttf?t=1683105399944') format('truetype');
}

.iconfont {
  font-family: "iconfont" !important;
  font-size: 16px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.about-article-info {
	margin-left: 25px;
}
.about-article-info div:nth-child(n+2) {
	border-top: 1px solid #e9eaeb;
}
.article-info-row {
	padding-top: 15px;
	margin-bottom: 15px;
}

.article-info-row a {
	color: #545c63;
	font-size: 14px;
}
.article-info-row a:hover {
	color: #3377ff;
}
/* 文章详情下边的创建时间以及浏览人数 */
.article-create-time {
	margin-top: 40px;
	font-size: 14px;
}
.imooc {
	font-size: 14px;
	color: #9199a1;
	margin-top: 20px;
}

.praise {
	margin: 30px auto;
	height: 75px;
	width: 75px;
	border-radius: 50%;
	background: rgba(255,170,0,.1);
	line-height: 75px;
	text-align: center;
}
.praise:hover{
	background-color: #ffaa00;
}

.praise span{
	font-size: 45px;
	color: #ffaa00;
}
.praise span:hover{
	color: #fff;
	cursor: pointer;
	
}

/* 评论的样式 */
.feedback-num {
	width: 1152px;
	margin: 0 auto;
	margin-top: 30px;
	font-weight: 700;
}
.article-feedback {
	width: 1152px;
	margin: 0 auto;
}
.feedback-wrap {
	display: inline-block;
	background-color: #fff;
	width: 800px;
	border-radius: 10px;
	margin-top: 25px;
	padding-left: 30px;
	padding-top: 30px;
}

.useless-right {
	display: inline-block;
	width: 330px;
	/* border:1px solid red;'' */
	margin-left: 23px;
}

.write-feedback-wrap >div {
	display: inline-block;
	height: 50px;
	line-height: 50px;
	font-weight: 700;
}
.write-feedback-wrap > span{
	display: inline-block;
	height: 50px;
	line-height: 50px;
	width: 530px;
	background-color: #f3f5f6;
	color:#9e99a1;
	border-radius: 10px;
	margin-left: 30px;
	padding-left: 20px;
}


.feedback-author>a>img {
	display: block;
	width: 50px;
	height: 50px;
	border-radius: 50%;
	opacity: 0.8;
}

.feedback-author>a>img:hover {
	opacity: 1;
}
.feedback-author>a>span{
	display: block;
	width: 50px;
	text-align: center;
	color: #b7bbbf;
	font-size: 12px;
}
.feedback-content {
	margin-left: 20px;
}
.feedback-content>a{
	display: block;
	font-size: 14px;
}
.feedback-content>span{
	display: block;
	margin: 15px 0px;
}
.feedback-detail {
	margin-top: 20px;
	padding-top: 30px;
	border-top: 1px solid #ebebec;
	width: 740px;
}
/* 点赞的那个字体 */
.feedback-content{
	width: 80%;
}

.feedback-content-footer>span{
	display: inline-block;
	width: 50px;
	height: 30px;
	line-height: 30px;
	text-align: center;
	font-size: 20px;
	background-color: #ededee;
	border-radius: 15px;
}
.reply-button {
	display: inline-block;
	color: #9199a1;
	font-size: 12px;
	margin-left: 25px;
	height: 30px;
	line-height: 30px;
}
.publish-time {
	display: inline-block;
	color: #9199a1;
	font-size: 12px;
	height: 30px;
	line-height: 30px;
}


.reply-box {
	margin-left: 70px;
	margin-top: 30px;
}
.feedback-reply-content {
	margin-left: 15px;
}

.feedback-reply-content>a {
	color: #07111b;
	font-size: 14px;
	font-weight: 700;
}
.reply-text {
	color: #939994;
	font-size: 14px;
}
.reply2-button {
	display: inline-block;
	color: #9199a1;
	font-size: 12px;
	height: 30px;
	line-height: 30px;
}
.feedback-reply-content>a{
	font-size: 14px;
}

.feedback-reply-content {
	width: 75%;
}

/* 没有评论数据的样式 */
.no-data {
	margin: 0 auto;
	margin-top: 30px;
}
.no-data-line {
	height: 65px;
	width: 760px;
	text-align: center;
	border-top: 1px solid #ebebec;
	padding-top: 10px;
}
.no-data-line>span {
}

/* 发布评论的模态框样式 */
.feedback-modal-wrap .modal-content{
	width: 700px;
	margin-left: -200px;
}

.feedback-modal-wrap .modal-dialog{
	padding-top: 200px;
}
.feedback-modal-wrap .modal-title{
	padding-left: 30px;
	color: black;
}

/* 回复评论的评论的样式 */
.write-author-feedback {
	margin-top: 30px;
}


.write-author-feedback img{
	width: 50px;
	height: 50px;
	border-radius: 50%;
}
.write-author-feedback textarea{
	border: 1px solid #d9dde1;
	width: 450px;
	height: 80px;
	border-radius: 5px;
	vertical-align: top;
	margin-left: 30px;
	padding-top: 10px;
	padding-left: 15px;
	resize: none;
}

.write-author-feedback textarea:focus{
	outline: none;
	border: 1px solid #d9dde1;
}

.author-feedback-button {
	width: 520px;
	text-align: right;
	margin-top: 10px;
}
.author-feedback-button button{
	width: 60px;
	height: 40px;
	border-radius: 25px;
	font-size: 14px;
}
.cancel-author-feedback{
	border: 1px solid #93999f;
	background-color: #fff;
	color: #93999f;
	
}
.cancel-author-feedback:hover{
	border: 1px solid #a6abb0;
	background-color: #fff;
	color: #4d555d;
	
}


.confirm-author-feedback{
	background-color: #3377ff;
	border: 1px solid #3377ff;
	color: #fff;
}

```

### css/base.css

```
* {
	margin: 0;
	padding: 0;
	/* css3的盒子模型 */
	box-sizing: border-box;
}
em,
i {
	font-style: none;
}

li {
	list-style-type: none;
}

img {
	border: 0;
	vertical-align: middle;
}

a {
	color: #545C63;
	text-decoration: none;
}

input {
	border: 0;
	outline: none;
}

html,
body {
	background-color: #f3f5f6;
	font-size: 16px;
}


.clearfix:after
			   {
				content: "";
				display: block;
				height: 0;
				clear: both;
				visibility: hidden;
			}
.fl {
	float: left;
}
.fr {
	float: right;
}


/* @font-face {
  font-family: 'iconfont';
  src: url('../../../font/iconfont.ttf?t=1680263401838') format('truetype');
} */

@font-face {
  font-family: 'iconfont';
  src: url('/font/iconfont.woff2?t=1683105399944') format('woff2'),
       url('/font/iconfont.woff?t=1683105399944') format('woff'),
       url('/font/iconfont.ttf?t=1683105399944') format('truetype');
}
.iconfont {
  font-family: "iconfont" !important;
  font-size: 16px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

### css/index.css

```
/* 头部的样式 */
.header {
	height: 65px;
	border-bottom: 1px solid #f3f5f6;
	background-color: #fff;
	position: sticky;
	top: 0;
}
.header-container {
	width: 1155px;
	/* border: 1px solid red; */
	margin: 0 auto;
	height: 65px;
	line-height: 65px;
}
.header-left span {
	margin-right: 20px;
}
.header-left span a:hover {
	color: #1c1f21;
}
.header-left span:nth-child(4) {
	display: inline-block;
	position: relative;
	width: 65px;
	height: 25px;
	line-height: 25px;
}
.header-left span:nth-child(8) {
	display: inline-block;
	position: relative;
	width: 80px;
	height: 25px;
	line-height: 25px;
}

.header-left span img {
	position: absolute;
	top: 0;
	right: 0;
	height: 10px;
}
.header-right>span {
	margin-left: 15px;
}

.header-right>span>i {
	font-size: 18px;
}
.header-right>span>i:hover {
	color: red;
	cursor: pointer;
}
.login a:hover {
	color: red;
}
/* 我是子头部的样式 */
.sub-header {
	height: 80px;
	background-color: #fff;
}
.sub-header-container {
	/* border: 1px solid red; */
	width: 1155px;
	margin: 0 auto;
	height: 80px;
	line-height: 80px;
}

.sub-header-left img:first-child {
	height: 54px;
}
.sub-header-left img:last-child {
	height: 19px;
	margin-bottom: -14px;
}
.sub-header-right {
	margin-top: 25px;
	width: 880px;
	padding-left: 470px;
}

.sub-header-right input{
	border: 1px solid #dddee0;
	width: 280px;
	height: 35px;
	border-top-left-radius: 5px;
	border-bottom-left-radius: 5px;
	color: #9199a1;
	font-size: 12px;
	padding: 8px 16px;
}
.sub-header-right>span {
	display: inline-block;
	background-color: #545c63;
	height: 35px;
	width: 35px;
	line-height: 35px;
	margin-right: 15px;
	text-align: center;
	color: #fff;
	border-top-right-radius: 5px;
	border-bottom-right-radius: 5px;
}

.sub-header-right>span:hover{
	cursor: pointer;
}
.sub-header-right button {
	height: 35px;
	line-height: 35px;
	width: 80px;
	background-color: #3377ff;
	border: 0;
	color: #fff;
	border-radius: 5px;
}
.sub-header-right button:hover {
	cursor: pointer;
}

/* 我是文章内容部分的样式 */
.article-container {
	width: 1155px;
	margin: 20px auto;
	/* border: 1px solid red; */
}
.left-menu {
	width: 105px;
	height: 350px;
	background-color: #fff;
	border-radius: 10px;
}
.left-menu>div {
	width: 90px;
	height: 40px;
	text-align: center;
	margin-top: 10px;
	margin-left: 8px;
	line-height: 40px;
}

.left-menu .selected {
	background-color: #eaf1ff;
	border-radius: 5px;
}
.left-menu .selected a {
	color: #3377ff;
	font-weight: 700;
}
.left-menu>div>a {
	font-size: 14px;
}

.left-menu>div>a:hover {
	color: #33a4ff;
}


.article-warpper {
	width: 1025px;
	background-color: #fff;
	margin-left: 20px;
	border-radius: 10px;
	/* height: 1500px; */
}

.article-inner {
	margin: 20px 20px;
}
.article-row {
	/* border: 1px solid red; */
	height: 80px;

}

.article-row>div{
	display: inline-block;
}

.article-header-image img{
	width: 66px;
	height: 66px;
	border-radius: 5px;
}
.article-name {
	height: 36px;
	line-height: 36px;
	font-weight: 700;
	color: #1c1f21;
}

.article-name:hover {
	color: #3377ff;
	cursor: pointer;
}

.article-name a {
	height: 36px;
	line-height: 36px;
	font-weight: 700;
	color: #1c1f21;
}

.article-name a:hover {
	color: #3377ff;
	cursor: pointer;
}
.article-desc {
	margin-left: 15px;
	width: 900px;
	height: 75px;
	line-height: 75px;
	border-bottom: 1px solid #e8e8e8;

}
.article-info {
	/* border:  1px solid red; */
	height: 36px;
	line-height: 36px;
}
.article-left span {
	display: inline-block;
	height: 25px;
	line-height: 25px;
	text-align: center;
	font-size: 12px;
	margin-right: 20px;
}
.article-left span:nth-child(2)::before {
	content: "\e8bf";
}
.article-left span:first-child {
	color: #1c1f21;
	background: rgba(84,92,99,0.1);
	width: 75px;
	border-radius: 13px;
}
.article-left span:nth-child(n+2) {
	color: #9199a1;
	font-size: 12px;
}
.article-right {
	color: #9199a1;
	font-size: 12px;
}

/* 下拉加载更多的样式 */
.load-more {
	height: 50px;
	line-height: 50px;
	text-align: center;
	color: #9199a1;
	font-size: 12px;
}

.login a img{
	height: 35px;
	border-radius: 50%;
	border: 2px solid #f3f5f6;
}
.login a img:hover{
	border:2px solid #f01616;
}

```

### css/login.css

```
.modal-dialog {
	width: 420px;
}
.modal-title {
	color: red;
	padding-left: 40%;
	font-weight: 700;
}
.mb-3 input {
	background-color: #f0f0f0;
}
.modal-body {
	margin: 0 auto;
}
.modal-body form {
	width: 350px;
}
.auth-code {
	display: inline-block;
	width: 265px;
	height: 38px;
	border-radius: 5px;
	padding-left: 10px;
	border:1px solid #dee2e6;
}
.login-button {
	background-color: red;
	width: 350px;
	border: 1px solid transparent;
	border-radius: 20px;
}

/* 下边是注册的样式 */
.send {
	width: 80px;
	height: 35px;
	border: 1px solid #48615b;
	color: #48615b;
	border-radius: 5px;
}

.register {
	color: red;
	font-weight: 700;
	width: 418px;
	text-align: center;
	
}
.register:hover {
	cursor: pointer;
}
```

### css/new-article.css

```
.header>div {
	display: inline-block;
	width: 33%;
	/* border: 1px solid red; */
}

.header {
	margin: 0px 20px 40px 20px;
	
	padding-top: 40px;
}
.header span {
	display: inline-block;
	height: 38px;
	line-height: 38px;
	text-align: center;
	border-radius: 19px;
}
.left span {
	width: 110px;
	background-color: #e2e4e6;
	font-size: 14px;
	color: #545c63;
	
}

.mid span {
	margin-left: 40%;
	width: 86px;
	background-color: #9199a1;
	font-size: 12px;
	color: #fff;
}
.right {
	text-align: right;
}
.right span {
	width: 90px;
	background-color: #3377ff;
	font-size: 14px;
	color: #fff;
}

.main {
	background-color: #fff;
	width: 900px;
	margin: 25px auto;
	border-radius: 10px;
	padding-left: 50px;
}

.article-header{
	margin-top: 20px;
	height: 30px;
	line-height: 30px;
	width: 800px;
	margin-bottom: 10px;
}

.article-header::placeholder{
	font-size: 20px;
	font-weight: 700;
}

.publish:hover{
	cursor: pointer;
}

body {
	background-color: #f3f5f6 !important;
}

/* 文章发布模态框样式 */
.modal-content {
	width: 670px !important;
	height: 470px !important;
	margin-top: 240px;
}
.publish-left {
	width: 190px;
	height: 410px;
	/* background-color: red; */
	margin-top: 20px;
}
.publish-right{
	width: 445px;
	height:  410px;
	/* background-color: blue; */
	margin-top: 20px;
}

/* 左侧的样式 */
.upload-header-image{
	width: 130px;
	height: 130px;
	line-height: 130px;
	text-align: center;
	background-color: #f8fafc;
	border-radius: 10px;
	margin-left: 20px;
}


.upload-header-image img{
	width: 40px;
	height: 40px;
}

.upload-header-image img:hover{
	cursor: pointer;
}
.upload-header-button {
	margin-top: 15px;
	height: 25px;
	width: 130px;
	border-radius: 12px;
	background-color: #383d42;
	color: white;
	text-align: center;
	line-height: 25px;
	margin-left: 20px;
	font-size: 12px;
}

.upload-header-button:hover {
	cursor: pointer;
}
.random-header {
	margin-top: 15px;
	height: 25px;
	width: 130px;
	border-radius: 12px;
	background-color: #ededee;
	color: #60676e;
	text-align: center;
	line-height: 25px;
	margin-left: 20px;
	font-size: 12px;
}

.random-header:hover {
	cursor: pointer;
}
.upload-desc {
	margin-top: 15px;
	width: 130px;
	color: #9199a1;
	margin-left: 20px;
	font-size: 12px;
}

/* 文章发布右侧 */
/* article-cloumns
 
 */
/* 投递栏目的样式 */
.article-label-name {
	font-size: 14px;
	font-weight: 700;
}
.article-label-value {
	position: relative;
	width: 280px;
	height: 40px;
	line-height: 40px;
	border-radius: 10px;
	border: 1px solid #9199a1;
	font-size: 14px;
	padding-left: 15px;
	margin-top: 10px;
}
.article-label-list {
	position:absolute;
	background-color: #fff;
	width: 100%;
	border: 1px solid #f3f5f6;
	border-radius: 10px;
	margin-left: -15px;
	
}
.article-label-value .article-label-list div{
	font-size: 14px;
	
}
.article-label-value .article-label-list div li{
	padding-left: 20px;
	
}
.article-label-selected {
	background-color: #f3f5f6;
}
.article-label-value .iconfont{
	margin-left: 90px;
	color: #9199a1;
	font-size: 14px;
}
/* 文章类型的样式 */
.article-type-name{
	font-size: 14px;
	font-weight: 700;
}
.article-type-value {
	position:relative;
	background-color: #fff;
	width: 140px;
	border: 1px solid #9199a1;
	border-radius: 10px;
	margin-left: 10px;
	height: 40px;
	line-height: 40px;
	margin-top: 10px;
	font-size: 14px;
	padding-left: 15px;
}
.article-type-list {
	position: absolute;
	background-color: #fff;
	width: 100%;
	border: 1px solid #f3f5f6;
	border-radius: 10px;
	margin-left: -15px;
}
.article-type-value .iconfont {
	margin-left: 45px;
	color: #9199a1;
	font-size: 14px;
}

.article-label-value>span:first-child{
	display: inline-block;
	width: 140px;
}
/* .article-type-selected { */
.selected{
	background-color: #f3f5f6;
}
.article-type-value>span:first-child{
	display: inline-block;
	width: 45px;
}

.article-type-value .article-type-list div li{
	padding-left: 20px;
}

/* 文章标签的样式 */
.article-tags{
	margin-top: 10px;
}

/* .article-tag-name span:nth-child(1){ */
.article-tag-name>span:nth-child(1){
	font-weight: 700;
	font-size: 14px;
}
/* .article-tag-name span:nth-child(2){ */
.article-tag-name>span:nth-child(2){
	font-size: 12px;
	color: #93999f;
	margin-left: 10px;
}
/* 选择标签的样式 */
/* .article-tag-value input{
	width: 430px;
	height: 35px;
	line-height: 35px;
	margin-top: 10px;
	font-size: 14px;
	border: 1px solid #9199a1;
	border-radius: 10px;
	padding-left: 15px;
} */
.article-tag-value::placeholder{
	color: #93999f;
	font-size: 14px;
	/* padding-left: 15px; */
}
.article-tag-list {
	margin-top: 10px;
	height: 180px;
}
.article-tag-list span{
	display: inline-block;
	height: 25px;
	line-height: 25px;
	text-align: center;
	padding-left:10px;
	padding-right: 10px;
	background-color: #eeeeef;
	color: #545c63;
	font-size: 12px;
	border-radius: 12px;
	margin-left: 5px;
}
/* 两个按钮的样式 */
.saveAndCancelButton{
	margin-left: 210px;
	width: 110px;
	height: 35px;
	line-height: 35px;
	text-align: center;
	border: 1px solid #ededee;
	background-color: #ededee;
	color: #9ca0a4;
	font-size: 14px;
	border-radius: 17px;
}

.publishButton {
	height: 35px;
	line-height: 35px;
	width: 100px;
	margin-left: 15px;
	font-size: 14px;
	background-color: #3377ff;
	border: 1px solid #3377ff;
	color: white;
	border-radius: 17px;
}

/* 我的草稿样式 */
.header .left > span{
	position: relative;
}

.header .left > span:hover{
	cursor: pointer;
}

.header .left .drafted-num {
	display: inline-block;
	position: absolute;
	right: 0;
	width: 17px;
	height: 17px;
	line-height: 17px;
	text-align: center;
	background-color: #f20d0d;
	color: white;
	font-size: 12px;
	border-radius: 50%;
}

/* 草稿列表的样式 */
.header .left{
	position: relative;
}
.drafted-info {
	position: absolute;
}
.drafted-info .drafted-list{
	background-color: #fff;
	width: 385px;
	/* height: 365px; */
	border-radius: 10px;
	margin-top: -23px;
	padding-left: 20px;
}
.drafted-info>div:first-child{
	font-size: 40px;
	color: white;
	margin-left: 20px;
	margin-top: -20px;
}
.drafted-info .drafted-list>i{
	display: inline-block;
	font-style: normal;
	font-weight: 700;
	font-size: 14px;
	margin-top: 20px;
	margin-bottom: 20px;
}
.drafted-list>div{
	width: 350px;
	height: 60px;
	line-height: 60px;
	border-radius: 10px;
	margin-bottom: 10px;
	background-color: #f3f5f6;
}
.drafted-list>div:hover{
	background-color: #e5eeff;
	cursor: pointer;
}
.drafted-icon i{
	font-size: 25px;
	height: 60px;
	line-height: 60px;
	margin-left: 10px;
}
.drafted-create {
	margin-left: 10px;
}
.drafted-create .drafted-name:hover{
	color:#0055ff;
}
.drafted-create .drafted-name{
	margin-top: 10px;
	color:#545c63;
	font-size: 14px;
	line-height: 20px;
	font-weight: 700;

}
.drafted-create .drafted-update-time{
	line-height: 20px;
	font-size: 12px;
	color:#9199a1;
}

/* 文章标签选择的样式 */
/* 选择标签的样式 */
.article-tag-value{
	width: 430px;
	/* height: 35px; */
	line-height: 35px;
	margin-top: 10px;
	font-size: 14px;
	border: 1px solid #9199a1;
	border-radius: 10px;
	padding-left: 15px;
}

.change-tags{
	margin-right: 10px;
}
.change-tags>span{
	height: 25px;
	line-height: 25px;
	padding:5px 10px;
	background-color: #eeeeef;
	border-radius: 13px;
	font-size: 12px;
	color:#545c63;
	margin-left: 5px;
}
/* 草稿名字溢出之后显示3个点 */
.drafted-name {
	/* 让文本不换行 */
	white-space: nowrap;
	/* 溢出隐藏 */
	overflow: hidden;
	text-overflow: ellipsis;
	width: 250px;
}
```

### css/personal_center.css

```
.person-center-header{
	height: 150px;
	background: url("/images/personal_background.png") no-repeat center top;
}
.user-info {
	width: 1154px;
	margin: 0 auto;
	}
.user-picture {
	margin-top: 25px;
}

.user-picture img{
	width: 150px;
	height: 150px;
	border-radius: 50%;
	border: 2px solid white;
}
.personal-name {
	font-size: 24px;
	color: white;
	margin-top: 50px;
	margin-left: 20px;
	font-weight: 700;
}
body{
	background-color: #fff !important;
}
.personal-main {
	margin-top: 50px;
}
.personal-content {
	width: 1154px;
	margin: 0 auto;
}

/* css原生绘制三角形 */

/* .every-menu {
	width: 0;
	height: 0; 
	border-top: 30px solid blue;
	border-bottom: 20px solid yellow;
	border-left: 30px solid red;
	border-right: 30px solid green;
} */

.menu>div{
	height: 48px;
	line-height: 48px;
	width: 145px;
	text-align: center;
	border-top-left-radius: 10px;
	border-bottom-left-radius: 10px;
}
.menu .active{
	background-color: #f34343;
	font-weight: 700;
}
.menu .active a{
	color: white;
	position: relative;
}
.menu .every-menu{
	
}

.menu .active a::after{
	position: absolute;
	content: "";
	border-top: 24px solid white;
	border-bottom: 24px solid white;
	border-left: 15px solid #f34343;
	border-right: 24px solid white;
	margin-left: 20px;
}
.content {
	margin-left: 50px;
}
.menu>div span:nth-child(2){
	margin-left: 8px;
}
html {
	background-color: #fff;
}

.content {
	width: 940px;
}
.every-item {
	border-bottom: 1px solid #edf1f2;
}

.no-item{
	height: 300px;
	line-height: 330px;
	text-align: center;
	font-size: 18px;
	color:#b5b9bc;
}
.no-item a{
	color: #f01400;
	font-weight: 700;
}
.item-title {
	margin: 15px 0;
}
.item-title a{
	color: #14191e;
	font-size: 20px;
	font-weight: 700;
	margin: 25px 0;
}
.item-title a:hover{
	color: #f01400;
}
.item-title span{
	border:1px solid #71777d;
	color: #71777d;
	font-size: 12px;
	padding: 5px 10px;
}
.item-image img{
	width: 210px;
	height: 130px;
}
.item-text {
	height: 130px;
	width: 700px;
	color: #4d555d;
	font-size: 14px;
	margin-left: 30px;
	line-height: 25px;
}
.item-info {
	color: #b5b9bc;
	font-size: 14px;
	padding-bottom: 15px;
	text-align: right;
	
}
.item-info span{
	margin-left: 10px;
}
```

### js/article-info.js

```
function favoriteUpdate(articleId,canceled){
	axios.post("/favorite/update_status",{
		article_id:articleId,
		canceled:canceled
	}).then((res)=>{
		if(res.data.status==3000){
			window.location.reload()
		}else{
			alert(res.data.data);
		}
	})
}

//  发布评论的return true;
var ue = UE.getEditor('feedback-container', {
		        // ... 更多配置
				shortcutMenu: false,
				elementPathEnabled : false,
				wordCount:false,
				autoHeightEnabled:false,
				// 初始化编辑器宽度,默认 1000
				initialFrameWidth:600,
				// 初始化编辑器高度,默认 320
				initialFrameHeight:150,
				serverUrl:"http://127.0.0.1:5000/feedback",
				toolbars: [
				  [
					   "insertcode",  
					    "bold",         // 加粗
					    "italic",       // 斜体
					    // "insertimage",  
						"link",
					    "insertorderedlist",   // 有序列表
					    "insertunorderedlist", // 无序列表
					    "undo",         // 撤销
					    "redo",         // 重做
					    // "emotion",             // 表情
				  ]
					  ]
		    });

// 发布评论
function addFeedback(articleId){
	var feedbackContent = ue.getContent();
	axios.post("/feedback/add",{
		article_id:articleId,
		content:feedbackContent
	}).then((res)=>{
		alert(res.data.data);
		window.location.reload();
	})
}

// 显示评论具体作者的回复输入框是否展示
var ifShowInputWrap=false;
// 存储当前打开的输入框id，用来控制关闭
var currentWriteAuthorInputId=0;
// 存储当前评论相关的信息，用来向后端发起请求，默认值都给0
var baseReplyId = 0;
var replyArticleId = 0;
var feedbackReplyId=0;
	
// 显示输入框
function showWriteAuthorInput(inputId,articleId,userId,nickname,replyId){
	baseReplyId = inputId;
	replyArticleId = articleId;
	feedbackReplyId=replyId;
	// 关闭当前已经打开的输入框
	if(currentWriteAuthorInputId != 0){
		hiddenWriteAuthorInput(currentWriteAuthorInputId);
	}
	currentWriteAuthorInputId = inputId;
	var inputWarp = document.getElementById(inputId);
	inputWarp.style.display="block";
	
}


// 隐藏输入框
function hiddenWriteAuthorInput(inputId){
	var inputWarp = document.getElementById(inputId);
	inputWarp.style.display="none";
}

// 发布回复评论的评论
function writeReply(){
	var content = document.getElementById(baseReplyId).querySelector("textarea").value;
	axios.post("/feedback/reply",{
		article_id:replyArticleId,
		content:content,
		reply_id:feedbackReplyId,
		base_reply_id:baseReplyId
	}).then((res)=>{
		alert(res.data.data);
		window.location.reload();
	})
	
}
```

### js/axios.min.js

```
!function(e,t){"object"==typeof exports&&"undefined"!=typeof module?module.exports=t():"function"==typeof define&&define.amd?define(t):(e="undefined"!=typeof globalThis?globalThis:e||self).axios=t()}(this,(function(){"use strict";function e(t){return e="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},e(t)}function t(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function n(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}function r(e,t,r){return t&&n(e.prototype,t),r&&n(e,r),Object.defineProperty(e,"prototype",{writable:!1}),e}function o(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var n=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==n)return;var r,o,i=[],a=!0,s=!1;try{for(n=n.call(e);!(a=(r=n.next()).done)&&(i.push(r.value),!t||i.length!==t);a=!0);}catch(e){s=!0,o=e}finally{try{a||null==n.return||n.return()}finally{if(s)throw o}}return i}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return i(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);"Object"===n&&e.constructor&&(n=e.constructor.name);if("Map"===n||"Set"===n)return Array.from(e);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return i(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function i(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}function a(e,t){return function(){return e.apply(t,arguments)}}var s,u=Object.prototype.toString,c=Object.getPrototypeOf,f=(s=Object.create(null),function(e){var t=u.call(e);return s[t]||(s[t]=t.slice(8,-1).toLowerCase())}),l=function(e){return e=e.toLowerCase(),function(t){return f(t)===e}},d=function(t){return function(n){return e(n)===t}},p=Array.isArray,h=d("undefined");var m=l("ArrayBuffer");var y=d("string"),v=d("function"),b=d("number"),g=function(t){return null!==t&&"object"===e(t)},w=function(e){if("object"!==f(e))return!1;var t=c(e);return!(null!==t&&t!==Object.prototype&&null!==Object.getPrototypeOf(t)||Symbol.toStringTag in e||Symbol.iterator in e)},E=l("Date"),O=l("File"),S=l("Blob"),R=l("FileList"),A=l("URLSearchParams");function T(t,n){var r,o,i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},a=i.allOwnKeys,s=void 0!==a&&a;if(null!=t)if("object"!==e(t)&&(t=[t]),p(t))for(r=0,o=t.length;r<o;r++)n.call(null,t[r],r,t);else{var u,c=s?Object.getOwnPropertyNames(t):Object.keys(t),f=c.length;for(r=0;r<f;r++)u=c[r],n.call(null,t[u],u,t)}}function j(e,t){t=t.toLowerCase();for(var n,r=Object.keys(e),o=r.length;o-- >0;)if(t===(n=r[o]).toLowerCase())return n;return null}var N="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof self?self:"undefined"!=typeof window?window:global,x=function(e){return!h(e)&&e!==N};var C,P=(C="undefined"!=typeof Uint8Array&&c(Uint8Array),function(e){return C&&e instanceof C}),k=l("HTMLFormElement"),U=function(e){var t=Object.prototype.hasOwnProperty;return function(e,n){return t.call(e,n)}}(),_=l("RegExp"),F=function(e,t){var n=Object.getOwnPropertyDescriptors(e),r={};T(n,(function(n,o){!1!==t(n,o,e)&&(r[o]=n)})),Object.defineProperties(e,r)},B="abcdefghijklmnopqrstuvwxyz",L="0123456789",D={DIGIT:L,ALPHA:B,ALPHA_DIGIT:B+B.toUpperCase()+L};var I={isArray:p,isArrayBuffer:m,isBuffer:function(e){return null!==e&&!h(e)&&null!==e.constructor&&!h(e.constructor)&&v(e.constructor.isBuffer)&&e.constructor.isBuffer(e)},isFormData:function(e){var t;return e&&("function"==typeof FormData&&e instanceof FormData||v(e.append)&&("formdata"===(t=f(e))||"object"===t&&v(e.toString)&&"[object FormData]"===e.toString()))},isArrayBufferView:function(e){return"undefined"!=typeof ArrayBuffer&&ArrayBuffer.isView?ArrayBuffer.isView(e):e&&e.buffer&&m(e.buffer)},isString:y,isNumber:b,isBoolean:function(e){return!0===e||!1===e},isObject:g,isPlainObject:w,isUndefined:h,isDate:E,isFile:O,isBlob:S,isRegExp:_,isFunction:v,isStream:function(e){return g(e)&&v(e.pipe)},isURLSearchParams:A,isTypedArray:P,isFileList:R,forEach:T,merge:function e(){for(var t=x(this)&&this||{},n=t.caseless,r={},o=function(t,o){var i=n&&j(r,o)||o;w(r[i])&&w(t)?r[i]=e(r[i],t):w(t)?r[i]=e({},t):p(t)?r[i]=t.slice():r[i]=t},i=0,a=arguments.length;i<a;i++)arguments[i]&&T(arguments[i],o);return r},extend:function(e,t,n){var r=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{},o=r.allOwnKeys;return T(t,(function(t,r){n&&v(t)?e[r]=a(t,n):e[r]=t}),{allOwnKeys:o}),e},trim:function(e){return e.trim?e.trim():e.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"")},stripBOM:function(e){return 65279===e.charCodeAt(0)&&(e=e.slice(1)),e},inherits:function(e,t,n,r){e.prototype=Object.create(t.prototype,r),e.prototype.constructor=e,Object.defineProperty(e,"super",{value:t.prototype}),n&&Object.assign(e.prototype,n)},toFlatObject:function(e,t,n,r){var o,i,a,s={};if(t=t||{},null==e)return t;do{for(i=(o=Object.getOwnPropertyNames(e)).length;i-- >0;)a=o[i],r&&!r(a,e,t)||s[a]||(t[a]=e[a],s[a]=!0);e=!1!==n&&c(e)}while(e&&(!n||n(e,t))&&e!==Object.prototype);return t},kindOf:f,kindOfTest:l,endsWith:function(e,t,n){e=String(e),(void 0===n||n>e.length)&&(n=e.length),n-=t.length;var r=e.indexOf(t,n);return-1!==r&&r===n},toArray:function(e){if(!e)return null;if(p(e))return e;var t=e.length;if(!b(t))return null;for(var n=new Array(t);t-- >0;)n[t]=e[t];return n},forEachEntry:function(e,t){for(var n,r=(e&&e[Symbol.iterator]).call(e);(n=r.next())&&!n.done;){var o=n.value;t.call(e,o[0],o[1])}},matchAll:function(e,t){for(var n,r=[];null!==(n=e.exec(t));)r.push(n);return r},isHTMLForm:k,hasOwnProperty:U,hasOwnProp:U,reduceDescriptors:F,freezeMethods:function(e){F(e,(function(t,n){if(v(e)&&-1!==["arguments","caller","callee"].indexOf(n))return!1;var r=e[n];v(r)&&(t.enumerable=!1,"writable"in t?t.writable=!1:t.set||(t.set=function(){throw Error("Can not rewrite read-only method '"+n+"'")}))}))},toObjectSet:function(e,t){var n={},r=function(e){e.forEach((function(e){n[e]=!0}))};return p(e)?r(e):r(String(e).split(t)),n},toCamelCase:function(e){return e.toLowerCase().replace(/[-_\s]([a-z\d])(\w*)/g,(function(e,t,n){return t.toUpperCase()+n}))},noop:function(){},toFiniteNumber:function(e,t){return e=+e,Number.isFinite(e)?e:t},findKey:j,global:N,isContextDefined:x,ALPHABET:D,generateString:function(){for(var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:16,t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:D.ALPHA_DIGIT,n="",r=t.length;e--;)n+=t[Math.random()*r|0];return n},isSpecCompliantForm:function(e){return!!(e&&v(e.append)&&"FormData"===e[Symbol.toStringTag]&&e[Symbol.iterator])},toJSONObject:function(e){var t=new Array(10);return function e(n,r){if(g(n)){if(t.indexOf(n)>=0)return;if(!("toJSON"in n)){t[r]=n;var o=p(n)?[]:{};return T(n,(function(t,n){var i=e(t,r+1);!h(i)&&(o[n]=i)})),t[r]=void 0,o}}return n}(e,0)}};function q(e,t,n,r,o){Error.call(this),Error.captureStackTrace?Error.captureStackTrace(this,this.constructor):this.stack=(new Error).stack,this.message=e,this.name="AxiosError",t&&(this.code=t),n&&(this.config=n),r&&(this.request=r),o&&(this.response=o)}I.inherits(q,Error,{toJSON:function(){return{message:this.message,name:this.name,description:this.description,number:this.number,fileName:this.fileName,lineNumber:this.lineNumber,columnNumber:this.columnNumber,stack:this.stack,config:I.toJSONObject(this.config),code:this.code,status:this.response&&this.response.status?this.response.status:null}}});var M=q.prototype,z={};["ERR_BAD_OPTION_VALUE","ERR_BAD_OPTION","ECONNABORTED","ETIMEDOUT","ERR_NETWORK","ERR_FR_TOO_MANY_REDIRECTS","ERR_DEPRECATED","ERR_BAD_RESPONSE","ERR_BAD_REQUEST","ERR_CANCELED","ERR_NOT_SUPPORT","ERR_INVALID_URL"].forEach((function(e){z[e]={value:e}})),Object.defineProperties(q,z),Object.defineProperty(M,"isAxiosError",{value:!0}),q.from=function(e,t,n,r,o,i){var a=Object.create(M);return I.toFlatObject(e,a,(function(e){return e!==Error.prototype}),(function(e){return"isAxiosError"!==e})),q.call(a,e.message,t,n,r,o),a.cause=e,a.name=e.name,i&&Object.assign(a,i),a};function H(e){return I.isPlainObject(e)||I.isArray(e)}function J(e){return I.endsWith(e,"[]")?e.slice(0,-2):e}function W(e,t,n){return e?e.concat(t).map((function(e,t){return e=J(e),!n&&t?"["+e+"]":e})).join(n?".":""):t}var K=I.toFlatObject(I,{},null,(function(e){return/^is[A-Z]/.test(e)}));function V(t,n,r){if(!I.isObject(t))throw new TypeError("target must be an object");n=n||new FormData;var o=(r=I.toFlatObject(r,{metaTokens:!0,dots:!1,indexes:!1},!1,(function(e,t){return!I.isUndefined(t[e])}))).metaTokens,i=r.visitor||f,a=r.dots,s=r.indexes,u=(r.Blob||"undefined"!=typeof Blob&&Blob)&&I.isSpecCompliantForm(n);if(!I.isFunction(i))throw new TypeError("visitor must be a function");function c(e){if(null===e)return"";if(I.isDate(e))return e.toISOString();if(!u&&I.isBlob(e))throw new q("Blob is not supported. Use a Buffer instead.");return I.isArrayBuffer(e)||I.isTypedArray(e)?u&&"function"==typeof Blob?new Blob([e]):Buffer.from(e):e}function f(t,r,i){var u=t;if(t&&!i&&"object"===e(t))if(I.endsWith(r,"{}"))r=o?r:r.slice(0,-2),t=JSON.stringify(t);else if(I.isArray(t)&&function(e){return I.isArray(e)&&!e.some(H)}(t)||(I.isFileList(t)||I.endsWith(r,"[]"))&&(u=I.toArray(t)))return r=J(r),u.forEach((function(e,t){!I.isUndefined(e)&&null!==e&&n.append(!0===s?W([r],t,a):null===s?r:r+"[]",c(e))})),!1;return!!H(t)||(n.append(W(i,r,a),c(t)),!1)}var l=[],d=Object.assign(K,{defaultVisitor:f,convertValue:c,isVisitable:H});if(!I.isObject(t))throw new TypeError("data must be an object");return function e(t,r){if(!I.isUndefined(t)){if(-1!==l.indexOf(t))throw Error("Circular reference detected in "+r.join("."));l.push(t),I.forEach(t,(function(t,o){!0===(!(I.isUndefined(t)||null===t)&&i.call(n,t,I.isString(o)?o.trim():o,r,d))&&e(t,r?r.concat(o):[o])})),l.pop()}}(t),n}function G(e){var t={"!":"%21","'":"%27","(":"%28",")":"%29","~":"%7E","%20":"+","%00":"\0"};return encodeURIComponent(e).replace(/[!'()~]|%20|%00/g,(function(e){return t[e]}))}function $(e,t){this._pairs=[],e&&V(e,this,t)}var X=$.prototype;function Q(e){return encodeURIComponent(e).replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}function Z(e,t,n){if(!t)return e;var r,o=n&&n.encode||Q,i=n&&n.serialize;if(r=i?i(t,n):I.isURLSearchParams(t)?t.toString():new $(t,n).toString(o)){var a=e.indexOf("#");-1!==a&&(e=e.slice(0,a)),e+=(-1===e.indexOf("?")?"?":"&")+r}return e}X.append=function(e,t){this._pairs.push([e,t])},X.toString=function(e){var t=e?function(t){return e.call(this,t,G)}:G;return this._pairs.map((function(e){return t(e[0])+"="+t(e[1])}),"").join("&")};var Y,ee=function(){function e(){t(this,e),this.handlers=[]}return r(e,[{key:"use",value:function(e,t,n){return this.handlers.push({fulfilled:e,rejected:t,synchronous:!!n&&n.synchronous,runWhen:n?n.runWhen:null}),this.handlers.length-1}},{key:"eject",value:function(e){this.handlers[e]&&(this.handlers[e]=null)}},{key:"clear",value:function(){this.handlers&&(this.handlers=[])}},{key:"forEach",value:function(e){I.forEach(this.handlers,(function(t){null!==t&&e(t)}))}}]),e}(),te={silentJSONParsing:!0,forcedJSONParsing:!0,clarifyTimeoutError:!1},ne={isBrowser:!0,classes:{URLSearchParams:"undefined"!=typeof URLSearchParams?URLSearchParams:$,FormData:"undefined"!=typeof FormData?FormData:null,Blob:"undefined"!=typeof Blob?Blob:null},isStandardBrowserEnv:("undefined"==typeof navigator||"ReactNative"!==(Y=navigator.product)&&"NativeScript"!==Y&&"NS"!==Y)&&"undefined"!=typeof window&&"undefined"!=typeof document,isStandardBrowserWebWorkerEnv:"undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope&&"function"==typeof self.importScripts,protocols:["http","https","file","blob","url","data"]};function re(e){function t(e,n,r,o){var i=e[o++],a=Number.isFinite(+i),s=o>=e.length;return i=!i&&I.isArray(r)?r.length:i,s?(I.hasOwnProp(r,i)?r[i]=[r[i],n]:r[i]=n,!a):(r[i]&&I.isObject(r[i])||(r[i]=[]),t(e,n,r[i],o)&&I.isArray(r[i])&&(r[i]=function(e){var t,n,r={},o=Object.keys(e),i=o.length;for(t=0;t<i;t++)r[n=o[t]]=e[n];return r}(r[i])),!a)}if(I.isFormData(e)&&I.isFunction(e.entries)){var n={};return I.forEachEntry(e,(function(e,r){t(function(e){return I.matchAll(/\w+|\[(\w*)]/g,e).map((function(e){return"[]"===e[0]?"":e[1]||e[0]}))}(e),r,n,0)})),n}return null}var oe={"Content-Type":void 0};var ie={transitional:te,adapter:["xhr","http"],transformRequest:[function(e,t){var n,r=t.getContentType()||"",o=r.indexOf("application/json")>-1,i=I.isObject(e);if(i&&I.isHTMLForm(e)&&(e=new FormData(e)),I.isFormData(e))return o&&o?JSON.stringify(re(e)):e;if(I.isArrayBuffer(e)||I.isBuffer(e)||I.isStream(e)||I.isFile(e)||I.isBlob(e))return e;if(I.isArrayBufferView(e))return e.buffer;if(I.isURLSearchParams(e))return t.setContentType("application/x-www-form-urlencoded;charset=utf-8",!1),e.toString();if(i){if(r.indexOf("application/x-www-form-urlencoded")>-1)return function(e,t){return V(e,new ne.classes.URLSearchParams,Object.assign({visitor:function(e,t,n,r){return ne.isNode&&I.isBuffer(e)?(this.append(t,e.toString("base64")),!1):r.defaultVisitor.apply(this,arguments)}},t))}(e,this.formSerializer).toString();if((n=I.isFileList(e))||r.indexOf("multipart/form-data")>-1){var a=this.env&&this.env.FormData;return V(n?{"files[]":e}:e,a&&new a,this.formSerializer)}}return i||o?(t.setContentType("application/json",!1),function(e,t,n){if(I.isString(e))try{return(t||JSON.parse)(e),I.trim(e)}catch(e){if("SyntaxError"!==e.name)throw e}return(n||JSON.stringify)(e)}(e)):e}],transformResponse:[function(e){var t=this.transitional||ie.transitional,n=t&&t.forcedJSONParsing,r="json"===this.responseType;if(e&&I.isString(e)&&(n&&!this.responseType||r)){var o=!(t&&t.silentJSONParsing)&&r;try{return JSON.parse(e)}catch(e){if(o){if("SyntaxError"===e.name)throw q.from(e,q.ERR_BAD_RESPONSE,this,null,this.response);throw e}}}return e}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,maxBodyLength:-1,env:{FormData:ne.classes.FormData,Blob:ne.classes.Blob},validateStatus:function(e){return e>=200&&e<300},headers:{common:{Accept:"application/json, text/plain, */*"}}};I.forEach(["delete","get","head"],(function(e){ie.headers[e]={}})),I.forEach(["post","put","patch"],(function(e){ie.headers[e]=I.merge(oe)}));var ae=ie,se=I.toObjectSet(["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"]),ue=Symbol("internals");function ce(e){return e&&String(e).trim().toLowerCase()}function fe(e){return!1===e||null==e?e:I.isArray(e)?e.map(fe):String(e)}function le(e,t,n,r,o){return I.isFunction(r)?r.call(this,t,n):(o&&(t=n),I.isString(t)?I.isString(r)?-1!==t.indexOf(r):I.isRegExp(r)?r.test(t):void 0:void 0)}var de=function(e,n){function i(e){t(this,i),e&&this.set(e)}return r(i,[{key:"set",value:function(e,t,n){var r=this;function o(e,t,n){var o=ce(t);if(!o)throw new Error("header name must be a non-empty string");var i=I.findKey(r,o);(!i||void 0===r[i]||!0===n||void 0===n&&!1!==r[i])&&(r[i||t]=fe(e))}var i,a,s,u,c,f=function(e,t){return I.forEach(e,(function(e,n){return o(e,n,t)}))};return I.isPlainObject(e)||e instanceof this.constructor?f(e,t):I.isString(e)&&(e=e.trim())&&!/^[-_a-zA-Z0-9^`|~,!#$%&'*+.]+$/.test(e.trim())?f((c={},(i=e)&&i.split("\n").forEach((function(e){u=e.indexOf(":"),a=e.substring(0,u).trim().toLowerCase(),s=e.substring(u+1).trim(),!a||c[a]&&se[a]||("set-cookie"===a?c[a]?c[a].push(s):c[a]=[s]:c[a]=c[a]?c[a]+", "+s:s)})),c),t):null!=e&&o(t,e,n),this}},{key:"get",value:function(e,t){if(e=ce(e)){var n=I.findKey(this,e);if(n){var r=this[n];if(!t)return r;if(!0===t)return function(e){for(var t,n=Object.create(null),r=/([^\s,;=]+)\s*(?:=\s*([^,;]+))?/g;t=r.exec(e);)n[t[1]]=t[2];return n}(r);if(I.isFunction(t))return t.call(this,r,n);if(I.isRegExp(t))return t.exec(r);throw new TypeError("parser must be boolean|regexp|function")}}}},{key:"has",value:function(e,t){if(e=ce(e)){var n=I.findKey(this,e);return!(!n||void 0===this[n]||t&&!le(0,this[n],n,t))}return!1}},{key:"delete",value:function(e,t){var n=this,r=!1;function o(e){if(e=ce(e)){var o=I.findKey(n,e);!o||t&&!le(0,n[o],o,t)||(delete n[o],r=!0)}}return I.isArray(e)?e.forEach(o):o(e),r}},{key:"clear",value:function(e){for(var t=Object.keys(this),n=t.length,r=!1;n--;){var o=t[n];e&&!le(0,this[o],o,e,!0)||(delete this[o],r=!0)}return r}},{key:"normalize",value:function(e){var t=this,n={};return I.forEach(this,(function(r,o){var i=I.findKey(n,o);if(i)return t[i]=fe(r),void delete t[o];var a=e?function(e){return e.trim().toLowerCase().replace(/([a-z\d])(\w*)/g,(function(e,t,n){return t.toUpperCase()+n}))}(o):String(o).trim();a!==o&&delete t[o],t[a]=fe(r),n[a]=!0})),this}},{key:"concat",value:function(){for(var e,t=arguments.length,n=new Array(t),r=0;r<t;r++)n[r]=arguments[r];return(e=this.constructor).concat.apply(e,[this].concat(n))}},{key:"toJSON",value:function(e){var t=Object.create(null);return I.forEach(this,(function(n,r){null!=n&&!1!==n&&(t[r]=e&&I.isArray(n)?n.join(", "):n)})),t}},{key:Symbol.iterator,value:function(){return Object.entries(this.toJSON())[Symbol.iterator]()}},{key:"toString",value:function(){return Object.entries(this.toJSON()).map((function(e){var t=o(e,2);return t[0]+": "+t[1]})).join("\n")}},{key:Symbol.toStringTag,get:function(){return"AxiosHeaders"}}],[{key:"from",value:function(e){return e instanceof this?e:new this(e)}},{key:"concat",value:function(e){for(var t=new this(e),n=arguments.length,r=new Array(n>1?n-1:0),o=1;o<n;o++)r[o-1]=arguments[o];return r.forEach((function(e){return t.set(e)})),t}},{key:"accessor",value:function(e){var t=(this[ue]=this[ue]={accessors:{}}).accessors,n=this.prototype;function r(e){var r=ce(e);t[r]||(!function(e,t){var n=I.toCamelCase(" "+t);["get","set","has"].forEach((function(r){Object.defineProperty(e,r+n,{value:function(e,n,o){return this[r].call(this,t,e,n,o)},configurable:!0})}))}(n,e),t[r]=!0)}return I.isArray(e)?e.forEach(r):r(e),this}}]),i}();de.accessor(["Content-Type","Content-Length","Accept","Accept-Encoding","User-Agent","Authorization"]),I.freezeMethods(de.prototype),I.freezeMethods(de);var pe=de;function he(e,t){var n=this||ae,r=t||n,o=pe.from(r.headers),i=r.data;return I.forEach(e,(function(e){i=e.call(n,i,o.normalize(),t?t.status:void 0)})),o.normalize(),i}function me(e){return!(!e||!e.__CANCEL__)}function ye(e,t,n){q.call(this,null==e?"canceled":e,q.ERR_CANCELED,t,n),this.name="CanceledError"}I.inherits(ye,q,{__CANCEL__:!0});var ve=ne.isStandardBrowserEnv?{write:function(e,t,n,r,o,i){var a=[];a.push(e+"="+encodeURIComponent(t)),I.isNumber(n)&&a.push("expires="+new Date(n).toGMTString()),I.isString(r)&&a.push("path="+r),I.isString(o)&&a.push("domain="+o),!0===i&&a.push("secure"),document.cookie=a.join("; ")},read:function(e){var t=document.cookie.match(new RegExp("(^|;\\s*)("+e+")=([^;]*)"));return t?decodeURIComponent(t[3]):null},remove:function(e){this.write(e,"",Date.now()-864e5)}}:{write:function(){},read:function(){return null},remove:function(){}};function be(e,t){return e&&!/^([a-z][a-z\d+\-.]*:)?\/\//i.test(t)?function(e,t){return t?e.replace(/\/+$/,"")+"/"+t.replace(/^\/+/,""):e}(e,t):t}var ge=ne.isStandardBrowserEnv?function(){var e,t=/(msie|trident)/i.test(navigator.userAgent),n=document.createElement("a");function r(e){var r=e;return t&&(n.setAttribute("href",r),r=n.href),n.setAttribute("href",r),{href:n.href,protocol:n.protocol?n.protocol.replace(/:$/,""):"",host:n.host,search:n.search?n.search.replace(/^\?/,""):"",hash:n.hash?n.hash.replace(/^#/,""):"",hostname:n.hostname,port:n.port,pathname:"/"===n.pathname.charAt(0)?n.pathname:"/"+n.pathname}}return e=r(window.location.href),function(t){var n=I.isString(t)?r(t):t;return n.protocol===e.protocol&&n.host===e.host}}():function(){return!0};function we(e,t){var n=0,r=function(e,t){e=e||10;var n,r=new Array(e),o=new Array(e),i=0,a=0;return t=void 0!==t?t:1e3,function(s){var u=Date.now(),c=o[a];n||(n=u),r[i]=s,o[i]=u;for(var f=a,l=0;f!==i;)l+=r[f++],f%=e;if((i=(i+1)%e)===a&&(a=(a+1)%e),!(u-n<t)){var d=c&&u-c;return d?Math.round(1e3*l/d):void 0}}}(50,250);return function(o){var i=o.loaded,a=o.lengthComputable?o.total:void 0,s=i-n,u=r(s);n=i;var c={loaded:i,total:a,progress:a?i/a:void 0,bytes:s,rate:u||void 0,estimated:u&&a&&i<=a?(a-i)/u:void 0,event:o};c[t?"download":"upload"]=!0,e(c)}}var Ee={http:null,xhr:"undefined"!=typeof XMLHttpRequest&&function(e){return new Promise((function(t,n){var r,o=e.data,i=pe.from(e.headers).normalize(),a=e.responseType;function s(){e.cancelToken&&e.cancelToken.unsubscribe(r),e.signal&&e.signal.removeEventListener("abort",r)}I.isFormData(o)&&(ne.isStandardBrowserEnv||ne.isStandardBrowserWebWorkerEnv)&&i.setContentType(!1);var u=new XMLHttpRequest;if(e.auth){var c=e.auth.username||"",f=e.auth.password?unescape(encodeURIComponent(e.auth.password)):"";i.set("Authorization","Basic "+btoa(c+":"+f))}var l=be(e.baseURL,e.url);function d(){if(u){var r=pe.from("getAllResponseHeaders"in u&&u.getAllResponseHeaders());!function(e,t,n){var r=n.config.validateStatus;n.status&&r&&!r(n.status)?t(new q("Request failed with status code "+n.status,[q.ERR_BAD_REQUEST,q.ERR_BAD_RESPONSE][Math.floor(n.status/100)-4],n.config,n.request,n)):e(n)}((function(e){t(e),s()}),(function(e){n(e),s()}),{data:a&&"text"!==a&&"json"!==a?u.response:u.responseText,status:u.status,statusText:u.statusText,headers:r,config:e,request:u}),u=null}}if(u.open(e.method.toUpperCase(),Z(l,e.params,e.paramsSerializer),!0),u.timeout=e.timeout,"onloadend"in u?u.onloadend=d:u.onreadystatechange=function(){u&&4===u.readyState&&(0!==u.status||u.responseURL&&0===u.responseURL.indexOf("file:"))&&setTimeout(d)},u.onabort=function(){u&&(n(new q("Request aborted",q.ECONNABORTED,e,u)),u=null)},u.onerror=function(){n(new q("Network Error",q.ERR_NETWORK,e,u)),u=null},u.ontimeout=function(){var t=e.timeout?"timeout of "+e.timeout+"ms exceeded":"timeout exceeded",r=e.transitional||te;e.timeoutErrorMessage&&(t=e.timeoutErrorMessage),n(new q(t,r.clarifyTimeoutError?q.ETIMEDOUT:q.ECONNABORTED,e,u)),u=null},ne.isStandardBrowserEnv){var p=(e.withCredentials||ge(l))&&e.xsrfCookieName&&ve.read(e.xsrfCookieName);p&&i.set(e.xsrfHeaderName,p)}void 0===o&&i.setContentType(null),"setRequestHeader"in u&&I.forEach(i.toJSON(),(function(e,t){u.setRequestHeader(t,e)})),I.isUndefined(e.withCredentials)||(u.withCredentials=!!e.withCredentials),a&&"json"!==a&&(u.responseType=e.responseType),"function"==typeof e.onDownloadProgress&&u.addEventListener("progress",we(e.onDownloadProgress,!0)),"function"==typeof e.onUploadProgress&&u.upload&&u.upload.addEventListener("progress",we(e.onUploadProgress)),(e.cancelToken||e.signal)&&(r=function(t){u&&(n(!t||t.type?new ye(null,e,u):t),u.abort(),u=null)},e.cancelToken&&e.cancelToken.subscribe(r),e.signal&&(e.signal.aborted?r():e.signal.addEventListener("abort",r)));var h,m=(h=/^([-+\w]{1,25})(:?\/\/|:)/.exec(l))&&h[1]||"";m&&-1===ne.protocols.indexOf(m)?n(new q("Unsupported protocol "+m+":",q.ERR_BAD_REQUEST,e)):u.send(o||null)}))}};I.forEach(Ee,(function(e,t){if(e){try{Object.defineProperty(e,"name",{value:t})}catch(e){}Object.defineProperty(e,"adapterName",{value:t})}}));var Oe=function(e){for(var t,n,r=(e=I.isArray(e)?e:[e]).length,o=0;o<r&&(t=e[o],!(n=I.isString(t)?Ee[t.toLowerCase()]:t));o++);if(!n){if(!1===n)throw new q("Adapter ".concat(t," is not supported by the environment"),"ERR_NOT_SUPPORT");throw new Error(I.hasOwnProp(Ee,t)?"Adapter '".concat(t,"' is not available in the build"):"Unknown adapter '".concat(t,"'"))}if(!I.isFunction(n))throw new TypeError("adapter is not a function");return n};function Se(e){if(e.cancelToken&&e.cancelToken.throwIfRequested(),e.signal&&e.signal.aborted)throw new ye(null,e)}function Re(e){return Se(e),e.headers=pe.from(e.headers),e.data=he.call(e,e.transformRequest),-1!==["post","put","patch"].indexOf(e.method)&&e.headers.setContentType("application/x-www-form-urlencoded",!1),Oe(e.adapter||ae.adapter)(e).then((function(t){return Se(e),t.data=he.call(e,e.transformResponse,t),t.headers=pe.from(t.headers),t}),(function(t){return me(t)||(Se(e),t&&t.response&&(t.response.data=he.call(e,e.transformResponse,t.response),t.response.headers=pe.from(t.response.headers))),Promise.reject(t)}))}var Ae=function(e){return e instanceof pe?e.toJSON():e};function Te(e,t){t=t||{};var n={};function r(e,t,n){return I.isPlainObject(e)&&I.isPlainObject(t)?I.merge.call({caseless:n},e,t):I.isPlainObject(t)?I.merge({},t):I.isArray(t)?t.slice():t}function o(e,t,n){return I.isUndefined(t)?I.isUndefined(e)?void 0:r(void 0,e,n):r(e,t,n)}function i(e,t){if(!I.isUndefined(t))return r(void 0,t)}function a(e,t){return I.isUndefined(t)?I.isUndefined(e)?void 0:r(void 0,e):r(void 0,t)}function s(n,o,i){return i in t?r(n,o):i in e?r(void 0,n):void 0}var u={url:i,method:i,data:i,baseURL:a,transformRequest:a,transformResponse:a,paramsSerializer:a,timeout:a,timeoutMessage:a,withCredentials:a,adapter:a,responseType:a,xsrfCookieName:a,xsrfHeaderName:a,onUploadProgress:a,onDownloadProgress:a,decompress:a,maxContentLength:a,maxBodyLength:a,beforeRedirect:a,transport:a,httpAgent:a,httpsAgent:a,cancelToken:a,socketPath:a,responseEncoding:a,validateStatus:s,headers:function(e,t){return o(Ae(e),Ae(t),!0)}};return I.forEach(Object.keys(e).concat(Object.keys(t)),(function(r){var i=u[r]||o,a=i(e[r],t[r],r);I.isUndefined(a)&&i!==s||(n[r]=a)})),n}var je="1.3.6",Ne={};["object","boolean","number","function","string","symbol"].forEach((function(t,n){Ne[t]=function(r){return e(r)===t||"a"+(n<1?"n ":" ")+t}}));var xe={};Ne.transitional=function(e,t,n){function r(e,t){return"[Axios v1.3.6] Transitional option '"+e+"'"+t+(n?". "+n:"")}return function(n,o,i){if(!1===e)throw new q(r(o," has been removed"+(t?" in "+t:"")),q.ERR_DEPRECATED);return t&&!xe[o]&&(xe[o]=!0,console.warn(r(o," has been deprecated since v"+t+" and will be removed in the near future"))),!e||e(n,o,i)}};var Ce={assertOptions:function(t,n,r){if("object"!==e(t))throw new q("options must be an object",q.ERR_BAD_OPTION_VALUE);for(var o=Object.keys(t),i=o.length;i-- >0;){var a=o[i],s=n[a];if(s){var u=t[a],c=void 0===u||s(u,a,t);if(!0!==c)throw new q("option "+a+" must be "+c,q.ERR_BAD_OPTION_VALUE)}else if(!0!==r)throw new q("Unknown option "+a,q.ERR_BAD_OPTION)}},validators:Ne},Pe=Ce.validators,ke=function(){function e(n){t(this,e),this.defaults=n,this.interceptors={request:new ee,response:new ee}}return r(e,[{key:"request",value:function(e,t){"string"==typeof e?(t=t||{}).url=e:t=e||{};var n,r=t=Te(this.defaults,t),o=r.transitional,i=r.paramsSerializer,a=r.headers;void 0!==o&&Ce.assertOptions(o,{silentJSONParsing:Pe.transitional(Pe.boolean),forcedJSONParsing:Pe.transitional(Pe.boolean),clarifyTimeoutError:Pe.transitional(Pe.boolean)},!1),null!=i&&(I.isFunction(i)?t.paramsSerializer={serialize:i}:Ce.assertOptions(i,{encode:Pe.function,serialize:Pe.function},!0)),t.method=(t.method||this.defaults.method||"get").toLowerCase(),(n=a&&I.merge(a.common,a[t.method]))&&I.forEach(["delete","get","head","post","put","patch","common"],(function(e){delete a[e]})),t.headers=pe.concat(n,a);var s=[],u=!0;this.interceptors.request.forEach((function(e){"function"==typeof e.runWhen&&!1===e.runWhen(t)||(u=u&&e.synchronous,s.unshift(e.fulfilled,e.rejected))}));var c,f=[];this.interceptors.response.forEach((function(e){f.push(e.fulfilled,e.rejected)}));var l,d=0;if(!u){var p=[Re.bind(this),void 0];for(p.unshift.apply(p,s),p.push.apply(p,f),l=p.length,c=Promise.resolve(t);d<l;)c=c.then(p[d++],p[d++]);return c}l=s.length;var h=t;for(d=0;d<l;){var m=s[d++],y=s[d++];try{h=m(h)}catch(e){y.call(this,e);break}}try{c=Re.call(this,h)}catch(e){return Promise.reject(e)}for(d=0,l=f.length;d<l;)c=c.then(f[d++],f[d++]);return c}},{key:"getUri",value:function(e){return Z(be((e=Te(this.defaults,e)).baseURL,e.url),e.params,e.paramsSerializer)}}]),e}();I.forEach(["delete","get","head","options"],(function(e){ke.prototype[e]=function(t,n){return this.request(Te(n||{},{method:e,url:t,data:(n||{}).data}))}})),I.forEach(["post","put","patch"],(function(e){function t(t){return function(n,r,o){return this.request(Te(o||{},{method:e,headers:t?{"Content-Type":"multipart/form-data"}:{},url:n,data:r}))}}ke.prototype[e]=t(),ke.prototype[e+"Form"]=t(!0)}));var Ue=ke,_e=function(){function e(n){if(t(this,e),"function"!=typeof n)throw new TypeError("executor must be a function.");var r;this.promise=new Promise((function(e){r=e}));var o=this;this.promise.then((function(e){if(o._listeners){for(var t=o._listeners.length;t-- >0;)o._listeners[t](e);o._listeners=null}})),this.promise.then=function(e){var t,n=new Promise((function(e){o.subscribe(e),t=e})).then(e);return n.cancel=function(){o.unsubscribe(t)},n},n((function(e,t,n){o.reason||(o.reason=new ye(e,t,n),r(o.reason))}))}return r(e,[{key:"throwIfRequested",value:function(){if(this.reason)throw this.reason}},{key:"subscribe",value:function(e){this.reason?e(this.reason):this._listeners?this._listeners.push(e):this._listeners=[e]}},{key:"unsubscribe",value:function(e){if(this._listeners){var t=this._listeners.indexOf(e);-1!==t&&this._listeners.splice(t,1)}}}],[{key:"source",value:function(){var t;return{token:new e((function(e){t=e})),cancel:t}}}]),e}();var Fe={Continue:100,SwitchingProtocols:101,Processing:102,EarlyHints:103,Ok:200,Created:201,Accepted:202,NonAuthoritativeInformation:203,NoContent:204,ResetContent:205,PartialContent:206,MultiStatus:207,AlreadyReported:208,ImUsed:226,MultipleChoices:300,MovedPermanently:301,Found:302,SeeOther:303,NotModified:304,UseProxy:305,Unused:306,TemporaryRedirect:307,PermanentRedirect:308,BadRequest:400,Unauthorized:401,PaymentRequired:402,Forbidden:403,NotFound:404,MethodNotAllowed:405,NotAcceptable:406,ProxyAuthenticationRequired:407,RequestTimeout:408,Conflict:409,Gone:410,LengthRequired:411,PreconditionFailed:412,PayloadTooLarge:413,UriTooLong:414,UnsupportedMediaType:415,RangeNotSatisfiable:416,ExpectationFailed:417,ImATeapot:418,MisdirectedRequest:421,UnprocessableEntity:422,Locked:423,FailedDependency:424,TooEarly:425,UpgradeRequired:426,PreconditionRequired:428,TooManyRequests:429,RequestHeaderFieldsTooLarge:431,UnavailableForLegalReasons:451,InternalServerError:500,NotImplemented:501,BadGateway:502,ServiceUnavailable:503,GatewayTimeout:504,HttpVersionNotSupported:505,VariantAlsoNegotiates:506,InsufficientStorage:507,LoopDetected:508,NotExtended:510,NetworkAuthenticationRequired:511};Object.entries(Fe).forEach((function(e){var t=o(e,2),n=t[0],r=t[1];Fe[r]=n}));var Be=Fe;var Le=function e(t){var n=new Ue(t),r=a(Ue.prototype.request,n);return I.extend(r,Ue.prototype,n,{allOwnKeys:!0}),I.extend(r,n,null,{allOwnKeys:!0}),r.create=function(n){return e(Te(t,n))},r}(ae);return Le.Axios=Ue,Le.CanceledError=ye,Le.CancelToken=_e,Le.isCancel=me,Le.VERSION=je,Le.toFormData=V,Le.AxiosError=q,Le.Cancel=Le.CanceledError,Le.all=function(e){return Promise.all(e)},Le.spread=function(e){return function(t){return e.apply(null,t)}},Le.isAxiosError=function(e){return I.isObject(e)&&!0===e.isAxiosError},Le.mergeConfig=Te,Le.AxiosHeaders=pe,Le.formToJSON=function(e){return re(I.isHTMLForm(e)?new FormData(e):e)},Le.HttpStatusCode=Be,Le.default=Le,Le}));
//# sourceMappingURL=axios.min.js.map

```

### js/header.js

```
function sendEmailVCode(){
	// 获取邮箱
	var targetEmail = document.querySelector("#reg-username").value;
	// 获取到发送按钮
	var sendEmailButton = document.querySelector("#send-email-vcode");
	
	// 也可以进行邮箱格式的验证
	if (!targetEmail.match(".+@.+\..+")){
		alert("邮箱格式错误");
		document.querySelector("#reg-username").focus();
		return false;
	}
	
	// 比对两次密码是否一致
	var firstPassword = document.querySelector("#reg-password").value;
	var secondPassword = document.querySelector("#reg-password1").value;
	if(firstPassword != secondPassword){
		alert("两次输入的密码不一致")
		document.querySelector("#reg-password").focus();
		return false;
	}
	// 发送邮箱验证码
	console.log(targetEmail);
	axios.post("/ecode",{
		email:targetEmail
	}).then((res)=>{
		console.log(res);
		alert("向后端发送验证码成功");
		// 设置倒计时 一般是60秒
		times=5;
		countDown(sendEmailButton,times);
		
	})
}

function countDown(sendEmailButton,times){
	sendEmailButton.disabled=true;
	sendEmailButton.innerHTML=times;
	if(times > 0){
		times = times-1;
		setTimeout(function(){
			countDown(sendEmailButton,times)
		},1000)
	}else{
		// 到了0秒了，那么一切还原
		sendEmailButton.disabled=false;
		sendEmailButton.innerHTML="发送";
	}
	
}

//  用户注册实现
function userReg(){
	// 获取邮箱
	var targetEmail = document.querySelector("#reg-username").value;
	
	// 也可以进行邮箱格式的验证
	if (!targetEmail.match(".+@.+\..+")){
		alert("邮箱格式错误");
		document.querySelector("#reg-username").focus();
		return false;
	}
	
	// 比对两次密码是否一致
	var firstPassword = document.querySelector("#reg-password").value;
	var secondPassword = document.querySelector("#reg-password1").value;
	if(firstPassword != secondPassword){
		alert("两次输入的密码不一致")
		document.querySelector("#reg-password").focus();
		return false;
	}
	
	//  开始执行用户注册
	// 获取用户输入的验证码
	var emailVCode = document.querySelector("#email-vcode").value;
	
	axios.post("/reg",{
		username:targetEmail,
		password:firstPassword,
		second_password:secondPassword,
		ecode:emailVCode
	}).then((res)=>{
		// res.data就是后端返回json
		// console.log(res.data)
		if(res.data.status==1000){
			alert(res.data.data);
			// 注册成功后要做做一个页面跳转，转到首页
			location.href="/"
		}else{
			alert(res.data.data);
		}
	})
	
	
}


// 登录功能实现
function doLogin(){
	var username = document.querySelector("#username").value;
	var password = document.querySelector("#password").value;
	var authCode = document.querySelector("#auth-code").value;
	axios.post("/login",{
		username:username,
		password:password,
		vcode:authCode
	}).then((res)=>{
		if(res.data.status==1000){
			alert(res.data.data);
			setTimeout("location.reload()",1000);
		}else{
			alert(res.data.data);
		}
	})
	
}
```

### js/index.js

```
console.log("index.js文件引入了");

//  锁定后端数据请求中的状态。 是否允许请求后端
var allowRequest=true;
var page=1;
//  但是这种翻页的写法会有兼容性问题

function getUrlParams(){
	// ?page=2&article_type=recommend
	var uri = location.search;
	var final_result = {};
	// 第一次请求没有参数的时候
	if(uri==""){
		final_result['page']=page;
		final_result['article_type']='recommend';
		final_result['start_num']=0;
		final_result['end_num']=10;
	}else {  // 有参数的时候
		if(uri.indexOf("?")!=-1){
			params = uri.substr(1);
			//  page=2&article_type=recommend
			param_list = params.split("&");
			// [page=2,article_type=recommend]
			for(var i=0;i<param_list.length;i++){
				var key = param_list[i].split("=")[0];
				var value= param_list[i].split("=")[1];
				final_result[key] = value;
			}
			
		}
		if(uri.includes("keyword") && !uri.includes("page")){
			final_result["page"]=1;
			final_result['start_num']=0;
			final_result['end_num']=10;
		}
		
	}
	
	return final_result;
}

// 锁 锁定后端数据请求状态，是否允许请求后端
function toNextPage(params){
	console.log(params);
	// 拼接url的过程
	var url="?";
	for(var key in params){
		if(key=="page"){
			params[key]=parseInt(params[key])+1;
		}
		if(key=="start_num"){
			params[key] = window.endNum;
		}
		//  page=2&article_type=recommend
		url += key
		url += "="
		url += params[key]
		url += "&"
	}
	if(!url.includes("scroll")){
		url += "scroll=1";
	}
	// 去掉url地址最后的&符号
	if(url.endsWith("&")){
		url = url.substr(0,url.length-1)
	}

	
	console.log(url);
	console.log("后端数据请求完毕，同时页面渲染完毕，打开请求锁");
	allowRequest=true;
	
	location.href=url;
}

function windowScroll(){
	if(window.startNum===window.endNum){
		document.querySelector(".load-more").innerHTML="没有更多数据了";
		return
	}
	// // 可视区域的高度，就是我们能看见的内容的高度
	// console.log(document.documentElement.clientHeight);
	// // 滚动条在文档中的高度的位置（滚出可见区域的高度）
	// console.log(document.documentElement.scrollTop);
	// // 所有内容的高度
	// console.log(document.body.scrollHeight);
	var clientHeight =document.documentElement.clientHeight;
	var scrollTop=document.documentElement.scrollTop;
	var scrollHeight=document.body.scrollHeight;
	if(clientHeight+scrollTop >= scrollHeight && allowRequest){
		console.log("开始向后端请求数据，重新渲染页面");
		allowRequest=false;
		//  获取url中的参数
		var params = getUrlParams();
		toNextPage(params);
	}
}

window.addEventListener("scroll",windowScroll);

```

### js/new-article.js

```
var ue = UE.getEditor('editor', {
		        // ... 更多配置
				shortcutMenu: false,
				elementPathEnabled : false,
				wordCount:false,
				autoHeightEnabled:false,
				// 初始化编辑器宽度,默认 1000
				initialFrameWidth:800,
				// 初始化编辑器高度,默认 320
				initialFrameHeight:800,
				serverUrl:"http://127.0.0.1:5000/feedback",
				toolbars: [
				  [
					   "insertcode",  
					    "bold",         // 加粗
					    "italic",       // 斜体
					    "insertimage",  
						"link",
					    "insertorderedlist",   // 有序列表
					    "insertunorderedlist", // 无序列表
					    "undo",         // 撤销
					    "redo",         // 重做
					    "emotion",             // 表情
				  ]
					  ]
		    });
			
			
// 控制投递的栏目菜单栏的显示与隐藏
var isArticleLabelListShow=true;

function showArticleLabelList(){
	var labelList = document.querySelector(".article-label-list");
	var labelValue = document.querySelector(".article-label-value");
	if(isArticleLabelListShow==true){
		labelList.style.display="block";
		isArticleLabelListShow=false;
		labelValue.style.boxShadow="0 0 0 4px rgb(28 31 33 / 10%)";
	}else{
		labelList.style.display="none";
		isArticleLabelListShow=true;
		labelValue.style.boxShadow="";
	}
}

var isArticleTypeListShow=true;
function showArticleTypeList(){
	var typeList = document.querySelector(".article-type-list");
	var typeValue = document.querySelector(".article-type-value");
	if(isArticleTypeListShow==true){
		typeList.style.display="block";
		isArticleTypeListShow=false;
		typeValue.style.boxShadow="0 0 0 4px rgb(28 31 33 / 10%)";
	}else{
		typeList.style.display="none";
		isArticleTypeListShow=true;
		typeValue.style.boxShadow="";
	}
}
var isDraftedListShow=true;
function showDraftedList(){
	var draftedList = document.querySelector(".drafted-info");
	if(isDraftedListShow==true){
		draftedList.style.display="block";
		isDraftedListShow=false;
	}else{
		draftedList.style.display="none";
		isDraftedListShow=true;
	}
}


// 声明存储文章内容的变量
var articleContent;
var articleTitle;
var articleId=-1;
// 选择投递的栏目
var label_name=""
var article_type=""
// 创建文章或者是文章的草稿存储
function createArticle(drafted){
	//  获取文章的标题
	articleTitle = document.querySelector(".article-header").value;
	// 获取文章的内容
	articleContent = ue.getContent();
	
	// 向后端发送请求
	axios.post("/article/save",{
		// 这是草稿存储的逻辑
		title:articleTitle,
		article_content:articleContent,
		article_id:articleId,
		drafted:drafted,
		// 下边的几个字段是正式发布的时候才用
		label_name:label_name,
		article_type:article_type,
		article_tag:articleTag
	}).then((res)=>{
		articleId = res.data.article_id
		alert(res.data.data)
		// 如果是文章发布的逻辑，那么我们需要默认跳转到文章详情页面
		if(drafted==1){
			setTimeout(function(){
				location.href="/detail?article_id="+articleId;
			},1000);
		}
	})
}

// 添加事件监听，上传文章头部图片
// 是页面加载完毕后立即执行。要不然就会报找不到addEnevtListener的错误
window.onload=function(){
	var articleHeaderImage = document.querySelector("#xFile");
	articleHeaderImage.addEventListener("change",function(event){
		// 拿到用户上传的图片
		var articleHeaderImageFile = event.target.files[0];
		// 构造请求的参数
		var formData = new FormData();
		// 添加一个上传文件的key，要和后台接收的key相同，后台要用到这个key然后获取到接收的文件
		formData.append("header-image-file",articleHeaderImageFile);
		formData.append("article_id",articleId);
		// 把数据提交给后台
		axios.post("/article/upload/article_header_image",formData).then((res)=>{
			var image = document.querySelector(".upload-header-image label img");
			image.setAttribute("src",res.data.url)
			image.style.width="130px";
			image.style.height="130px";
		})
		
	})
}
//  文章头图随机图片
function randomHeaderImage(){
	var formData = new FormData();
	formData.append("article_id",articleId);
	// 把数据提交给后台
	axios.post("/article/random/header/image",formData).then((res)=>{
		var image = document.querySelector(".upload-header-image label img");
		image.setAttribute("src",res.data.url)
		image.style.width="130px";
		image.style.height="130px";
	})
}

// 选择投递的栏目
function selectLabelName(label_name_args,label_value_args){
	label_name = label_name_args;
	var firstChildSpan = document.querySelector(".article-label-value>span:first-child");
	firstChildSpan.innerHTML = label_value_args;
	var lis = document.querySelectorAll(".article-label-list>div>li");
	// 注意这里的for循环，如果我们使用了in那么就会多遍历出来一些属性，因为in会把lis当成对象来遍历
	// 那么就把其它属性也循环出来了
	for(i of lis.keys()){
		// console.log(i);
		lis[i].className="no-selected";
		if(lis[i].getAttribute("data-label-type") == label_name_args){
			lis[i].className="selected";
		}
	}
	
}

// 选择文章的类型
function selectArticleType(article_type_name_args,article_type_value_args){
	article_type = article_type_name_args;
	var firstChildSpan = document.querySelector(".article-type-value>span:first-child");
	firstChildSpan.innerHTML = article_type_value_args;
	var lis = document.querySelectorAll(".article-type-list>div>li");
	// 注意这里的for循环，如果我们使用了in那么就会多遍历出来一些属性，因为in会把lis当成对象来遍历
	// 那么就把其它属性也循环出来了
	for(i of lis.keys()){
		// console.log(i);
		lis[i].className="no-selected";
		if(lis[i].getAttribute("data-article-type") == article_type_name_args){
			lis[i].className="selected";
		}
	}
}

// 添加文章标签
var articleTag=""; //这个就是存储到数据库里的样子
var finalTagsList=[]; //这个是用来做中间转换用的
var tagNum=0;
function addTag(tagName){
	if(finalTagsList.length==3){
		return false;
	}
	// 我们需要定位到change-tags，给它添加子元素
	var changeTags = document.querySelector(".change-tags");
	var childElement = "span";
	var mySpanTag = document.createElement(childElement);
	// <span>Python</span>
	mySpanTag.innerHTML=tagName;
	mySpanTag.setAttribute("data-tag",tagName);
	mySpanTag.addEventListener("click",deleteTag);
	finalTagsList.push(tagName);
	articleTag = finalTagsList.join(",");
	changeTags.appendChild(mySpanTag);
	// 如果标签数量等于了3个，那么就删除掉input标签
	if(finalTagsList.length==3){
		var tagInputElement = document.querySelector(".article-tag-value>input");
		document.querySelector(".article-tag-value").removeChild(tagInputElement)
	}
	// 修改前端标签的数量显示
	document.querySelector(".tag-num").innerHTML=finalTagsList.length;
}


function deleteTag(){
	var changeTags = document.querySelector(".change-tags");
	var changeSonTags = document.querySelectorAll(".change-tags>span");
	for(var i of changeSonTags.keys()){
		if(changeSonTags[i].getAttribute("data-tag")==this.innerHTML){
			changeTags.removeChild(changeSonTags[i]);
		}
		// 删除完之后，我们需要对数组中的元素进行删除，然后再改变最终的字符串
		for(i in finalTagsList){
			if(finalTagsList[i]==this.innerHTML){
				finalTagsList.splice(i,1);
				articleTag=finalTagsList.join(",");
			}
		}
	}
	/* 如果长度小于3，我们需要判断孩子里边有没有input标签，如果没有，那么就添加 */
	//  <input class="fl" type="text" placeholder="选择下列标签">
	var tagInputElement = document.querySelector(".article-tag-value>input");
	if(tagInputElement==null){
		var articleTagValue=document.querySelector(".article-tag-value");
		tagInputElement = document.createElement("input");
		tagInputElement.className = "fl";
		tagInputElement.type="text";
		tagInputElement.setAttribute("placeholder","选择下列标签")
		articleTagValue.appendChild(tagInputElement);
		// 手动绑定一下input监听事件
		addInputEventListenerFunc();
	}
	
	// 修改前端的标签数量
	document.querySelector(".tag-num").innerHTML=finalTagsList.length;
	
}

// 修复一下input标签删除后，再重建没有监听input事件的bug
var addInputEventListenerFunc;

window.onload=function(){
	function addInputEventListener(){
		var article_tags = window.globalArticleTags;
		console.log(article_tags);
		var inputElement = document.querySelector(".article-tag-value>input");
		inputElement.addEventListener("input",function(event){
			var resetArticleTagList=[];
			var tag_value = inputElement.value;
			console.log(tag_value);
			// 动态渲染，重新筛选标签
			for(var i in article_tags){
				if(article_tags[i].search(tag_value)!=-1){
					resetArticleTagList.push(article_tags[i]);
				}
			}
			/* 再次渲染页面 */
			var articleTagListElement = document.querySelector(".article-tag-list");
			// 先删除掉所有的孩子，然后再用新的列表内容进行标签渲染
			articleTagListElement.innerHTML="";
			// <span onclick="addTag('{{article_tag}}')">{{article_tag}}</span>
			for(var i in resetArticleTagList){
				var element = document.createElement("span");
				element.setAttribute("onclick","addTag('"+resetArticleTagList[i]+"')")
				element.innerHTML=resetArticleTagList[i];
				articleTagListElement.appendChild(element);
			}
		})
	}
	addInputEventListenerFunc = addInputEventListener;
	addInputEventListenerFunc();
}

// 在ue中显示我的草稿内容
function toDrafted(draftedId){
	/* 一个是把title的值给放上去 */
	var articleHeader = document.querySelector(".article-header");
	
	// 把article_contetn的内容放上去
	axios.post("/article/drafted",{
		id:draftedId
	}).then((res)=>{
		articleHeader.value = res.data.data.title;
		ue.body.innerHTML=res.data.data.article_content;
		// 千万不要忘记我们此时编辑的是哪个草稿
		articleId = res.data.data.id;
	})
	
}
```

### js/sub-header.js

```
function search_article(){
	var keyword = document.querySelector(".searchbox").value;
	// console.log(keyword);
	location.href="?keyword="+keyword;
}

function toWriteArticlePage(isLogin){
	console.log(isLogin);
	if(isLogin=='None' || isLogin!='true'){
		alert("您好，请登录");
		document.querySelector(".login>span:first-child").click();
	}else{
		window.open("/article/new","_blank")
	}
}
```



### 其他文件夹

font, images, plugins, upload文件夹省略

先用pytest对项目进行完整的单元测试、集成测试、系统测试和验收测试（使用conftest.py,pytest.in），
然后用selenium对关键位置，关键模块关键功能进行自动化测试
测试时，需要用到数据库时，要连接项目中的数据库，测试要规范化，达到企业级标准

tip:
这个注册页面需要注册邮箱的验证码，这个验证码由项目随机生成，发送到用户注册的邮箱中，而不是由用户来决定的，所以在测试用户注册时，需要考虑这一点