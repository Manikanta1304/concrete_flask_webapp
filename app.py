from flask import *
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('concrete.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		cement = float(request.form['cement'])
		slag = float(request.form['slag'])
		ash = float(request.form['ash'])
		water = float(request.form['water'])
		superplastic = float(request.form['superplastic'])
		coarseagg = float(request.form['coarseagg'])
		fineagg = float(request.form['fineagg'])
		age = float(request.form['age'])

		inputs = np.array([[cement,slag,ash,water,
	 			superplastic,coarseagg,fineagg,
	 			age]])

		prediction = model.predict(inputs)

		return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
	app.run(debug=True)