import logging
from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def get_db_connection():
    logging.info('Attempting to connect to the database')
    conn = psycopg2.connect(
        host="34.136.236.4",
        database="faizadb",
        user="faizauser",
        password="Fayiz@293"
    )
    logging.info('Connected to the database')
    return conn

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        value1 = data.get('value1')
        value2 = data.get('value2')
        if value1 and value2:
            conn = get_db_connection()
            cursor = conn.cursor()
            logging.info(f'Inserting data: {value1}, {value2}')
            cursor.execute("INSERT INTO data (value1, value2) VALUES (%s, %s)", (value1, value2))
            conn.commit()
            cursor.close()
            conn.close()
            logging.info(f'Data inserted successfully: {value1}, {value2}')
            return jsonify({'message': 'Data inserted successfully!'}), 200
        else:
            logging.error('Invalid data received')
            return jsonify({'error': 'Invalid data!'}), 400
    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return jsonify({'error': 'Internal server error!'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
