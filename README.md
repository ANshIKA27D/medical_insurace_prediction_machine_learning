# 🩺 Medical Insurance Premium Predictor

This project aims to predict the **medical insurance premium** for individuals based on various personal attributes such as age, BMI, smoking status, number of children, gender, and region. The model helps insurance providers and individuals estimate the cost of medical insurance plans with the help of machine learning algorithms.

## 🚀 Project Objective

The objective of this project is to develop a robust predictive system that estimates medical insurance charges using multiple machine learning models. This can assist insurance companies in pricing premiums more accurately and help users understand how different factors influence their insurance costs.

---

## 📊 Dataset

- **Source**: [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Features**:
  - `age`: Age of the individual
  - `sex`: Gender (male/female)
  - `bmi`: Body Mass Index
  - `children`: Number of children covered by insurance
  - `smoker`: Smoking status
  - `region`: Residential region in the US
  - `charges`: Medical insurance cost (target variable)

---

## 🧠 Models Used

The following machine learning models were trained and evaluated:

1. **Linear Regression**  
   A basic regression model to establish a linear relationship between features and premium charges.

2. **Random Forest Regressor**  
   An ensemble-based algorithm using multiple decision trees for improved accuracy and generalization.

3. **XGBoost Regressor**  
   A powerful gradient boosting algorithm optimized for speed and performance in predictive tasks.

---

## ⚙️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **Scikit-learn**
- **XGBoost**
- **Streamlit** (for the interactive web app)

---

## 📈 Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

Model performance was compared on training and test sets using the above metrics to assess overfitting and accuracy.

---

## 🖥️ Deployment

The model is deployed using **Streamlit**, providing an interactive web interface where users can enter input parameters (age, BMI, etc.) and receive a predicted insurance premium.

To run the app locally:
```bash
streamlit run app.py
