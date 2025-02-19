# Student Marks Prediction using Machine Learning
# Introduction
Student marks prediction is a crucial application of machine learning, helping students understand their expected scores based on study hours. This project utilizes a trained machine learning model to predict students' marks based on the number of study hours they input.

This web application is built using Flask, and the model used is a pre-trained regression model stored in student_mark_prediction.pkl. The application takes user input, processes it, makes predictions, and displays the result in a user-friendly manner.

# Implementation
The prediction logic is implemented in app.py. This script loads a trained ML model using joblib, processes user inputs via Flask, and serves predictions on a web page.

# Key Features
Users can enter the number of study hours in the web interface.
The application validates the input (ensuring study hours are between 1 and 24).
The trained model predicts student marks based on study hours.
All predictions are stored in a CSV file (smp_data_from_app.csv) for future reference.

# Tools & Technologies Used
Python (Flask for web development)
NumPy & Pandas (Data processing)
Scikit-Learn (Machine Learning)
Joblib (Model loading)
HTML, CSS (Frontend UI)
