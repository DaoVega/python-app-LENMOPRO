from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Función para conectar a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='flaskdb'
    )

# Ruta principal: muestra el formulario
@app.route('/')
def index():
    return render_template('index.html')

from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Función para conectar a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='flaskdb'
    )

# Ruta principal: muestra el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para registrar el correo
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name:
        return jsonify({'error': 'El nombre es obligatorio'}), 400
    if not email:
        return jsonify({'error': 'El correo electrónico es obligatorio'}), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = 'INSERT INTO users (name, email) VALUES (%s, %s)'
        cursor.execute(query, (name, email))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({'message': f'Usuario {name} registrado correctamente'}), 200
    except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
            return jsonify({'error': f'Error al registrar usuario: {err}'}), 500
    except Exception as e:
            print(f"Error general: {e}")
            return jsonify({'error': 'Error al registrar usuario'}), 500



def init_db():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) NOT NULL UNIQUE
            )
        ''')
        connection.commit()
        cursor.close()
        connection.close()
        print("Base de datos inicializada correctamente.")
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")



if __name__ == '__main__':
    print("Iniciando la aplicación...")
    init_db() 
    app.run(host='0.0.0.0', port=5001)

