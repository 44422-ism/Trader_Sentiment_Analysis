# 📊 Trader Sentiment Analysis Dashboard

## 🚀 Overview
This project is an interactive analytics dashboard that explores how **market sentiment (Fear vs Greed)** influences trader behavior, profitability, and risk-taking patterns.

It is designed as a **behavioral finance intelligence prototype** combining data analysis and machine learning concepts.

---

## 🎯 Problem Statement
Financial traders often behave differently under varying market emotions.  
This project aims to answer:

- Do traders take more risk during Greed phases?
- Does higher activity lead to higher profitability?
- How does sentiment impact trading performance?

---

## 📊 Key Features

- 📂 Upload or use default datasets
- 📊 PnL analysis across market sentiment conditions
- 📈 Trader behavior pattern analysis
- 🧩 Trader segmentation (Frequent vs Infrequent)
- 🧠 Automated insight generation
- 📉 Visual analytics dashboard with interactive filters

---

## ⚙️ Tech Stack

- **Frontend:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **ML Concepts:** Behavioral segmentation, statistical grouping

---

## 🧠 Key Insights Discovered

- Traders show higher activity during **Greed phases**
- Increased activity does NOT guarantee higher profits
- Fear phases lead to more stable trading behavior
- Behavioral differences are statistically significant across sentiment regimes


## 📂 Project Structure

  Trader_Sentiment_Analysis/
│

├── app.py

├── fear_greed_index.csv

├── historical_data.csv

├── Trader_Sentiment_Analysis.ipynb

├── README.md

└── requirements.txt

---
## 🚀 How to Run


* git clone https://github.com/44422-ism/Trader_Sentiment_Analysis.git

* cd Trader_Sentiment_Analysis
  
* pip install -r requirements.txt
  
* streamlit run app.py


📌 Limitations


1. Dataset size is limited for deep ML modeling

2. Market behavior is inherently stochastic

3. Sentiment classification is simplified (Fear vs Greed only)


🌱 Future Improvements


1. Real-time sentiment API integration

2. Advanced predictive modeling (time-series forecasting)

3. Portfolio risk scoring system

4. Deployment as SaaS analytics tool


📌 Author Note

This project was built as a data analytics and behavioral finance prototype to demonstrate end-to-end understanding of data pipelines, visualization, and insight generation.

✨ Disclaimer

This project is for educational and analytical purposes only and does not constitute financial advice.
---
