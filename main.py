from flask import Flask, render_template
from datetime import datetime
from blog import Blog
import requests

# Get the year
current_year = datetime.now().year

blogs = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
blog_list = []
for blog in blogs:
    blog = Blog(blog["id"], blog["title"], blog["subtitle"], blog["body"], blog["image_url"], blog["date"], blog["author"])
    blog_list.append(blog)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', year=current_year, blogs=blog_list)


@app.route('/about')
def about():
    return render_template('about.html', year=current_year)


@app.route('/contact')
def contact():
    return render_template('contact.html', year=current_year)


@app.route("/blog/<int:blog_id>")
def blog(blog_id):
    detail_blog = None
    for blog_post in blog_list:
        if blog_post.id == blog_id:
            detail_blog = blog_post
    return render_template("blog.html", year=current_year, blog=detail_blog)


if __name__ == '__main__':
    app.run(debug=True)
