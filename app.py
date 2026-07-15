import pandas as pd
import numpy as np
import joblib

# Load the scaler and kmeans model
scaler = joblib.load('scaler.pkl')
kmeans = joblib.load('kmeans_model.pkl')

def predict_cluster(annual_income, spending_score):
    """
    Predicts the customer cluster based on annual income and spending score.
    """
    # Create a DataFrame for the new data point
    new_customer_data = pd.DataFrame([{
        'Annual Income (k$)': annual_income,
        'Spending Score (1-100)': spending_score
    }])
    
    # Scale the new data point using the loaded scaler
    new_customer_scaled = scaler.transform(new_customer_data)
    
    # Predict the cluster
    cluster = kmeans.predict(new_customer_scaled)[0]
    
    return int(cluster)

if __name__ == '__main__':
    print("Customer Segmentation Prediction Application")
    
    # Example prediction
    # Let's use an example from the dataset, e.g., customer 0: (15, 39) -> Cluster 0
    # Or customer 1: (15, 81) -> Cluster 2
    
    example_annual_income = 15
    example_spending_score = 39
    predicted_cluster = predict_cluster(example_annual_income, example_spending_score)
    print(f"For Annual Income (k$): {example_annual_income}, Spending Score (1-100): {example_spending_score}, Predicted Cluster: {predicted_cluster}")
    
    example_annual_income_2 = 15
    example_spending_score_2 = 81
    predicted_cluster_2 = predict_cluster(example_annual_income_2, example_spending_score_2)
    print(f"For Annual Income (k$): {example_annual_income_2}, Spending Score (1-100): {example_spending_score_2}, Predicted Cluster: {predicted_cluster_2}")

    # You can also add more interactive input if desired
    # income = float(input("Enter Annual Income (k$): "))
    # spending = float(input("Enter Spending Score (1-100): "))
    # custom_cluster = predict_cluster(income, spending)
    # print(f"Predicted Cluster for your input: {custom_cluster}")
