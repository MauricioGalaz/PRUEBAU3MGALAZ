from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/calcular_promedio', methods=['POST'])
def calcular_promedio():
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    promedio = round((nota1 + nota2 + nota3) / 3, 2)  # Redondear a 2 decimales
    estado = "Aprobado" if (promedio >= 40) and (asistencia >= 75) else "Reprobado"


    return render_template('ejercicio1.html', nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia, promedio=promedio, estado=estado)



@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/comparar_nombres', methods=['POST'])
def comparar_nombres():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    nombres = [nombre1, nombre2, nombre3]

    nombre_mas_largo = max(nombres, key=len)
    cantidad_caracteres = len(nombre_mas_largo)

    return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo,
                           cantidad_caracteres=cantidad_caracteres, nombres=nombres)


if __name__ == '__main__':
    app.run(debug=True)


