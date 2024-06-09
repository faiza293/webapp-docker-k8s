from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://faizauser:Fayiz@293@34.136.236.4/faizadb'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    value1 = db.Column(db.String(50))
    value2 = db.Column(db.String(50))

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    value1 = data['value1']
    value2 = data['value2']
    
    new_data = Data(value1=value1, value2=value2)
    db.session.add(new_data)
    db.session.commit()
    
    return jsonify({'message': 'Data submitted successfully!'})

if __name__ == '__main__':
    # Create all database tables
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
