from flask import render_template,request,redirect,url_for,Blueprint,flash,abort
from flask_login import current_user,login_required
from Thetechblog import db
from Thetechblog.model import Blogpost
from Thetechblog.blogposts.forms import BlogPostForm

blogposts=Blueprint('blogposts',__name__)

@blogposts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form=BlogPostForm()
    if form.validate_on_submit():
        blog_post=Blogpost(title=form.title.data,
                           text=form.text.data,
                           user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html',form=form)

@blogposts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post=Blogpost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',title=blog_post.title,
                           date=blog_post.date,post=blog_post)

@blogposts.route('/<int:blog_post_id/update',methods=['GET','POST'])
@login_required
def update(blog_post_id):
    blog_post=Blogpost.query.get_or_404(blog_post_id)
    if blog_post.author!=current_user:
        abort(403)

    form=BlogPostForm()
    if form.validate_on_submit():
        blog_post.title=form.title.data
        blog_post.text=form.text.data
        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('blogposts.blog_post',blog_post_id=blog_post.id))
    elif request.method == 'GET':
        form.title.data=blog_post.title
        form.text.data=blog_post.text
    
    return render_template('create_post.html',title='Updating',form=form)

@blogposts.route('/<int:blog_post_id/delete',methods=['GET','POST'])
@login_required
def deletepost(blog_post_id):
    blog_post=Blogpost.query.get_or_404(blog_post_id)
    if blog_post.author!=current_user:
        abort(403)
    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))

        
    

