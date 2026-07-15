import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
scaler = joblib.load("scaler.pkl")
kmeans = joblib.load("kmeans_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ Customer Segmentation using K-Means")
st.write("Enter customer details to predict the customer segment.")

# User inputs
annual_income = st.number_input(
    "Annual Income (k$)",
    min_value=0.0,
    max_value=200.0,
    value=50.0
)

spending_score = st.number_input(
    "Spending Score (1-100)",
    min_value=1.0,
    max_value=100.0,
    value=50.0
)

if st.button("Predict Customer Cluster"):

    # Create dataframe
    new_customer = pd.DataFrame({
        "Annual Income (k$)": [annual_income],
        "Spending Score (1-100)": [spending_score]
    })

    # Scale
    scaled_data = scaler.transform(new_customer)

    # Predict
    cluster = kmeans.predict(scaled_data)[0]

    st.success(f"Predicted Customer Cluster: {cluster}")

    # Cluster description
    descriptions = {
        0: "Budget Customers 💰",
        1: "Average Customers 🙂",
        2: "Premium Customers 👑",
        3: "High Spending Customers 🛍️",
        4: "Potential Customers ⭐"
    }

    st.info(descriptions.get(cluster, "Customer Segment"))
