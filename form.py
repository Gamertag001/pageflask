from flask import Flask, render_template, request

form = Flask(__name__)

@form.route('/')
def inicio():
	return render_template('inicio2.html')

@form.route('/formulario', methods=['GET', 'POST'])
def formulario():
	if request.method == 'POST':
		nombre = request.form['nombre']
		correo = request.form['correo']
		return render_template('response.html',nombre=nombre, correo=correo)
	return render_template('form.html')

if __name__ =='__main__':
	form.run(debug=True)