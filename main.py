from routes import app,db
from sqlalchemy import inspect
from models.user import User

def init_db():
    #在app创建之前执行的话需要用这种方法初始化数据库的表
    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table('users'):          
            db.create_all()
            user = User(username="root",password="123456",fullname="root user",description="root用户")
            db.session.add(user)
            db.session.commit()

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0',debug=True,port=10087)