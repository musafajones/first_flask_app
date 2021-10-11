from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        "author": "Jahmal Daniels",
        "title" : "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "February 20th, 2021"
    },
    {
        "author": "Marsellus Wallace",
        "title" : "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "February 24th, 2021"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ == "__main__":
    app.run(debug=True)


