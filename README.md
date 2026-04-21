# 📊 Trader_Sentiment_Analysis
End-to-end data analysis project examining trader behavior under Fear vs Greed market conditions, including feature engineering, modeling, and a Streamlit dashboard.


📌 Objective


The goal of this project is to analyze how market sentiment (Fear vs Greed) impacts trader behavior and performance, and to derive actionable insights that can inform trading strategies.


🧠 Methodology


Cleaned and merged trader data with market sentiment data
Converted timestamps and aligned datasets at a daily level


Engineered key features:


Daily PnL per trader
Trade frequency
Average position size
Long/short ratio
Performed exploratory data analysis to compare behavior across sentiment regimes
Built a Random Forest model to predict trade profitability


📊 Key Insights


Higher trading activity during Greed phases
Traders execute more trades and take larger positions during Greed periods, indicating risk-seeking behavior.
Overtrading reduces efficiency
Increased activity during Greed does not lead to proportional gains in profitability, suggesting diminishing returns.
More disciplined behavior during Fear phases
Traders tend to be more cautious, resulting in lower activity but relatively stable outcomes.


🤖 Predictive Modeling


Initial model accuracy: ~78% (random split)
Improved evaluation using time-aware validation to reduce data leakage


Conclusion:


While trader behavior and sentiment provide some predictive signal, profitability remains highly influenced by market randomness and execution timing.


💡 Strategy Recommendations


Limit overtrading during Greed periods to reduce exposure to volatility
Adopt selective, disciplined trading during Fear periods for more stable outcomes


📊 Dashboard

An interactive dashboard built using Streamlit allows users to:

Explore sentiment distribution
Analyze PnL across market conditions
Compare trader behavior
View segmentation insights


⚙️ Tech Stack


Python
Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn
Streamlit


▶️ How to Run


Clone the repository


Install dependencies:                pip install -r requirements.txt


Run the dashboard:                   streamlit run app.py
