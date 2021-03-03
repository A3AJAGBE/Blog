from flask import Flask, render_template
from datetime import datetime
from blog import Blog
import requests

blogs = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
blog_list = []
for blog in blogs:
    blog = Blog(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    blog_list.append(blog)

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year, blogs=blog_list)


if __name__ == '__main__':
    app.run(debug=True)
