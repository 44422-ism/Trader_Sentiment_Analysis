📊 Trader Sentiment Analysis 


📌 Project Overview


This project is a data analysis and machine learning prototype that examines how market sentiment (Fear vs Greed) influences trader behavior and performance. The analysis is performed using historical trading data and sentiment indices, and the results are deployed as an interactive Streamlit web application.


The app allows users to:

Upload trading and sentiment datasets

Analyze trader performance across market conditions

Visualize PnL distribution under Fear vs Greed

Explore trading behavior and activity patterns

View segmented insights on trader types


⚙️ Tech Stack


Frontend (Dashboard)

Streamlit → Interactive web interface

Python → Data handling and visualization

Backend (Data Analysis & Modeling)

Pandas → Data cleaning and transformation

NumPy → Numerical operations

Matplotlib & Seaborn → Data visualization

Scikit-learn → Machine learning model (Random Forest)


📂 Directory Structure


app.py                # Main Streamlit dashboard  requirements.txt      # Python dependencies  README.md             # Project documentation  


🚀 How to Run the Project


Clone the repository:

git clone https://github.com/44422-ism/Trader_Sentiment_Analysis.gitcd Trader_Sentiment_Analysis


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


📊 Key Insights


Traders are more active during Greed phases, indicating risk-taking behavior

Increased activity does not guarantee higher profitability → evidence of overtrading

Fear phases show more cautious and relatively stable trading patterns

Behavioral trends vary significantly across sentiment conditions



🔬 Limitations (Current Version)


Model accuracy is limited due to dataset size and features

Market behavior is inherently unpredictable → limited predictive reliability

Analysis is based on historical data and may not generalize to real-time markets

Sentiment classification is simplified (Fear vs Greed only)



🌱 Future Scope


Integration with real-time market sentiment APIs


Advanced feature engineering (volatility, leverage, timing signals)


Improved ML models and time-series validation


Enhanced dashboard with filters and live analytics


Deployment with continuous data updates



📦 Software Requirements


Python 3.8+


Streamlit


Pandas


NumPy


Matplotlib


Seaborn


Scikit-learn



📈 Business & Impact


This project demonstrates how data-driven insights can help in:

Understanding trader psychology under different market conditions

Identifying inefficient trading patterns like overtrading

Supporting better decision-making strategies

Building scalable analytics tools for financial markets



✨ This is a prototype project created for educational and analytical purposes, not for financial advice or real-world trading decisions.

📌 About
A data analysis and machine learning project that explores the relationship between market sentiment and trader performance, deployed as an interactive Streamlit dashboard.
