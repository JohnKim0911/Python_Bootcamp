from flask import Flask, render_template
import requests

# Flask web app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Harry Potter API
URL_all_characters = "https://hp-api.onrender.com/api/characters"
response = requests.get(url=URL_all_characters)
response.raise_for_status()
all_characters = response.json()


@app.route("/")
def home():
    return render_template("index.html", all_characters=all_characters)


if __name__ == '__main__':
    app.run(debug=True)