from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

MYSQL_HOST = os.getenv("MYSQL_HOST","localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT","3306")
MYSQL_USER = os.getenv("MYSQL_USER","root")
MYSQL_PWD = os.getenv("MYSQL_PWD","123456")
MYSQL_DB = os.getenv("MYSQL_DB","myblog_db")




#设置模版目录，静态文件目录，静态文件读取路径
app = Flask(__name__,template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets')

#配置数据库连接参数
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
#配置flask_login 需要的SECRET_KEY
app.config['SECRET_KEY'] = "f295d972a332f48ff26594527e064e79"
db = SQLAlchemy(app)

login_manager = LoginManager(app)

from routes import user_routes
from routes import admin_routes