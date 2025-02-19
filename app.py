# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

# Initialize Flask App
app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')

# Load ML Model
model_path = os.path.join(os.getcwd(), "student_mark_prediction.pkl")
model = joblib.load(model_path)

# DataFrame to Store Predictions
df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    global df
    
    try:
        input_features = [int(request.form['study_hours'])]
        features_value = np.array(input_features)
        
        # Validate input hours
        if input_features[0] < 0 or input_features[0] > 24:
            return render_template('index.html', prediction_text='Please enter valid hours between 1 to 24 if you live on Earth!')

        # Predict output
        output = model.predict([features_value])[0][0].round(2)

        # Store inputs and predicted values in DataFrame
        df = pd.concat([df, pd.DataFrame({'Study Hours': input_features, 'Predicted Output': [output]})], ignore_index=True)
        df.to_csv('smp_data_from_app.csv', index=False)

        return render_template('index.html', prediction_text=f'You will get [{output}%] marks when you study [{input_features[0]}] hours per day.')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
