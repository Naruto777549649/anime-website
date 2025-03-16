from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

@app.route('/')
def home():
    animes = Anime.query.all()
    return render_template('index.html', animes=animes)

@app.route('/add', methods=['GET', 'POST'])
def add_anime():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image_url = request.form['image_url']
        
        new_anime = Anime(name=name, description=description, image_url=image_url)
        db.session.add(new_anime)
        db.session.commit()
        flash("Anime added successfully!", "success")
        return redirect('/')
    return render_template('add_anime.html')

if __name__ == '__main__':
    app.run(debug=True)