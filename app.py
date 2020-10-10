from webscripts import courtside_bot, nrml_bot, deadstock_bot
from flask import  Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def handle_data():

    if (request.method == "POST"):

        website_type = request.form['website']
        size = request.form['size']
        link = request.form['weblink']

        if (website_type == "courtside"):
            courtside_bot(link, size)
        if (website_type == "nrml"):
            nrml_bot(link, size)
        if (website_type == "deadstock"):
            deadstock_bot(link, size)
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)




















