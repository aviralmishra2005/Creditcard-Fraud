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