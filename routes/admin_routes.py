#管理员能访问的页面
from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import login_required
from services.image_service import ImageService
from services.article_service import ArticleService
from models.article import Article
from forms.article_form import ArticleForm
from forms.delete_article_form import DeleteArticleForm
from forms.image_upload_form import ImageUploadForm
from routes import app
from common.profile import Profile
from werkzeug.utils import secure_filename
from common.utils import get_save_filepath

@app.route('/createarticle.html',methods=['GET','POST'])
@login_required
def create_article_page():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article()
        new_article.title = form.title.data
        new_article.content = form.content.data
        try:
            article,error_msg = ArticleService().create_article(new_article)
            if error_msg:
                flash(f'发布文章失败:{error_msg}',category='danger')
            else:
                flash(f'发布文章完成',category='success')
                return redirect(url_for('home_page'))
        except Exception as e:
            flash(f'发布文章失败:{e}',category='danger')
    return render_template('edit_article.html',form=form,is_edit=False)

@app.route('/editarticle/<article_id>',methods=['GET','POST'])
@login_required
def edit_article_page(article_id:str):
    form = ArticleForm()
    if request.method == 'GET':
        try:
            article = ArticleService().get_article_by_id(int(article_id))
            if not article:
                flash(f'要修改的文章未找到',category="danger")
                return redirect(url_for('home_page'))
            else:
                form.title.data = article.title
                form.content.data = article.content               
        except Exception as e:
            flash(f'提取文章失败:{e}',category="danger")
            return redirect(url_for('home_page'))
            
    
    if form.validate_on_submit():
        try:
            updateed_article = Article()
            updateed_article.id = int(article_id)
            updateed_article.title = form.title.data
            updateed_article.content = form.content.data
            article,error_msg = ArticleService().update_article(updateed_article)
            if error_msg:
                flash(f'编辑文章失败:{error_msg}',category='danger')
            else:
                flash(f'发布文章完成',category='success')
                return redirect(url_for('home_page'))
        except Exception as e:
            flash(f'修改文章失败:{e}',category='danger')
    return render_template("edit_article.html",form = form,is_edit=True)


@app.route('/delete_article',methods=['POST'])
@login_required
def delete_article():
    form = DeleteArticleForm()
    if form.validate_on_submit():
        try:
            result,error_msg = ArticleService().delete_article(int(form.article_id.data))
            if result:
                flash(f'成功删除文章',category='success')
                return redirect(url_for('home_page'))
            else:
                flash(f'删除文章失败:{error_msg}',category='danger')
        except Exception as e:
            flash(f'删除文章失败:{e}',category='danger')
    return redirect(url_for('home_page'))
    
    
@app.route('/images',methods=['GET','POST'])
@login_required
def images_page():
    form = ImageUploadForm()
    if form.validate_on_submit():
       image_file = form.image_file.data     
       images_path = Profile.get_images_path()
       #确保文件名符合规范
       image_file_name = secure_filename(image_file.filename)
       image_full_path = images_path.joinpath(image_file_name)
       path_to_save=get_save_filepath(image_full_path)
       #保存
       image_file.save(path_to_save)
       flash(f'图片保存为:{path_to_save}',category="success")
    image_file_names = ImageService().get_image_filename_list()
       
    return render_template('images.html',form=form,image_file_names=image_file_names)