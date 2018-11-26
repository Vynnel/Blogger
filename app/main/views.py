from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Post, Comment
from .. import db
from .forms import PostForm, CommentForm
from flask_login import login_required, current_user
import datetime
from ..email import mail_message

#Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()

    title = 'Home - Welcome to The Blogger'

    return render_template('index.html', title=title, posts=posts)


