# Equipment Failure Detection using Machine Learning

## 📌 Overview
This project focuses on predicting **equipment failures** using historical sensor data and machine learning techniques.  
By analyzing operational parameters such as temperature, vibration, pressure, and runtime, the model predicts the likelihood of equipment failure in advance, enabling **predictive maintenance** and reducing downtime and operational costs.

---

## 🧠 Problem Statement
Unexpected equipment failures lead to production losses, safety risks, and high maintenance costs.  
Traditional maintenance strategies are reactive or time-based.  
This project aims to implement a **data-driven predictive maintenance system** that can identify potential failures before they occur.

---

## ⚙️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn

---

## 📂 Project Structure

Equipment_failure_Detection/
│
├── equipment_failure.py # Model training & prediction script
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── data/ # Sensor dataset (ignored in repo)
│ ├── train.csv
│ └── test.csv
├── models/ # Saved ML models (ignored in repo)


---

## 📊 Dataset
The dataset consists of time-series sensor readings collected from industrial equipment, including:
- Temperature
- Vibration
- Pressure
- Rotational speed (RPM)
- Operating hours

Target variable:
- `failure_next_7d` (indicates whether failure occurs in the next 7 days)

---

## 🏗️ Model & Approach
- Data preprocessing and feature engineering
- Handling missing values using imputation
- Feature scaling using StandardScaler
- Machine Learning models:
  - Random Forest Classifier
  - Gradient Boosting (optional)
- Model evaluation using:
  - Accuracy
  - Precision, Recall, F1-score
  - ROC-AUC

---

## 🚀 How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/USERNAME/Equipment_failure_Detection.git
cd Equipment_failure_Detection

pip install -r requirements.txt

Run the project: python equipment_failure.py
