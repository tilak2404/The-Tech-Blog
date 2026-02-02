#core/views.py
from Thetechblog.model import Blogpost
from flask import render_template,request,url_for,redirect,Blueprint
from datetime import datetime, timedelta

core=Blueprint('core',__name__)

@core.route('/')
def index():
    page=request.args.get('page',1,type=int)
    blog_posts=Blogpost.query.order_by(Blogpost.date.desc()).paginate(page=page,per_page=5)
    new_threshold = datetime.utcnow() - timedelta(hours=24)
    return render_template('index.html',blog_posts=blog_posts, new_threshold=new_threshold)

@core.route('/info')
def info():
    return render_template('info.html')