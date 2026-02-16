import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Page configuration
st.set_page_config(page_title="Trend Analysis Dashboard", layout="wide")

# Title
st.title("📊 Trend Analysis Dashboard")
st.markdown("Final Year Project - Multi-Industry Trend Prediction System")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("synthetic_trend_dataset.csv")
    return df

df = load_data()

# Create Trend Category
def trend_category(score):
    if score >= 0.6:
        return "Rising"
    elif score >= 0.4:
        return "Stable"
    else:
        return "Declining"

df["TrendCategory"] = df["TrendScore"].apply(trend_category)

# Sidebar Filter
st.sidebar.header("Filter Options")
selected_industry = st.sidebar.selectbox(
    "Select Industry", df["Industry"].unique()
)

filtered_df = df[df["Industry"] == selected_industry]

# KPIs
st.subheader(f"Key Metrics - {selected_industry}")
col1, col2, col3 = st.columns(3)

col1.metric("Average Revenue", f"${filtered_df['Revenue'].mean():,.0f}")
col2.metric("Average Customers", f"{filtered_df['Customers'].mean():,.0f}")
col3.metric("Average Trend Score", f"{filtered_df['TrendScore'].mean():.2f}")

# Trend Score Chart
st.subheader("Trend Score Over Time")
fig1 = px.line(filtered_df, x="Month", y="TrendScore", markers=True)
st.plotly_chart(fig1, use_container_width=True)

# Revenue Chart
st.subheader("Revenue Trend")
fig2 = px.line(filtered_df, x="Month", y="Revenue", color_discrete_sequence=["green"])
st.plotly_chart(fig2, use_container_width=True)

# Customer Chart
st.subheader("Customer Growth")
fig3 = px.line(filtered_df, x="Month", y="Customers", color_discrete_sequence=["blue"])
st.plotly_chart(fig3, use_container_width=True)

# Machine Learning Model
st.header("Trend Score Prediction")

label_encoder = LabelEncoder()
df["Industry_Encoded"] = label_encoder.fit_transform(df["Industry"])

X = df[["Industry_Encoded", "Month", "Revenue", "Customers", "GrowthRate"]]
y = df["TrendScore"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# User Inputs
month = st.slider("Future Month", 1, 60, 37)
revenue = st.number_input("Expected Revenue", value=80000)
customers = st.number_input("Expected Customers", value=3000)
growth = st.slider("Growth Rate", 0.0, 0.2, 0.05)

industry_encoded = label_encoder.transform([selected_industry])[0]

if st.button("Predict Trend"):
    new_data = np.array([[industry_encoded, month, revenue, customers, growth]])
    prediction = model.predict(new_data)[0]

    if prediction >= 0.6:
        category = "Rising 📈"
    elif prediction >= 0.4:
        category = "Stable ➖"
    else:
        category = "Declining 📉"

    st.success(f"Predicted Trend Score: {prediction:.3f}")
    st.info(f"Trend Category: {category}")
