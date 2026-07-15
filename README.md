# 🛍️ Customer Segmentation Using K-Means Clustering

A Machine Learning project that segments retail store customers based on their **Annual Income** and **Spending Score** using the **K-Means Clustering** algorithm. The project includes an interactive **Streamlit web application** for predicting customer segments.

---

## 📖 Project Overview

Customer segmentation is an essential business strategy that helps organizations understand customer behavior and create targeted marketing campaigns. This project uses the K-Means clustering algorithm to group customers with similar purchasing patterns into different segments.

The trained model is deployed using **Streamlit**, allowing users to enter customer details and instantly predict the corresponding customer cluster.

---

## 🎯 Objectives

- Segment customers based on purchasing behavior.
- Apply the K-Means Clustering algorithm.
- Build an interactive Streamlit web application.
- Enable quick prediction of customer segments.
- Support data-driven business decisions.

---

## 🚀 Features

- Interactive and user-friendly interface.
- Customer cluster prediction.
- Data preprocessing using StandardScaler.
- Trained K-Means clustering model.
- Easy deployment with Streamlit Community Cloud.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

## 📂 Project Structure

```
customer-segmentation-using-kmeans/
│── app.py
│── scaler.pkl
│── kmeans_model.pkl
│── requirements.txt
│── README.md
```

---

## 📊 Dataset

The model is trained using customer purchase history with the following features:

- Annual Income (k$)
- Spending Score (1–100)

The data is standardized using **StandardScaler** before training the K-Means model.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/customer-segmentation-using-kmeans.git
```

### Navigate to the project folder

```bash
cd customer-segmentation-using-kmeans
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Launch the Streamlit application using:

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Workflow

1. Load customer dataset.
2. Select relevant features.
3. Standardize the data.
4. Train the K-Means clustering model.
5. Save the trained model and scaler using Joblib.
6. Load the saved model in Streamlit.
7. Predict customer clusters based on user input.

---

## 📌 Input Features

| Feature | Description |
|----------|-------------|
| Annual Income (k$) | Customer's annual income |
| Spending Score (1–100) | Customer's spending behavior score |

---

## 📌 Output

The application predicts the **Customer Cluster** based on the provided inputs.

Example:

| Annual Income | Spending Score | Predicted Cluster |
|---------------|---------------|-------------------|
| 15 | 39 | Cluster 0 |
| 15 | 81 | Cluster 2 |

---

## 📸 Screenshots

After deploying your application, add screenshots here.

Example:

- Home Page
- Prediction Result

---

## 🔮 Future Enhancements

- Interactive cluster visualization
- Upload custom datasets
- Customer analytics dashboard
- Automatic cluster interpretation
- Business recommendation system

---

## 👩‍💻 Author

**Gargi Katkamwar**

B.Tech – Electronics and Telecommunication Engineering

Machine Learning | Artificial Intelligence | Data Science Enthusiast
