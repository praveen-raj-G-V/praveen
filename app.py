import numpy as np
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


import joblib

# Load the trained model using joblib
with open('diabetesmodel.pkl', 'rb') as file:
    model = joblib.load(file)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
            # Get input values from the form
            pregnancies = int(request.form['pregnancies'])
            glucose = float(request.form['glucose'])
            blood_pressure = float(request.form['blood_pressure'])
            skin_thickness = float(request.form['skin_thickness'])
            insulin = float(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = float(request.form['age'])
            

            # Make predictions and get probabilities
            input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
            prediction = model.predict(input_data)
            predicted_probabilities = model.predict_proba(input_data)

            if prediction[0] == 1:
                result = "The model predicts that the person is diabetic."

                # Get the probability of being diabetic
                probability_diabetic = predicted_probabilities[0][1]

                # Define a threshold for risk level (you can adjust this threshold as needed)
                risk_threshold = 0.5

                if probability_diabetic >= risk_threshold:
                    risk_level = "High"

                    # Determine diabetes type based on features
                    glucose_level = glucose
                    insulin_level = insulin
                    dpf_value = dpf

                    # Define threshold values to differentiate between Type 1 and Type 2 diabetes
                    glucose_threshold = 140  # Example threshold for glucose level
                    insulin_threshold = 5    # Example threshold for insulin level
                    dpf_threshold = 0.6      # Example threshold for diabetes pedigree function

                    if insulin_level < insulin_threshold and glucose_level > glucose_threshold and dpf_value > dpf_threshold:
                        diabetes_type = "Type 1"
                    else:
                        diabetes_type = "Type 2"
                else:
                    risk_level = "Low"
                    diabetes_type = "Not Applicable"  # Since the person is not diabetic

                # Provide generic recommendations (consult a healthcare professional for personalized advice)
                recommendations = [
                    "Maintain a healthy diet with balanced carbohydrate intake.",
                    "Engage in regular physical activity.",
                    "Monitor blood glucose levels regularly.",
                    "Take prescribed medications as directed by a healthcare provider.",
                    "Schedule regular check-ups with a healthcare professional.",
                ]

                # Return the results to the web interface
                return render_template('result.html', result=result, risk_level=risk_level, diabetes_type=diabetes_type, recommendations=recommendations)
            else:
                result = "The model predicts that the person is not diabetic."
                return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
