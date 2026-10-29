from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='proyecto',
        password='ingadima',
        database='estudiantes_db',
        charset='utf8mb4'
    )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    p1 = request.form['p1']
    p2 = request.form['p2']
    p3 = request.form['p3']
    p4 = request.form['p4']
    p5 = request.form['p5']
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO respuestas_ia (nombre, correo, p1, p2, p3, p4, p5) VALUES (%s,%s,%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nombre, correo, p1, p2, p3, p4, p5))
        conexion.commit()
        conexion.close()
        mensaje = "Datos registrados"
    except Exception as e:
        mensaje = f"Hubo un error: {e}"

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)