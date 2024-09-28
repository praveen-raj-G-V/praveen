
# Diabetes prediction Using Machine Learning

## Overview

This project presents a machine learning-based web application for predicting diabetes. The application:

-  if a person is diabetic.

- Classifies between Type 1 and Type 2 diabetes.

- Provides personalized recommendations for diabetes management.

 - Built using a Decision Tree classifier, the model aims to improve prediction accuracy and care.

# Features

- Diabetes Prediction (Diabetic/Non-Diabetic).
- Type Classification (Type 1 or Type 2 Diabetes).
- Personalized Recommendations for diabetes management.


# Project structure
- project_folder/
  - app.py
  - trained.ipynb
  - diabetesmodel.pkl
  - dataset.csv
  - templates/
      - index.html
      - result.html
  - static/
      - styles.css

# How to Run the Project
## Train the Model
Open trained.ipynb in Jupyter Notebook.
Run the notebook to train the model.
The trained model will be saved as diabetesmodel.pkl.

## Set Up the Web Application
Install Flask using:

pip install Flask

Place app.py, diabetesmodel.pkl, dataset.csv, and the templates/ and static/ folders in the same directory.

## Run the Web Application
Run app.py using:

python app.py

Access the web app at http://127.0.0.1:5000.
4. Upload Data and Get Predictions
Upload data through the web interface.

Get predictions on whether the user is diabetic, the type of diabetes, and personalized recommendations.

## Dataset
The dataset (dataset.csv) is provided with the project and used to train the model.

## Dependencies
- Python 3.x
- Flask
- Jupyter Notebook
- Pandas
- Scikit-learn
# Screenshots

![Screenshot 2023-11-03 224302](https://github.com/user-attachments/assets/08d35bf5-b16c-408d-be67-7a47c17e097c)

## posibility-1: Diabetic
![Screenshot 2023-11-03 230112](https://github.com/user-attachments/assets/10f18982-fade-4734-9fc2-b31ead328b04)

## posibility-2: Not Diabetic
![Screenshot 2023-11-03 225518](https://github.com/user-attachments/assets/b76ad76d-9e9c-4140-9701-41052fce3ea1)



## Documentation

[project report.pdf](https://github.com/user-attachments/files/17174892/project.report.GV.final.1.pdf)



## Conclusion
Just try it for your practices.If error occurs kindly mention via praj77258@gmail.com