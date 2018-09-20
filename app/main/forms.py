from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email
from ..models import Subscriber
from wtforms import ValidationError

class BlogForm(FlaskForm):    
    category = StringField('Post  Blog' ,validators=[Required()])
    title = StringField('Enter Your Name' ,validators=[Required()])
    submit = SubmitField('Go')
    
class CommentForm(FlaskForm):
    describe = StringField('Write A comment' ,validators=[Required()])
    submit = SubmitField('Go') 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Go')


class SubscriberForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    title = StringField('Entre Your Name' ,validators=[Required()])
    submit = SubmitField('Subscribe')    

    def validate_email(self,data_field):
                if Subscriber.query.filter_by(email =data_field.data).first():
                    raise ValidationError('There is an account with that email')
