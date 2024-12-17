## 🔥 **Calories Burned Prediction Web App**

This project is a **Flask-based web application** that predicts the **calories burned** during a workout session based on user input such as age, weight, height, exercise duration, heart rate, and body temperature. The prediction is powered by a **Random Forest Regressor** machine learning model.

---

### 🚀 **Features**

- **User-Friendly Interface**: Modern, attractive, and responsive UI.
- **Input Fields**:
   - Age  
   - Height (cm)  
   - Weight (kg)  
   - Exercise Duration (mins)  
   - Heart Rate (bpm)  
   - Body Temperature (°C)  
   - Gender (Male/Female)  
- **Prediction Output**: Real-time prediction of calories burned displayed on the UI.

---

### 📊 **Technology Stack**

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, Font Awesome, Google Fonts
- **Machine Learning**: Random Forest Regressor (sklearn)
- **Libraries**:
   - `Flask`  
   - `sklearn`  
   - `pandas`  
   - `numpy`  
   - `joblib`  

---

### 🛠️ **Setup and Installation**

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/calories-prediction-app.git
   cd calories-prediction-app
   ```

2. **Install Dependencies**:
   Ensure Python is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Data**:
   - Add your `calories.csv` and `exercise.csv` datasets to the root folder.
   - These datasets should include user exercise and calorie data.

4. **Run the Flask Application**:
   ```bash
   python app.py
   ```

5. **Access the Web App**:
   Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

### 🖥️ **Usage**

1. Fill out the form with your **personal details** (age, height, weight, etc.).
2. Click the **Predict** button.
3. The predicted **calories burned** will be displayed below the form.

-
### 🧪 **Model Training**

The machine learning model (Random Forest Regressor) was trained using:
- **Input Features**:
   - Age, Height, Weight, Exercise Duration, Heart Rate, Body Temperature, Gender
- **Target**: Calories burned

The model is saved using `joblib` and loaded during runtime.

---

### 🤝 **Contributing**

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-yourFeatureName
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your feature or fix"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-yourFeatureName
   ```
5. Submit a pull request.

---

### 🔒 **License**

This project is licensed under the **MIT License**.
