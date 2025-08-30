from flask import Flask, render_template, request

suma = Flask(__name__)

@suma.route('/')
def inicio():
	return render_template('inicio2.html')

@suma.route('/calculadora', methods=['GET', 'POST'])
def formulario():
	if request.method == 'POST':
		numero_1 = int(request.form['numero 1'])
		numero_2 = int(request.form['numero 2'])
		total = request.form['total']
		return render_template('response_suma.html',numero_1=numero_1, numero_2=numero_2, total=total)
	return render_template('form2.html')

if __name__ =='__main__':
	suma.run(debug=True)