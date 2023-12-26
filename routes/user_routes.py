#用户能访问的页面
from flask_login import logout_user
from common.profile import Profile
from forms.login_form import LoginForm
from forms.delete_article_form import DeleteArticleForm
from routes import app
import flask 
from services.article_service import ArticleService
from services.user_service import UserService
@app.route('/')
@app.route('/index.html')
def home_page():
    delete_article_form = DeleteArticleForm()
    articles = ArticleService().get_articles()
    #让模版渲染函数，把模版页面渲染出来返回给浏览器 ,变量可以通过关键字参数传入
    return flask.render_template("index.html",articles= articles,delete_article_form=delete_article_form)

@app.route('/about.html')
def about_page():
    return flask.render_template("about.html",my_title="About Page")

@app.route('/article/<article_id>.html')
def article_page(article_id):
    article = ArticleService().get_article_by_id(article_id)
    if article:
        return flask.render_template("article.html",article = article)
    #如果不存在就返回404
    flask.abort(404)

@app.route('/login.html',methods=['GET','POST'])
def login_page():
    #new一个form，如果内容不指定，直接会使用flask.request.form 和flask.request.file
    form = LoginForm()
    #validate_on_submit()只对 POST 有效
    if form.validate_on_submit():
        result = UserService().do_login(username=form.username.data,password=form.password.data)
        if result:
            #在缓存中增加一条消息
            flask.flash(f'欢迎{form.username.data}回来',category='success')
            return flask.redirect(flask.url_for('home_page'))
        else:
            flask.flash('用户名或密码错误,请重试！',category='danger')

    return flask.render_template("login.html",form = form)
@app.route('/logout.html')
def logout_page():
    logout_user()
    flask.flash(f'已登出',category='warning')
    return flask.redirect(flask.url_for('home_page'))

@app.route('/image/<image_filename>')
def download_image(image_filename:str):
    image_path = Profile.get_images_path()
    image_filepath = image_path.joinpath(image_filename)
    if not image_filepath.exists():
        return flask.abort(404)
    return flask.send_from_directory(directory=image_path,path=image_filename)
        