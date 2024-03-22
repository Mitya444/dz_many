from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carsss.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    cars = db.relationship('Car', backref='owner', lazy=True)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@app.route('/fill_data')
def fill_data():
    user1 = User(name='John')
    user2 = User(name='Alice')

    car1 = Car(brand='Toyota', model='Camry', owner=user1)
    car2 = Car(brand='Honda', model='Civic', owner=user1)
    car3 = Car(brand='Ford', model='Mustang', owner=user2)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(car1)
    db.session.add(car2)
    db.session.add(car3)
    db.session.commit()

    return 'Data added successfully!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    #fill_data()
    app.run(debug=True)
