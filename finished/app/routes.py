from flask import redirect, request, render_template, url_for
from app import my_app, db
from app.models import Post

@my_app.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts)

@my_app.route('/new', methods=['POST'])
def new_post():
    author = request.form.get('author', '')
    body = request.form.get('body', '')
    title = request.form.get('title', '')
    post = Post(author=author, body=body, title=title)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))
