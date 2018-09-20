from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment
from .forms import UpdateProfile,BlogForm,CommentForm,SubscriberForm
from . import main
from .. import db,photos
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Subscriber
from datetime import datetime
from ..email import mail_message

#view function that handles profile display
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user) 

#a view function that will handle an update request
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)


#routing to display admins profile picture
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/blog', methods=['GET','POST'])
@login_required
def blog():
    blog_form=BlogForm()
    if blog_form.validate_on_submit():        
        new_blog = Blog(category=blog_form.category.data,title = blog_form.title.data)
        db.session.add(new_blog)
        db.session.commit()
    subscribers = Subscriber.query.all()
    for email in subscribers:
        mail_message("Hello Welcome To your Health Is Your Wealth Blog ","email/welcome_post",email.email,subscribers=subscribers)
    return render_template('blog.html',blog_form=blog_form) 

#routing for subscribers/receive email after subscription
@main.route('/', methods=['GET','POST'])
def subscriber():
    subscriber_form=SubscriberForm()
    if subscriber_form.validate_on_submit():
        subscriber= Subscriber(email=subscriber_form.email.data,title = subscriber_form.title.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Hey Welcome To My Blog ","email/welcome_subscriber",subscriber.email,subscriber=subscriber)
    subscriber = Blog.query.all()
    food = Blog.query.all()
    return render_template('index.html',subscriber=subscriber,subscriber_form=subscriber_form,blog=blog) 

#view function for comment display
@main.route('/comments/<int:id>', methods=['GET','POST'])
def comment(id):
    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(description=comment_form.describe.data,blog_id=id)
        db.session.add(new_comment)
        db.session.commit()
    comments = Comment.query.filter_by(blog_id=id)
    return render_template('comment.html',comment_form=comment_form,comments=comments)    

#delete blog when user is authenticated
@main.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    try:
        if current_user.is_authenticated:
            blogs = Blog.query.filter_by(id=id).all()
            for blog in blogs: 
                db.session.delete(blog)
                db.session.commit()
            return redirect(url_for('main.blog'))
        return '  '
    except Exception as e:
        return(str(e))    

#deleting a comment by the admin
@main.route('/del/<int:id>', methods=['GET','POST'])
def deleted(id):
    try:
        if current_user.is_authenticated:
            comment_form=CommentForm()
            comment = Comment.query.filter_by(comment_id=id).first()
            for comment in comments: 
                db.session.delete(comment)
                db.session.commit()
            return redirect(url_for('main.comment'))
        return ''
    except Exception as e:
        return(str(e))    

        

