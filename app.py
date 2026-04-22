import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("📊 Trader Performance vs Market Sentiment")
st.caption("Interactive analytics dashboard using trading data + Fear/Greed sentiment index")

# -------------------- SIDEBAR --------------------
st.sidebar.header("📂 Data Source")

st.sidebar.info("You can upload your own datasets or use the default project data.")

sentiment_file = st.sidebar.file_uploader("Sentiment CSV", type=["csv"])
trades_file = st.sidebar.file_uploader("Trades CSV", type=["csv"])

# -------------------- LOAD DATA (UPLOAD OR DEFAULT) --------------------
try:
    if sentiment_file is not None:
        sentiment = pd.read_csv(sentiment_file)
    else:
        sentiment = pd.read_csv("fear_greed_index.csv")

    if trades_file is not None:
        trades = pd.read_csv(trades_file)
    else:
        trades = pd.read_csv("historical_data.csv")

    st.sidebar.success("Data loaded successfully ✔")

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# -------------------- CLEAN DATA --------------------
sentiment.columns = sentiment.columns.str.lower()
trades.columns = trades.columns.str.lower()

# Date conversion (safe handling)
sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date
trades['timestamp'] = pd.to_datetime(trades['timestamp'], unit='ms')
trades['date'] = trades['timestamp'].dt.date

# -------------------- MERGE --------------------
df = pd.merge(
    trades,
    sentiment[['date', 'classification']],
    on='date',
    how='left'
)

# -------------------- FEATURE ENGINEERING --------------------
df['sentiment'] = df['classification'].apply(
    lambda x: 'Fear' if 'Fear' in str(x) else 'Greed'
)

df['is_long'] = df['side'].apply(lambda x: 1 if str(x).upper() == 'BUY' else 0)

# -------------------- FILTERS --------------------
st.sidebar.subheader("🔎 Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    ['Fear', 'Greed'],
    default=['Fear', 'Greed']
)

df = df[df['sentiment'].isin(sentiment_filter)]

# -------------------- TABS --------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📌 Overview",
    "📊 PnL Analysis",
    "📈 Behavior",
    "🧩 Segmentation"
])

# -------------------- TAB 1: OVERVIEW --------------------
with tab1:
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Trades", len(df))
    col2.metric("Unique Traders", df['account'].nunique())
    col3.metric("Avg PnL", round(df['closed pnl'].mean(), 2))

    st.dataframe(df.head(), use_container_width=True)

    fig, ax = plt.subplots()
    df['sentiment'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title("Sentiment Distribution")
    st.pyplot(fig)

# -------------------- TAB 2: PNL ANALYSIS --------------------
with tab2:
    st.subheader("PnL Distribution by Sentiment")

    fig, ax = plt.subplots()
    sns.boxplot(x='sentiment', y='closed pnl', data=df, ax=ax)
    ax.set_title("PnL vs Market Sentiment")
    st.pyplot(fig)

# -------------------- TAB 3: BEHAVIOR --------------------
with tab3:
    st.subheader("Trader Behavior Patterns")

    behavior = df.groupby('sentiment')[['size usd', 'is_long']].mean()

    fig, ax = plt.subplots()
    behavior.plot(kind='bar', ax=ax)
    ax.set_title("Behavior under Market Sentiment")
    st.pyplot(fig)

    st.write("Average Behavior Metrics")
    st.dataframe(behavior)

# -------------------- TAB 4: SEGMENTATION --------------------
with tab4:
    st.subheader("Trader Segmentation Analysis")

    daily = df.groupby(['account', 'date']).agg(
        pnl=('closed pnl', 'sum'),
        trades=('account', 'count')
    ).reset_index()

    median_trades = daily['trades'].median()

    daily['type'] = daily['trades'].apply(
        lambda x: 'Frequent' if x > median_trades else 'Infrequent'
    )

    seg = daily.groupby('type')['pnl'].mean()

    fig, ax = plt.subplots()
    seg.plot(kind='bar', ax=ax)
    ax.set_title("Profitability by Trader Type")
    st.pyplot(fig)

# -------------------- INSIGHTS --------------------
st.markdown("---")
st.subheader("🧠 Key Insights")

st.markdown("""
- Traders show higher activity during **Greed phases**
- Increased activity does not guarantee higher profits → possible overtrading
- Fear phases show more stable and cautious trading behavior
""")

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("Built for financial behavior analysis using sentiment-driven trading data")
