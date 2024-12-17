from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Train the model if not already trained
MODEL_FILE = "calories_model.pkl"
if not os.path.exists(MODEL_FILE):
    # Load datasets
    calories_df = pd.read_csv("calories.csv")
    exercise_df = pd.read_csv("exercise.csv")

    # Merge datasets
    data = pd.merge(exercise_df, calories_df, on="User_ID")

    # Feature selection and preprocessing
    features = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
    data = pd.get_dummies(data, columns=['Gender'], drop_first=True)  # Encode Gender to binary

    # Prepare input features (X) and target (y)
    X = data[['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 'Gender_male']]
    y = data['Calories']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, MODEL_FILE)
else:
    print("Model already exists. Skipping training...")

# Load the saved model
loaded_model = joblib.load(MODEL_FILE)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    age = float(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    duration = float(request.form['duration'])
    heart_rate = float(request.form['heart_rate'])
    body_temp = float(request.form['body_temp'])
    gender = request.form['gender']

    # Encode gender
    gender_male = 1 if gender == 'male' else 0

    # Prepare input features for prediction
    input_features = np.array([[age, height, weight, duration, heart_rate, body_temp, gender_male]])

    # Make prediction
    prediction = loaded_model.predict(input_features)
    output = round(prediction[0], 2)

    # Return prediction to the form
    return render_template('index.html', prediction_text=f'Predicted Calories Burned: {output}')

if __name__ == "__main__":
    app.run(debug=True)
