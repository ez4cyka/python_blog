from flask_login import login_user
from sqlalchemy import Select
from routes import db
from models.user import User

class UserService:
    def do_login(self,username:str,password:str) ->bool:
        query = Select(User).where(User.username==username)
        attempted_user = db.session.scalar(query)
        if attempted_user and attempted_user.check_password_correction(password):
            #让flask_login 把当前用户放进session
            login_user(attempted_user)
            return True
        return False