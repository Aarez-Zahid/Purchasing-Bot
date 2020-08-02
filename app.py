from webscripts import courtside_shoe_bot
from flask import  Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_data():
    website_type = request.form['website']
    shoe_size = request.form['size']
    link = request.form['weblink']


    if (website_type == "courtside"):
        courtside_shoe_bot(link,shoe_size)


    return "done"



if __name__ == "__main__":
    app.run(debug=True)




















