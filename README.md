# 🏠 House Price Prediction using Machine Learning

This project forecasts housing prices using various machine learning algorithms. It helps real estate developers, investors, and buyers make informed decisions based on data-driven predictions.

---

## 📌 Problem Statement

Accurate house price prediction reduces investment risks and promotes market transparency. This project uses historical housing data to build regression models that forecast home prices based on key features.

---

## 📊 Features

- Data cleaning pipeline with typecasting, mapping, and outlier handling
- Step-by-step Exploratory Data Analysis (EDA)
- Machine Learning Models:
  - ✅ Linear Regression (Best performing)
  - K-Nearest Neighbors (KNN)
  - Support Vector Regressor (SVR)
  - XGBoost
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting Regressor
- EDA visualizations for correlation, distributions, and relationships
- Web app interface built using Flask, HTML, CSS, and JavaScript (local only)

---

## 🗂 Project Structure

- house_price_prediction/
  - app.py
  - clean_dataset.py
  - cleaned_housing_dataset.csv
  - linear_regression_model_2.pkl
  - eda_step_1.py
  - eda_step_2.py
  - eda_step_3.py
  - eda_step_4.py
  - eda_step_5.py
  - eda_step_6.py
  - eda_step_7.py
  - eda_step_8.py
  - eda_step_9.py
  - eda_step_10.py
  - uploads/
    - housedata.csv
  - static/
    - index.css
    - prediction.css
    - script.js
    - House Image.jpg
    - eda_result1.png
    - eda_result2.png
    - eda_result3.png
    - eda_result4.png
    - eda_result5.png
    - eda_result6.png
    - eda_result7.png
    - eda_result8.png
    - eda_result9.png
    - eda_result10.png
  - templates/
    - index.html
    - prediction.html
    - cleaning_eda.html
  - README.md
  - requirements.txt

---
## 📈 Dataset Information

- 📦 Source: [Kaggle Housing Dataset](https://www.kaggle.com/datasets/shree1992/housedata)
- Records after cleaning: **3,618 rows**
- Features include:
  - Bedrooms, Bathrooms
  - Living Area, Lot Area
  - Basement and Above Basement Area
  - ZIP, City, Floors, Waterfront, View/Condition Ratings

---

## ✅ Best Performing Model: Linear Regression

- R² Score: **0.63**
- Mean Squared Error (MSE): **16.8 Billion**
- Preprocessing: StandardScaler
- Hyperparameter tuning: GridSearchCV, Cross-Validation

---

## 📊 Visualizations

- Histograms and Box Plots before/after cleaning
- Correlation heatmaps
- Bar and pie charts for categorical distributions
- Actual vs Predicted Scatter Plots
- Residual error histograms
- Model-wise comparison of R² and MSE

---

## 🧠 Future Enhancements

- ✅ Deploy the app to Render/Heroku/AWS
- 📍 Add geospatial features (e.g., proximity to amenities)
- 📦 Integrate model stacking or deep learning
- 📧 Set up email alerts for price changes
- 📱 Make the frontend fully mobile-responsive

---

## 📚 References

- [Kaggle Dataset](https://www.kaggle.com/datasets/shree1992/housedata)
- [scikit-learn](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [RealPython Guide to Data Cleaning](https://realpython.com/python-data-cleaning-numpy-pandas/)

---

## 👨‍💻 Authors

- **Jonnalagadda Satvik**
- **Komatineni Jaswanth**
- **Jaladi Hima Venkata Sai Saketh Ram**

> 🎓 This project was built as part of the *Data Intensive Computing* final course at University at Buffalo.
