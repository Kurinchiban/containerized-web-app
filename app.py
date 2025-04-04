from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/flaskapp'
db = SQLAlchemy(app)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    vehicle_type = request.form['vehicle_type']
    new_vehicle = Vehicle(type=vehicle_type)
    db.session.add(new_vehicle)
    db.session.commit()
    return 'Vehicle added successfully!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host='0.0.0.0', port=5000)
