# Credit Card Fraud Detection (Jupyter/Colab Project)

## Overview

This notebook trains a credit card fraud detection model using a Random Forest classifier combined with SMOTE to handle the dataset's heavy class imbalance. It includes visualizations, model evaluation, and example predictions.

---

## What This Project Does

* Loads and explores the **creditcard.csv** dataset
* Visualizes class imbalance
* Builds a pipeline with **StandardScaler + SMOTE + RandomForest**
* Trains and evaluates the model
* Displays:

  * Class distribution plot
  * Confusion matrix
  * Feature importance chart
* Saves the trained model as `model.joblib`
* Generates sample predictions with fraud probability scores

---

## How to Use

1. Download 'creditcard.csv' from here https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud and upload it into the notebook.
2. Run all cells in order to train the model and view results.
3. Download the trained model if needed:

   ```python
   files.download("model.joblib")
   ```

---

## Notes

* The dataset must include a **Class** column (0 = legit, 1 = fraud).
* All steps run in a single notebook with no additional setup beyond uploading the CSV.

---
