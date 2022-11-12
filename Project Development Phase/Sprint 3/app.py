import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='Template')
model = pickle.load(open('D:/IBM_UAEP/model.pkl', 'rb'))



@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['GET','post'])
def predict():
	
	GRE_Score = int(request.form['GRE Score'])
	TOEFL_Score = int(request.form['TOEFL Score'])
	University_Rating = int(request.form['University Rating'])
	SOP = float(request.form['SOP'])
	LOR = float(request.form['LOR'])
	CGPA = float(request.form['CGPA'])
	Research = int(request.form['Research'])
	
	final_features = pd.DataFrame([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA,Research]])
	predict=model.predict(final_features)
	
	output=predict[0]
	if(output>0.60):
	   return render_template('chance.html')
	else:
		return render_template('nochance.html')   
	
    
	
	return render_template('index.html', prediction_text='Admission chances are'+ format(output))
	
if __name__ == "__main__":
	app.run(debug=True)