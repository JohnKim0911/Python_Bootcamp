from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap(app)
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# with app.app_context():
#     db.create_all()
#     db.session.commit()


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    img_url = StringField('Image (URL)', validators=[DataRequired(), URL()])
    loc = StringField('Location', validators=[DataRequired()])
    seats = SelectField('Seats', choices=['0-10', '10-20', '20-30', '30-40', '40-50', '50+'], validators=[DataRequired()])
    price = StringField('Coffee Price', validators=[DataRequired()])
    toilet = BooleanField('Has Toilet?')
    wifi = BooleanField('Has Wifi?')
    sockets = BooleanField('Has Sockets?')
    calls = BooleanField('Can Take Calls?')
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    all_cafes = db.session.query(Cafe).all()
    list_of_rows = [cafe.to_dict() for cafe in all_cafes]
    return render_template('cafes.html', cafes=list_of_rows)


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        has_toilet = form.toilet.data
        has_wifi = form.wifi.data
        has_sockets = form.sockets.data
        can_take_calls = form.calls.data

        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=has_sockets,
            has_toilet=has_toilet,
            has_wifi=has_wifi,
            can_take_calls=can_take_calls,
            seats=request.form.get("seats"),
            coffee_price=request.form.get("price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


# HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
