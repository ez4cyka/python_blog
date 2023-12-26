from operator import and_
from models.article import Article
from routes import db
from sqlalchemy import Select, func
class ArticleService:
    #根据id查文章
    def get_article_by_id(self,id):
        return db.session.get(Article,id)
    def get_articles(self):
        return db.session.query(Article).all()
        # query = Select(Article)
        # return db.session.scalars(query).all()
    def create_article(self,article:Article):
        #检查文章标题的唯一性
        query = Select(Article).where(Article.title == article.title)
        exist_article = db.session.scalars(query).all()
        if exist_article:
            return article,"同标题的文章已存在"
        try:
            db.session.add(article)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return article,None
    def update_article(self,article:Article):
        exist_article = db.session.get(Article,article.id)
        if not exist_article:
            return article,"文章不存在"
        query = Select(Article).where(and_(Article.title == article.title,Article.id != article.id))
        other_article = db.session.scalars(query).all()
        if other_article:
            return article,"同标题的文章已存在"
        exist_article.title =   article.title
        exist_article.content = article.content
        exist_article.update_time = func.now()
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return article,None
    
    def delete_article(self,article_id:int):
        article = db.session.get(Article,article_id)
        if article:
            try:
                db.session.delete(article)
                db.session.commit()
                return True,None
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            return False,'找不到要删除的文章'
        