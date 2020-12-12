from models.blog import Posts
from flask import Flask, render_template
app = Flask(__name__)

posts = Posts()


@app.route('/')
def index():
    return render_template('index.html', title="Developo Network - The tech Blog", blog=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")


@app.route('/blog/<post>/<id>')
def post(post, id=None):
    print(id)
    posts.current_post = int(id)-1
    print()

    return render_template('post.html', title=post, post=posts.get_currnt_post())


if __name__ == '__main__':
    app.run(debug=True)
