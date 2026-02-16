# 📊 Trend Analysis Dashboard (Final Year Project)

## 🎓 Project Overview

This project presents a **Machine Learning-Based Trend Analysis Dashboard** developed as a final year undergraduate system. The dashboard analyzes multi-industry trends using synthetic time-series data and predicts future trend scores using a Random Forest Regressor model.

The system provides interactive visual analytics and real-time trend prediction for five major industries over a 36-month period.

---

## 🏭 Selected Industries

* 🛍️ Retail
* 🏥 Healthcare
* 💻 Technology
* 🚚 Transportation
* 💰 Finance

Each industry is modeled with realistic growth behavior:

* Technology → Fast growth
* Healthcare → Stable growth
* Retail → Moderate fluctuations
* Transportation → Seasonal patterns
* Finance → Steady growth

---

## 🧠 Key Features

✔ Interactive Streamlit Dashboard
✔ Machine Learning Trend Prediction (Random Forest)
✔ Multi-Industry Data Analysis
✔ 36 Months Synthetic Dataset
✔ Trend Classification (Rising, Stable, Declining)
✔ KPI Metrics (Revenue, Customers, Trend Score)
✔ Professional Visualization using Plotly

---

## 📂 Project Structure

```
trend-analysis-dashboard/
│
├── app.py                        # Streamlit Dashboard Application
├── synthetic_trend_dataset.csv   # Synthetic Dataset (36 months × 5 industries)
├── requirements.txt              # Project Dependencies
└── README.md                     # Project Documentation
```

---

## 📊 Dataset Description

The dataset is synthetically generated for academic research purposes and contains the following attributes:

| Column Name | Description                                  |
| ----------- | -------------------------------------------- |
| Industry    | Industry category (Retail, Healthcare, etc.) |
| Month       | Time period (1–36 months)                    |
| Revenue     | Monthly revenue values                       |
| Customers   | Number of customers                          |
| GrowthRate  | Monthly growth rate                          |
| TrendScore  | Target variable (0 to 1)                     |

---

## 🤖 Machine Learning Model

* Model Used: **Random Forest Regressor**
* Purpose: Predict Trend Score based on industry metrics
* Input Features:

  * Industry (Encoded)
  * Month
  * Revenue
  * Customers
  * Growth Rate
* Output:

  * Predicted Trend Score (0–1)

---

## 📈 Trend Classification Logic

| Trend Score Range | Category     |
| ----------------- | ------------ |
| ≥ 0.6             | 📈 Rising    |
| 0.4 – 0.6         | ➖ Stable     |
| ≤ 0.4             | 📉 Declining |

---

## 🖥️ Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* Scikit-learn
* NumPy
* Visual Studio Code
* Git & GitHub

---

## ⚙️ Installation & Setup (Local Run)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/trend-analysis-dashboard.git
cd trend-analysis-dashboard
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit App

```bash
streamlit run app.py
```

The dashboard will open in your browser at:

```
http://localhost:8501
```

---

## 🚀 Deployment (Streamlit Cloud)

This project is deployed using Streamlit Cloud for online access and demonstration.

Deployment Steps:

1. Upload project to GitHub
2. Connect GitHub to Streamlit Cloud
3. Select repository and app.py
4. Deploy the application

---

## 🎓 Academic Contribution

This project demonstrates:

* End-to-end machine learning pipeline
* Synthetic data generation for research
* Interactive dashboard development
* Predictive analytics for trend forecasting
* Decision support system design

The system is suitable for academic evaluation, research presentation, and real-time trend analysis demonstrations.

---

## 👨‍🎓 Author

Final Year Undergraduate
Trend Analysis Dashboard Project
Machine Learning & Data Analytics

---

## 📜 License

This project is developed for academic and educational purposes.
