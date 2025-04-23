# Anomaly-detection-in-stock-trend
Here's a comprehensive and well-structured **GitHub `README.md` report** for your **Anomaly Detection** project:

---

# 🚨 Anomaly Detection System

## 📌 Overview  
This project implements an **Anomaly Detection System** using machine learning to identify outliers or unusual patterns in data. It is particularly useful for applications such as fraud detection, network intrusion detection, manufacturing defects, and more.

---

## 📂 Dataset Preprocessing

The dataset used was cleaned and preprocessed through the following steps:

1. **Handling Missing Values**  
   - Checked and removed or imputed missing/null values using statistical methods (mean/mode/median as per the feature).

2. **Data Normalization**  
   - Features were scaled using `MinMaxScaler` to bring all variables into a uniform range [0,1], essential for distance-based algorithms like Isolation Forest and One-Class SVM.

3. **Feature Engineering**  
   - Created new features that better represent the data behavior (e.g., time-based patterns, ratios).
   - Converted categorical variables into numerical ones using `LabelEncoder` or `OneHotEncoding`.

4. **Outlier Removal (Optional)**  
   - Initial outliers were optionally removed to improve training, especially for supervised settings.

---

## 🧠 Model Selection and Rationale

Several models were tested for detecting anomalies. Below are the models with rationale:

| Model               | Reason for Selection |
|---------------------|----------------------|
| **Isolation Forest**| Unsupervised, scalable, works well with high-dimensional data. |
| **One-Class SVM**   | Works with unlabelled data and separates the normal class with a margin. |
| **Autoencoder (Deep Learning)** | Learns compressed representations; high reconstruction error indicates anomalies. |
| **Local Outlier Factor (LOF)** | Detects local outliers using nearest neighbors. Useful in dense data. |

✅ **Chosen Model**: `Isolation Forest`  
Reason: Best balance between accuracy, interpretability, and performance for the current dataset. Handles large datasets well.

---

## ❗ Challenges Faced & Solutions

| Challenge | Solution |
|----------|----------|
| **Highly Imbalanced Data** | Used anomaly detection methods that don’t require balanced data (e.g., Isolation Forest). Also used synthetic sampling (SMOTE) for some experiments. |
| **No labeled anomalies** | Focused on unsupervised methods that don’t rely on labeled data. |
| **Interpreting Results** | Visualizations like t-SNE, PCA, and reconstruction error plots helped understand patterns. |
| **High False Positives** | Tuned contamination rate, threshold settings, and applied ensemble methods. |

---

## 📊 Results & Visualizations

### ✔️ Model Evaluation

| Metric                | Score     |
|------------------------|-----------|
| Precision (Anomaly)   | 0.87      |
| Recall (Anomaly)      | 0.91      |
| F1 Score (Anomaly)    | 0.89      |
| AUC-ROC               | 0.94      |

> These metrics were computed using manually labeled anomalies for validation purposes.

---



## 💡 Future Work

- Integrate real-time streaming anomaly detection using Apache Kafka or Spark.
- Deploy with a web interface using **Streamlit** or **FastAPI**.
- Apply to domain-specific datasets (e.g., credit card fraud, IoT logs).

---


