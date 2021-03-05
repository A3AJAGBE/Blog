from flask import Flask, render_template, request
from datetime import datetime
from blog import Blog
import requests

# Get the year
current_year = datetime.now().year

blogs = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
blog_list = []
for blog in blogs:
    blog = Blog(blog["id"], blog["title"], blog["subtitle"], blog["body"], blog["image_url"], blog["date"],
                blog["author"])
    blog_list.append(blog)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', year=current_year, blogs=blog_list)


@app.route('/about')
def about():
    return render_template('about.html', year=current_year)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        message_info = f"The following information has been sent successfully; " \
                       f"Name: {name}, " \
                       f"Email: {email}, " \
                       f"Phone Number: {phone}, " \
                       f"Message: {message}"
        return render_template('contact.html', year=current_year, sent=True, message_info=message_info)
    return render_template('contact.html', year=current_year, sent=False)


@app.route("/blog/<int:blog_id>")
def blog(blog_id):
    detail_blog = None
    for blog_post in blog_list:
        if blog_post.id == blog_id:
            detail_blog = blog_post
    return render_template("blog.html", year=current_year, blog=detail_blog)


if __name__ == '__main__':
    app.run(debug=True)
