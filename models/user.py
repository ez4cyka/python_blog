
from datetime import datetime

from flask_login import UserMixin
from routes import db,login_manager
from sqlalchemy import Integer,String,BLOB,TIMESTAMP
from sqlalchemy.orm import Mapped,mapped_column

#定义一个函数告诉login_manager怎么查到用户
@login_manager.user_loader
def load_user(user_id):
    # return db.session.query(User).filter(User.id==user_id).first()
    return db.session.get(User,user_id)

#登录流程里需要用到一些特殊的方法，这些方法UserMixin里已经把额外方法实现了
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    username:Mapped[str] = mapped_column(String(128),unique=True,nullable=False)
    password:Mapped[str] = mapped_column(String(255),nullable=False)
    fullname:Mapped[str] = mapped_column(String(128),nullable=False)
    description:Mapped[str] = mapped_column(String(255),nullable=True)

    def check_password_correction(self,attempted_password):
        return self.password == attempted_password
    