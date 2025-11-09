# Credit Card Fraud Detection

This project provides a credit card fraud detection system using machine learning. It includes a Jupyter notebook for training the model and a Streamlit web app for making predictions on new transaction data.

## Project Structure

* `creditcard-fraud-detection.ipynb` – Trains and builds the fraud detection model using **pandas**, **scikit-learn**, **imbalanced-learn**, and **joblib**.
* `model.joblib` – The trained machine learning pipeline (150 MB) saved using **Git LFS**.
* `main.py` – Streamlit web app that loads `model.joblib` and predicts fraud on uploaded CSV files.
* `README.md` – This file.
* `requirements.txt` – Python dependencies (optional; your repo may have it for reference).

---

## Features

* Detects potential credit card fraud in transaction data.
* Handles numeric and categorical features.
* Balances the dataset using SMOTE to handle class imbalance.
* Generates fraud probability scores for each transaction.
* Provides downloadable prediction results as a CSV file.

---

## How It Works

1. **Training (in `creditcard-fraud-detection.ipynb`)**

   * Reads the dataset (`creditcard.csv`).
   * Performs preprocessing:

     * Scales numeric features (`Amount`, `TransactionHour`)
     * One-hot encodes categorical features (`MerchantID`, `TransactionType`, `Location`)
   * Handles class imbalance using SMOTE.
   * Trains a Random Forest classifier.
   * Saves the trained pipeline to `model.joblib`.

2. **Web App (in `main.py`)**

   * Loads the saved model pipeline (`model.joblib`).
   * Allows the user to upload a CSV file with transactions.
   * Extracts features and predicts fraud along with probability scores.
   * Displays predictions in the app and allows downloading them as a CSV file.

---

## Setup and Usage

1. **Clone the repository**

```bash
git clone https://github.com/aviralmishra2005/Creditcard-Fraud.git
```

2. **Install dependencies** (if using `requirements.txt`)

```bash
pip install -r requirements.txt
```

> Make sure you have **Git LFS installed** to properly handle `model.joblib`.

3. **Run the Streamlit web app in your local repository folder**

```bash
streamlit run main.py
```

4. **Upload a CSV file** containing transactions.

   * The CSV should include columns like:
     `TransactionID`, `TransactionDate`, `Amount`, `MerchantID`, `TransactionType`, `Location`.

5. **View predictions** in the app and download them as a CSV file.

---

## Notes

* The `model.joblib` file is tracked with **Git LFS** due to its large size (150 MB).
* The app automatically computes `TransactionHour` from `TransactionDate`.
* The pipeline includes preprocessing, oversampling with SMOTE, and a Random Forest classifier.

---
