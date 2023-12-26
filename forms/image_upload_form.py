from flask_wtf import FlaskForm
from wtforms import FileField, StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

#flask中的表单类
class ImageUploadForm(FlaskForm):
    image_file = FileField(label="选择图片:",validators = [DataRequired()])
    submit = SubmitField(label="上传")