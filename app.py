import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

# Load model and dataset (for visual comparison)
model = joblib.load("churn_model.pkl")
data = pd.read_csv("sales_churn_data.csv")

# Sidebar Input
st.set_page_config(page_title="Sales Churn Dashboard", layout="wide")
st.sidebar.header("📋 Customer Input")

industry = st.sidebar.selectbox("Industry", ["SaaS", "Retail", "Healthcare", "Other"])
region = st.sidebar.selectbox("Region", ["North America", "Europe", "South America", "Asia"])
sales_calls_last_30d = st.sidebar.number_input("Sales Calls (Last 30 Days)", min_value=0, value=10)
support_tickets_last_30d = st.sidebar.number_input("Support Tickets (Last 30 Days)", min_value=0, value=2)
days_since_last_login = st.sidebar.number_input("Days Since Last Login", min_value=0, value=10)
total_revenue = st.sidebar.number_input("Total Revenue", min_value=0, value=5000)
subscription_age_months = st.sidebar.number_input("Subscription Age (Months)", min_value=1, value=12)

input_df = pd.DataFrame([{
    'sales_calls_last_30d': sales_calls_last_30d,
    'support_tickets_last_30d': support_tickets_last_30d,
    'days_since_last_login': days_since_last_login,
    'total_revenue': total_revenue,
    'subscription_age_months': subscription_age_months
}])

# Predict
prediction = model.predict(input_df)[0]
probability = model.predict_proba(input_df)[0][1]

# Title Section
st.title("📊 Sales Churn Prediction Dashboard")
st.markdown("This dashboard visualizes the churn prediction and compares input data with average churned customers.")

# Prediction Display
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Prediction", value="❌ Churn" if prediction else "✅ Not Churn")
    st.metric(label="Churn Probability", value=f"{probability:.2f}")

with col2:
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Churn Likelihood (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "crimson" if prediction else "green"},
            'steps': [
                {'range': [0, 50], 'color': 'lightgreen'},
                {'range': [50, 100], 'color': 'lightcoral'}
            ]
        }
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

# Comparison Bar Chart
churned_avg = data[data["churn"] == 1][input_df.columns].mean().reset_index()
churned_avg.columns = ["Feature", "Churned_Avg"]
user_input_melted = input_df.melt(var_name="Feature", value_name="User_Input")
merged = pd.merge(churned_avg, user_input_melted, on="Feature")

fig_bar = px.bar(merged, x="Feature", y=["Churned_Avg", "User_Input"],
                 barmode="group", title="📉 Feature Comparison: Input vs Avg Churned")

st.plotly_chart(fig_bar, use_container_width=True)
