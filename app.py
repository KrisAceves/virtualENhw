from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", name="Kristian Aceves", aboutMe=["I am a UTRGV student.", "I enjoy coding."])

@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/user/<username>")
def user(username):
    return f"Hello, {username}!"

if __name__ == "__main__":
    app.run(debug=True)
