from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Optional
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    """Admin login form"""
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

class ContactForm(FlaskForm):
    """Contact form for frontend"""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    subject = StringField('Subject', validators=[Optional(), Length(max=200)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=2000)])
    phone = StringField('Phone', validators=[Optional(), Length(max=20)])
    company = StringField('Company', validators=[Optional(), Length(max=100)])

class PageForm(FlaskForm):
    """Page creation/editing form"""
    title = StringField('Title', validators=[DataRequired(), Length(max=200)])
    slug = StringField('Slug', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[Optional()])
    meta_description = TextAreaField('Meta Description', validators=[Optional(), Length(max=500)])
    meta_keywords = StringField('Meta Keywords', validators=[Optional(), Length(max=500)])
    template_name = SelectField('Template', choices=[
        ('page.html', 'Default Page'),
        ('index.html', 'Home Page'),
    ], default='page.html')
    is_published = BooleanField('Published', default=True)
    is_featured = BooleanField('Featured')

class SiteConfigForm(FlaskForm):
    """Site configuration form"""
    site_title = StringField('Site Title', validators=[Optional(), Length(max=200)])
    site_description = TextAreaField('Site Description', validators=[Optional(), Length(max=500)])
    contact_email = StringField('Contact Email', validators=[Optional(), Email()])
    social_twitter = StringField('Twitter URL', validators=[Optional()])
    social_linkedin = StringField('LinkedIn URL', validators=[Optional()])
    social_github = StringField('GitHub URL', validators=[Optional()])
    social_instagram = StringField('Instagram URL', validators=[Optional()])
