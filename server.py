import os
import smtplib
from models.blog import Posts
from flask import Flask, render_template, request
app = Flask(__name__)

posts = Posts()
OWN_EMAIL = os.environ.get('email')
OWN_PASSWORD = os.environ.get('password')
print(OWN_EMAIL, OWN_PASSWORD)


@app.route('/')
def index():
    return render_template('index.html', title="Developo Network - The tech Blog", blog=posts)


@app.route('/about')
def about():

    return render_template('about.html', title="About")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            print(name, email, message)

        except:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            print("Something went wrong")
        finally:
            send_email(name=name, email=email, message=message)

    return render_template('contact.html', title="Contact")


@app.route('/blog/<post>/<id>')
def post(post, id=None):
    print(id)
    posts.current_post = int(id)-1
    print()

    return render_template('post.html', title=post, post=posts.get_currnt_post())


def send_email(name, email,  message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True)
