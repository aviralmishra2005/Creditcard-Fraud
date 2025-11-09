<<<<<<< HEAD
---

# Credit Card Fraud Detection with Visualizations

## Overview

This project trains a **Random Forest** model to detect credit card fraud, handling class imbalance with **SMOTE**. It includes:

* Training and evaluating the model
* Visualizing class distribution and feature importance
* Saving the trained model for later predictions

Designed to run in **Google Colab** or any Jupyter Notebook.

---

## Usage

1. **Open Colab** and create a new notebook.
2. **Upload your CSV** (creditcard.csv):

```python
from google.colab import files
uploaded = files.upload()
```

3. **Run the notebook cells** in order:

   * Install missing libraries
   * Load and explore dataset
   * Train model
   * Evaluate and visualize results
   * Save model (`model.joblib`)

4. **Download files** if needed:

```python
from google.colab import files
files.download("model.joblib")       # Trained model
results.to_csv("predictions.csv")    # Predictions
files.download("predictions.csv")
```

---

## Features & Visualizations

* Class distribution plot (Legit vs Fraud)
* Confusion matrix
* Feature importance ranking
* Classification metrics (Precision, Recall, F1-score, Accuracy)

---

## Notes

* Dataset must include a `Class` column (0 = Legit, 1 = Fraud)
* `requirements.txt` contains all needed libraries
* You can modify the model or add new visualizations as needed

---
=======
# Credit Card Fraud Detection

This project provides a simple credit card fraud detection system using machine learning. It includes a Jupyter notebook for training the model and a Streamlit web app for making predictions on new transaction data.

## Project Structure

* `creditcard-fraud-detection.ipynb` – Trains and builds the fraud detection model using **pandas**, **scikit-learn**, **imbalanced-learn**, and **joblib**.
* `model.joblib` – The trained machine learning pipeline saved from the notebook.
* `main.py` – Streamlit web app that loads `model.joblib` and predicts fraud on uploaded transaction CSV files.

## Features

* Detects potential credit card fraud in transaction data.
* Handles both numeric and categorical features.
* Balances the dataset using SMOTE to improve model performance.
* Generates fraud probability scores for each transaction.
* Provides downloadable prediction results as a CSV file.

## How It Works

1. **Training (in `creditcard-fraud-detection.ipynb`)**

   * Reads the dataset (`creditcard.csv`).
   * Performs preprocessing (scaling numeric features, one-hot encoding categorical features).
   * Uses SMOTE to handle class imbalance.
   * Trains a Random Forest classifier.
   * Saves the trained pipeline to `model.joblib`.

2. **Web App (in `main.py`)**

   * Loads the saved model pipeline (`model.joblib`).
   * Allows the user to upload a CSV file of transactions.
   * Extracts features and predicts fraud along with probability scores.
   * Displays predictions in the app and allows downloading them as a CSV.

## Usage

1. Run the Streamlit web app in the terminal:

```bash
streamlit run main.py
```

2. Upload a CSV file containing transactions.

   * The file should include columns like: `TransactionID`, `TransactionDate`, `Amount`, `MerchantID`, `TransactionType`, `Location`.

3. View predictions in the app.

4. Download the predictions as a CSV file.

---
>>>>>>> baea5501c35f33d79d5283ae056a1fbedbb627bc
